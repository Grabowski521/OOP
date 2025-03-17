class ProductMixin:
    @classmethod
    def new_product(cls, product_data: dict):
        """Общий метод для создания нового объекта с базовыми проверками."""
        # Проверка наличия всех необходимых ключей
        required_keys = cls.required_keys
        if not required_keys.issubset(product_data.keys()):
            raise ValueError(f"Необходимые ключи: {required_keys}. Получено: {product_data.keys()}")

        # Проверка типов данных
        for key, expected_type in cls.type_checks.items():
            if not isinstance(product_data[key], expected_type):
                raise TypeError(f"{key} должно быть типа {expected_type}, получено {type(product_data[key])}")

        # Проверка на неотрицательную цену
        if 'price' in product_data and product_data['price'] <= 0:
            raise ValueError("Цена не должна быть нулевой или отрицательной.")

        # Создание объекта с помощью конструктора класса
        return cls(**product_data)

class Product(ProductMixin):
    required_keys = {'name', 'description', 'price', 'quantity'}
    type_checks = {
        'name': str,
        'description': str,
        'price': (int, float),
        'quantity': int
    }

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

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

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product.")
        if type(self) != type(other):
            raise TypeError("Можно складывать только объекты одного и того же класса.")
        return (self.price * self.quantity) + (other.price * other.quantity)

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
        return "\n".join(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

if __name__ == "__main__":
    # Создание смартфона через new_product
    smartphone_data = {
        "name": "iPhone 14",
        "description": "Смартфон от Apple",
        "price": 999.9,
        "quantity": 50,
        "efficiency": "A15 Bionic",
        "model": "14 Pro",
        "memory": 256,
        "color": "Space Gray"
    }
    smartphone = Smartphone.new_product(smartphone_data)

    # Создание газонной травы через new_product
    lawn_grass_data = {
        "name": "Green Lawn",
        "description": "Газонная трава",
        "price": 19.99,
        "quantity": 100,
        "country": "Russia",
        "germination_period": "14 days",
        "color": "Green"
    }
    lawn_grass = LawnGrass.new_product(lawn_grass_data)

    # Попытка сложить смартфон и газонную траву
    try:
        total_cost = smartphone + lawn_grass
        print(f"Общая стоимость товаров: {total_cost}")
    except TypeError as e:
        print(e)  # Ожидаем: "Можно складывать только объекты одного и того же класса."

    # Создание второго смартфона
    smartphone2_data = {
        "name": "Samsung Galaxy S21",
        "description": "Смартфон от Samsung",
        "price": 899.99,
        "quantity": 30,
        "efficiency": "Exynos 2100",
        "model": "S21",
        "memory": 128,
        "color": "Phantom Black"
    }
    smartphone2 = Smartphone.new_product(smartphone2_data)

    # Сложение двух смартфонов
    total_smartphones = smartphone + smartphone2
    print(f"Общая стоимость смартфонов: {total_smartphones}")