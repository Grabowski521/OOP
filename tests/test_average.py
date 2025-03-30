import unittest
from abc import ABC, abstractmethod
from src.main import *

class TestNewFunctionality(unittest.TestCase):

    def test_product_zero_quantity(self):
        # Тест на создание продукта с нулевым количеством
        with self.assertRaises(ValueError) as context:
            Product("Тестовый продукт", "Описание", 100, 0)
        self.assertEqual(str(context.exception), "Товар с нулевым количеством не может быть добавлен")

    def test_product_valid_quantity(self):
        # Тест на создание продукта с корректным количеством
        product = Product("Тестовый продукт", "Описание", 100, 5)
        self.assertEqual(product.quantity, 5)
        self.assertEqual(product.name, "Тестовый продукт")
        self.assertEqual(product.price, 100)

    def test_category_average_price_empty(self):
        # Тест на среднюю цену в пустой категории
        category = Category("Пустая категория", "Описание")
        self.assertEqual(category.average_price(), 0)

    def test_category_average_price_with_products(self):
        # Тест на среднюю цену с товарами
        category = Category("Тестовая категория", "Описание")
        product1 = Product("Продукт1", "Описание1", 1000, 10)
        product2 = Product("Продукт2", "Описание2", 2000, 5)
        category.add_product(product1)
        category.add_product(product2)
        expected_average = (1000 + 2000) / 2  # 1500
        self.assertEqual(category.average_price(), expected_average)

