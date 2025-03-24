from abc import ABC, abstractmethod


# Класс-миксин для логирования создания объектов
class InitLoggerMixin:

    def __new__(cls, *args, **kwargs):
        print(f"Создан объект класса {cls.__name__} с параметрами:{args}, {kwargs}")
        return super().__new__(cls)


# Абстрактный базовый класс BaseProduct
class BaseProduct(ABC):
    @classmethod
    def new_product(cls, product_data: dict):
        """Общий метод для создания нового объекта с базовыми проверками."""
        required_keys = cls.required_keys  # type: ignore[attr-defined]
        if not required_keys.issubset(product_data.keys()):
            raise ValueError(f"Необходимые ключи: {required_keys}. Получено: {product_data.keys()}")

        for key, expected_type in cls.type_checks.items():  # type: ignore[attr-defined]
            if not isinstance(product_data[key], expected_type):
                raise TypeError(f"{key} должно быть типа {expected_type}, получено {type(product_data[key])}")

        if 'price' in product_data and product_data['price'] <= 0:
            raise ValueError("Цена не должна быть нулевой или отрицательной.")
        if 'quantity' in product_data and product_data['quantity'] < 0:
            raise ValueError("Количество не может быть отрицательным.")

        return cls(**product_data)  # type: ignore[attr-defined]

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @property
    @abstractmethod
    def quantity(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


# Класс Product с добавленным миксином
class Product(InitLoggerMixin, BaseProduct):
    required_keys = {'name', 'description', 'price', 'quantity'}
    type_checks = {
        'name': str,
        'description': str,
        'price': (int, float),
        'quantity': int
    }

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self._name = name
        self._description = description
        self.__price = price
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Цена должна быть числом.")
        if value <= 0:
            raise ValueError("Цена не должна быть нулевой или отрицательной.")
        self.__price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Количество должно быть целым числом.")
        if value < 0:
            raise ValueError("Количество не может быть отрицательным.")
        self._quantity = value

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product.")
        if type(self) != type(other):
            raise TypeError("Можно складывать только объекты одного и того же класса.")
        return (self.price * self.quantity) + (other.price * other.quantity)


# Класс Smartphone, наследующийся от Product
class Smartphone(Product):
    required_keys = {'name', 'description', 'price', 'quantity', 'efficiency', 'model', 'memory', 'color'}
    type_checks = {
        'name': str,
        'description': str,
        'price': (int, float),
        'quantity': int,
        'efficiency': str,
        'model': str,
        'memory': int,
        'color': str
    }

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: str, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return f"{super().__str__()}, Модель: {self.model}, Цвет: {self.color}"


# Класс LawnGrass, наследующийся от Product
class LawnGrass(Product):
    required_keys = {'name', 'description', 'price', 'quantity', 'country', 'germination_period', 'color'}
    type_checks = {
        'name': str,
        'description': str,
        'price': (int, float),
        'quantity': int,
        'country': str,
        'germination_period': str,
        'color': str
    }

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return f"{super().__str__()}, Страна: {self.country}, Цвет: {self.color}"


# Класс Category для управления списком продуктов
class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []
        Category.total_categories += 1

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только экземпляры класса Product.")
        self.__products.append(product)
        Category.total_products += 1

    def remove_product(self, product: Product, ignore_not_found: bool = False):
        if product in self.__products:
            self.__products.remove(product)
            Category.total_products -= 1
        elif not ignore_not_found:
            raise ValueError("Продукт не найден в категории.")

    def update_product_quantity(self, product: Product, new_quantity: int):
        if product not in self.__products:
            raise ValueError("Продукт не найден в категории.")
        if not isinstance(new_quantity, int) or new_quantity < 0:
            raise ValueError("Количество товара должно быть неотрицательным целым числом.")
        product.quantity = new_quantity

    @property
    def products_info(self):
        if not self.__products:
            return "В категории нет товаров."
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


if __name__ == "__main__":
    # Создание объекта Product
    product = Product('Продукт1', 'Описание продукта', 1200, 10)

    # Создание объекта Smartphone
    smartphone = Smartphone('Смартфон1', 'Описание смартфона', 10000, 5, 'Высокая', 'МодельX', 128, 'Черный')

    # Создание объекта LawnGrass
    lawn_grass = LawnGrass('Трава1', 'Описание травы', 500, 20, 'Россия', '10 дней', 'Зелёный')
