import unittest

from src.main import Product, Category

class TestProduct(unittest.TestCase):
    def setUp(self):
        # Данные для создания продукта
        self.product_data = {
            'name': "Товар A",
            'description': "Описание A",
            'price': 100.0,
            'quantity': 10
        }
        self.product = Product.new_product(self.product_data)

    def test_create_product(self):
        """Проверка создания продукта с корректными данными"""
        self.assertEqual(self.product.name, "Товар A")
        self.assertEqual(self.product.description, "Описание A")
        self.assertEqual(self.product.price, 100.0)
        self.assertEqual(self.product.quantity, 10)

    def test_create_product_invalid_data(self):
        """Проверка обработки некорректных данных при создании продукта"""
        invalid_data = {
            'name': "Товар B",
            'description': "Описание B",
            'price': -50.0,  # Отрицательная цена
            'quantity': 5
        }
        with self.assertRaises(ValueError):
            Product.new_product(invalid_data)

    def test_price_setter(self):
        """Проверка работы сеттера для цены"""
        self.product.price = 150.0
        self.assertEqual(self.product.price, 150.0)
        with self.assertRaises(ValueError):
            self.product.price = -10.0

    def test_add_method(self):
        """Проверка метода сложения продуктов"""
        product2 = Product.new_product({
            'name': "Товар B",
            'description': "Описание B",
            'price': 200.0,
            'quantity': 2
        })
        total_cost = self.product + product2
        self.assertEqual(total_cost, 100.0 * 10 + 200.0 * 2)

    def test_str_method(self):
        expected_str = "Товар A, 100.0 руб. Остаток: 10 шт."
        self.assertEqual(str(self.product), expected_str)


class TestCategory(unittest.TestCase):
    def setUp(self):
        # Создание категории и продукта для тестов
        self.category = Category(name="Электроника", description="Категория электронных товаров")
        self.product_data = {
            'name': "Товар A",
            'description': "Описание A",
            'price': 100.0,
            'quantity': 10
        }
        self.product = Product.new_product(self.product_data)

    def tearDown(self):
        # Сброс счетчиков
        Category.total_categories = 0
        Category.total_products = 0

    def test_create_category(self):
        """Проверка создания категории"""
        self.assertEqual(self.category.name, "Электроника")
        self.assertEqual(self.category.description, "Категория электронных товаров")
        self.assertEqual(Category.total_categories, 1)

    def test_add_product(self):
        """Проверка добавления продукта в категорию"""
        self.category.add_product(self.product)
        self.assertEqual(len(self.category._Category__products), 1)
        self.assertEqual(Category.total_products, 1)

    def test_remove_product(self):
        """Проверка удаления продукта из категории"""
        self.category.add_product(self.product)
        self.category.remove_product(self.product)
        self.assertEqual(len(self.category._Category__products), 0)
        self.assertEqual(Category.total_products, 0)

    def test_update_product_quantity(self):
        """Проверка обновления количества продукта"""
        self.category.add_product(self.product)
        self.category.update_product_quantity(self.product, 20)
        self.assertEqual(self.product.quantity, 20)

    def test_products_info(self):
        """Проверка свойства products_info"""
        self.category.add_product(self.product)
        expected_info = "Товар A, 100.0 руб. Остаток: 10 шт."
        self.assertEqual(self.category.products_info, expected_info)

    def test_str_method(self):
        self.category.add_product(self.product)
        expected_str = "Электроника, количество продуктов: 10 шт."
        self.assertEqual(str(self.category), expected_str)

    def test_str_method_no_products(self):
        expected_str = "Электроника, количество продуктов: 0 шт."
        self.assertEqual(str(self.category), expected_str)

    def test_str_method_multiple_products(self):
        product2 = Product.new_product({
            'name': "Товар B",
            'description': "Описание B",
            'price': 200.0,
            'quantity': 5
        })
        self.category.add_product(self.product)
        self.category.add_product(product2)
        expected_str = "Электроника, количество продуктов: 15 шт."
        self.assertEqual(str(self.category), expected_str)


if __name__ == '__main__':
    unittest.main()