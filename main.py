class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (f"Product(name={self.name}, description={self.description}, "
                f"price={self.price}, quantity={self.quantity})")


class Category:
    total_categories = 0  # Счетчик общего количества категорий
    total_products = 0    # Счетчик общего количества товаров

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products = []  # Список для хранения продуктов

        # Увеличиваем счетчик категорий при создании новой категории
        Category.total_categories += 1

    def add_product(self, product: Product):
        """Добавляет продукт в категорию."""
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только экземпляры класса Product.")
        self.products.append(product)
        # Увеличиваем счетчик товаров при добавлении нового продукта
        Category.total_products += 1

    def remove_product(self, product: Product):
        """Удаляет продукт из категории."""
        if product in self.products:
            self.products.remove(product)
            # Уменьшаем счетчик товаров при удалении продукта
            Category.total_products -= 1
        else:
            raise ValueError("Продукт не найден в категории.")

    def __str__(self):
        return (f"Category(name={self.name}, description={self.description}, "
                f"products={self.products})")


# Пример использования
if __name__ == "__main__":
    # Создаются два продукта
    product1 = Product(name="Ноутбук", description="Профессиональный ноутбук", price=1200.0, quantity=10)
    product2 = Product(name="Мышь", description="Оптическая мышь", price=25.0, quantity=50)

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
    book1 = Product(name="Приключения", description="Книга о приключениях", price=15.0, quantity=30)
    books.add_product(book1)

    # Вывод информации о новой категории
    print(books)

    # Вывод общего количества категорий и товаров после добавления новой категории и продукта
    print(f"Общее количество категорий: {Category.total_categories}")
    print(f"Общее количество товаров: {Category.total_products}")