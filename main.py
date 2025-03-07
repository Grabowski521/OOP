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
        """Создает новый объект класса Product на основе словаря с параметрами товара."""
        required_keys = {'name', 'description', 'price', 'quantity'}
        if not required_keys.issubset(product_data.keys()):
            raise ValueError(f"Необходимые ключи: {required_keys}. Полученные ключи: {product_data.keys()}")

        # Проверка типов данных
        if not isinstance(product_data['name'], str):
            raise TypeError("Имя товара должно быть строкой.")
        if not isinstance(product_data['description'], str):
            raise TypeError("Описание товара должно быть строкой.")
        if not isinstance(product_data['price'], (int, float)):
            raise TypeError("Цена товара должна быть числом.")
        if not isinstance(product_data['quantity'], int):
            raise TypeError("Количество товара должно быть целым числом.")

        # Добавляем проверку на неотрицательную цену
        if product_data['price'] <= 0:
            raise ValueError("Цена не должна быть нулевой или отрицательной.")

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
        if not isinstance(value, (int, float)):
            raise TypeError("Цена должна быть числом.")
        if value <= 0:
            raise ValueError("Цена не должна быть нулевой или отрицательной.")
        self.__price = value

    def __add__(self, other):
        """Метод для сложения двух объектов Product."""
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product.")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Category:
    total_categories = 0  # Счетчик общего количества категорий
    total_products = 0    # Счетчик общего количества товаров

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []  # Приватный список для хранения продуктов
        Category.total_categories += 1

    def add_product(self, product: Product):
        """Добавляет продукт в категорию."""
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только экземпляры класса Product.")
        self.__products.append(product)
        Category.total_products += 1

    def remove_product(self, product: Product, ignore_not_found: bool = False):
        """
        Удаляет продукт из категории.

        :param product: Экземпляр класса Product для удаления.
        :param ignore_not_found: Если True, не выбрасывает исключение, если продукт не найден.
        """
        if product in self.__products:
            self.__products.remove(product)
            Category.total_products -= 1
        elif not ignore_not_found:
            raise ValueError("Продукт не найден в категории.")

    def update_product_quantity(self, product: Product, new_quantity: int):
        """
        Обновляет количество товара в категории.

        :param product: Экземпляр класса Product.
        :param new_quantity: Новое количество товара.
        """
        if product not in self.__products:
            raise ValueError("Продукт не найден в категории.")
        if not isinstance(new_quantity, int) or new_quantity < 0:
            raise ValueError("Количество товара должно быть неотрицательным целым числом.")
        product.quantity = new_quantity

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
    # Создание двух продуктов
    product_data1 = {
        'name': "Товар A",
        'description': "Описание A",
        'price': 100.0,
        'quantity': 10
    }
    product_data2 = {
        'name': "Товар B",
        'description': "Описание B",
        'price': 200.0,
        'quantity': 2
    }

    product1 = Product.new_product(product_data1)
    product2 = Product.new_product(product_data2)

    # Сложение двух продуктов
    total_cost = product1 + product2
    print(f"Общая стоимость товаров: {total_cost}")  # Вывод: 1400.0

    # Остальной пример использования
    electronics = Category(name="Электроника", description="Категория электронных товаров")
    electronics.add_product(product1)
    electronics.add_product(product2)
    print(electronics)
    print(f"Общее количество категорий: {Category.total_categories}")
    print(f"Общее количество товаров: {Category.total_products}")
    electronics.remove_product(product1, ignore_not_found=True)
    print(electronics)
    print(f"Общее количество категорий: {Category.total_categories}")
    print(f"Общее количество товаров: {Category.total_products}")
    books = Category(name="Книги", description="Категория книг")
    book_data = {
        'name': "Приключения",
        'description': "Книга о приключениях",
        'price': 15.0,
        'quantity': 30
    }
    book1 = Product.new_product(book_data)
    books.add_product(book1)
    print(books)
    print(f"Общее количество категорий: {Category.total_categories}")
    print(f"Общее количество товаров: {Category.total_products}")
    print("Список товаров в категории 'Электроника':")
    print(electronics.products_info)
    print("Список товаров в категории 'Книги':")
    print(books.products_info)
    print(f"Цена продукта {product2.name}: {product2.price}")
    product2.price = 30.0
    print(f"Цена продукта {product2.name} после обновления: {product2.price}")
    try:
        product2.price = -10.0
    except ValueError as e:
        print(f"Ошибка при установке цены: {e}")
    print(f"Цена продукта {product2.name} после попытки некорректного обновления: {product2.price}")
    electronics.update_product_quantity(product2, 100)
    print(f"Новое количество товара {product2.name}: {product2.quantity}")