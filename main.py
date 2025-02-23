class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут цены
        self.quantity = quantity

    def __str__(self):
        return (f"Product(name={self.name}, description={self.description}, "
                f"price={self.__price}, quantity={self.quantity})")

    @classmethod
    def new_product(cls, product_data: dict):
        """Создает новый объект класса Product на основе словаря с параметрами товара)."""
        required_keys = {'name', 'description', 'price', 'quantity'}
        if not required_keys.issubset(product_data.keys()):
            raise ValueError(f"Необходимые ключи: {required_keys}. Полученные ключи: {product_data.keys()}")
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    @property
    def price(self):
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, value: float):
        """Сеттер для цены с проверкой."""
        if value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        self.__price = value


class Category:
    total_categories = 0  # Счетчик общего количества категорий
    total_products = 0    # Счетчик общего количества товаров

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []  # Приватный список для хранения продуктов

        # Увеличиваем счетчик категорий при создании новой категории
        Category.total_categories += 1

    def add_product(self, product: Product):
        """Добавляет продукт в категорию."""
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только экземпляры класса Product.")
        self.__products.append(product)
        # Увеличиваем счетчик товаров при добавлении нового продукта
        Category.total_products += 1

    def remove_product(self, product: Product):
        """Удаляет продукт из категории."""
        if product in self.__products:
            self.__products.remove(product)
            # Уменьшаем счетчик товаров при удалении продукта
            Category.total_products -= 1
        else:
            raise ValueError("Продукт не найден в категории.")

    @property
    def products_info(self):
        """Возвращает строковое представление списка товаров в категории."""
        if not self.__products:
            return "В категории нет товаров."
        return "\n".join(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products)

    def __str__(self):
        return (f"Category(name={self.name}, description={self.description}, "
                f"products=[{self.products_info}])")


# Пример использования
if __name__ == "__main__":
    # Создаются два продукта с использованием класс-метода new_product
    product_data1 = {
        'name': "Ноутбук",
        'description': "Профессиональный ноутбук",
        'price': 1200.0,
        'quantity': 10
    }
    product_data2 = {
        'name': "Мышь",
        'description': "Оптическая мышь",
        'price': 25.0,
        'quantity': 50
    }

    product1 = Product.new_product(product_data1)
    product2 = Product.new_product(product_data2)

    # Создание категории
    electronics = Category(name="Электроника", description="Категория электронных товаров")

    # Добавление продуктов в категорию
    electronics.add_product(product1)
    electronics.add_product(product2)

    # Вывод информации о категории
    print(electronics)

    # Вывод общего количества категорий и товаров
    print(f"Общее количество категорий: {Category.total_categories}")
    print(f"Общее количество товаров: {Category.total_products}")

    # Удаление продукта из категории
    electronics.remove_product(product1)

    # Вывод информации о категории после удаления продукта
    print(electronics)

    # Вывод общего количества категорий и товаров после удаления продукта
    print(f"Общее количество категорий: {Category.total_categories}")
    print(f"Общее количество товаров: {Category.total_products}")

    # Создание еще одной категории
    books = Category(name="Книги", description="Категория книг")

    # Добавление продукта в новую категорию
    book_data = {
        'name': "Приключения",
        'description': "Книга о приключениях",
        'price': 15.0,
        'quantity': 30
    }
    book1 = Product.new_product(book_data)
    books.add_product(book1)

    # Вывод информации о новой категории
    print(books)

    # Вывод общего количества категорий и товаров после добавления новой категории и продукта
    print(f"Общее количество категорий: {Category.total_categories}")
    print(f"Общее количество товаров: {Category.total_products}")

    # Пример использования геттера products_info
    print("Список товаров в категории 'Электроника':")
    print(electronics.products_info)

    print("Список товаров в категории 'Книги':")
    print(books.products_info)

    # Пример использования геттера и сеттера для цены
    print(f"Цена продукта {product2.name}: {product2.price}")
    product2.price = 30.0  # Успешное обновление цены
    print(f"Цена продукта {product2.name} после обновления: {product2.price}")
    product2.price = -10.0  # Попытка установить неправильную цену
    print(f"Цена продукта {product2.name} после неправильной попытки обновления: {product2.price}")