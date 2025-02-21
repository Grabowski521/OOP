import unittest
from main import *

class TestProduct(unittest.TestCase):
    def test_product_initialization(self):
        product = Product(name="Ноутбук", description="Профессиональный ноутбук", price=1200.0, quantity=10)
        self.assertEqual(product.name, "Ноутбук")
        self.assertEqual(product.description, "Профессиональный ноутбук")
        self.assertEqual(product.price, 1200.0)
        self.assertEqual(product.quantity, 10)

    def test_product_str_representation(self):
        product = Product(name="Мышь", description="Оптическая мышь", price=25.0, quantity=50)
        expected_str = "Product(name=Мышь, description=Оптическая мышь, price=25.0, quantity=50)"
        self.assertEqual(str(product), expected_str)


class TestCategory(unittest.TestCase):
    def setUp(self):
        Category.total_categories = 0
        Category.total_products = 0

    def test_category_initialization(self):
        category = Category(name="Электроника", description="Категория электронных товаров")
        self.assertEqual(category.name, "Электроника")
        self.assertEqual(category.description, "Категория электронных товаров")
        self.assertEqual(category.products, [])
        self.assertEqual(Category.total_categories, 1)

    def test_category_str_representation(self):
        category = Category(name="Книги", description="Категория книг")
        expected_str = "Category(name=Книги, description=Категория книг, products=[])"
        self.assertEqual(str(category), expected_str)

    def test_add_product(self):
        category = Category(name="Электроника", description="Категория электронных товаров")
        product1 = Product(name="Ноутбук", description="Профессиональный ноутбук", price=1200.0, quantity=10)
        product2 = Product(name="Мышь", description="Оптическая мышь", price=25.0, quantity=50)

        category.add_product(product1)
        self.assertEqual(len(category.products), 1)
        self.assertIn(product1, category.products)
        self.assertEqual(Category.total_products, 1)

        category.add_product(product2)
        self.assertEqual(len(category.products), 2)
        self.assertIn(product2, category.products)
        self.assertEqual(Category.total_products, 2)

    def test_remove_product(self):
        category = Category(name="Электроника", description="Категория электронных товаров")
        product1 = Product(name="Ноутбук", description="Профессиональный ноутбук", price=1200.0, quantity=10)
        product2 = Product(name="Мышь", description="Оптическая мышь", price=25.0, quantity=50)

        category.add_product(product1)
        category.add_product(product2)
        self.assertEqual(len(category.products), 2)
        self.assertIn(product1, category.products)
        self.assertIn(product2, category.products)
        self.assertEqual(Category.total_products, 2)

        category.remove_product(product1)
        self.assertEqual(len(category.products), 1)
        self.assertNotIn(product1, category.products)
        self.assertIn(product2, category.products)
        self.assertEqual(Category.total_products, 1)

        with self.assertRaises(ValueError):
            category.remove_product(product1)  # Удаление несуществующего продукта

    def test_total_categories(self):
        category1 = Category(name="Электроника", description="Категория электронных товаров")
        category2 = Category(name="Книги", description="Категория книг")
        self.assertEqual(Category.total_categories, 2)

    def test_total_products(self):
        category1 = Category(name="Электроника", description="Категория электронных товаров")
        product1 = Product(name="Ноутбук", description="Профессиональный ноутбук", price=1200.0, quantity=10)
        product2 = Product(name="Мышь", description="Оптическая мышь", price=25.0, quantity=50)

        category1.add_product(product1)
        category1.add_product(product2)
        self.assertEqual(Category.total_products, 2)

        category2 = Category(name="Книги", description="Категория книг")
        product3 = Product(name="Приключения", description="Книга о приключениях", price=15.0, quantity=30)
        category2.add_product(product3)
        self.assertEqual(Category.total_products, 3)


