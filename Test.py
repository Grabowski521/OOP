import unittest
from main import *
class TestProduct(unittest.TestCase):
    def test_new_product(self):
        product_data = {
            'name': "Ноутбук",
            'description': "Профессиональный ноутбук",
            'price': 1200.0,
            'quantity': 10
        }
        product = Product.new_product(product_data)
        self.assertEqual(product.name, "Ноутбук")
        self.assertEqual(product.description, "Профессиональный ноутбук")
        self.assertEqual(product.price, 1200.0)
        self.assertEqual(product.quantity, 10)

    def test_price_setter(self):
        product = Product(name="Мышь", description="Оптическая мышь", price=25.0, quantity=50)
        product.price = 30.0
        self.assertEqual(product.price, 30.0)
        with self.assertRaises(ValueError) as context:
            product.price = -10.0
        self.assertEqual(str(context.exception), "Цена не должна быть нулевая или отрицательная")

    def test_price_getter(self):
        product = Product(name="Мышь", description="Оптическая мышь", price=25.0, quantity=50)
        self.assertEqual(product.price, 25.0)


class TestCategory(unittest.TestCase):
    def setUp(self):
        Category.total_categories = 0
        Category.total_products = 0

    def test_add_product(self):
        product1 = Product(name="Ноутбук", description="Профессиональный ноутбук", price=1200.0, quantity=10)
        product2 = Product(name="Мышь", description="Оптическая мышь", price=25.0, quantity=50)
        electronics = Category(name="Электроника", description="Категория электронных товаров")
        electronics.add_product(product1)
        electronics.add_product(product2)
        self.assertEqual(len(electronics.__dict__['_Category__products']), 2)
        self.assertEqual(Category.total_categories, 1)
        self.assertEqual(Category.total_products, 2)

    def test_remove_product(self):
        product1 = Product(name="Ноутбук", description="Профессиональный ноутбук", price=1200.0, quantity=10)
        product2 = Product(name="Мышь", description="Оптическая мышь", price=25.0, quantity=50)
        electronics = Category(name="Электроника", description="Категория электронных товаров")
        electronics.add_product(product1)
        electronics.add_product(product2)
        electronics.remove_product(product1)
        self.assertEqual(len(electronics.__dict__['_Category__products']), 1)
        self.assertEqual(Category.total_categories, 1)
        self.assertEqual(Category.total_products, 1)

    def test_products_info(self):
        product1 = Product(name="Ноутбук", description="Профессиональный ноутбук", price=1200.0, quantity=10)
        product2 = Product(name="Мышь", description="Оптическая мышь", price=25.0, quantity=50)
        electronics = Category(name="Электроника", description="Категория электронных товаров")
        electronics.add_product(product1)
        electronics.add_product(product2)
        expected_info = ("Ноутбук, 1200.0 руб. Остаток: 10 шт.\n"
                         "Мышь, 25.0 руб. Остаток: 50 шт.")
        self.assertEqual(electronics.products_info, expected_info)

    def test_no_products_info(self):
        electronics = Category(name="Электроника", description="Категория электронных товаров")
        self.assertEqual(electronics.products_info, "В категории нет товаров.")
