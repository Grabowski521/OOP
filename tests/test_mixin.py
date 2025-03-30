import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.main import *

class TestInitLoggerMixin(unittest.TestCase):
    def test_product_creation(self):
        """Тест создания объекта класса Product"""
        with StringIO() as buf, redirect_stdout(buf):
            product = Product('Тестовый продукт', 'Описание', 1000, 10)
            output = buf.getvalue().strip()
            expected = "Создан объект класса Product с параметрами:('Тестовый продукт', 'Описание', 1000, 10), {}"
            self.assertEqual(output, expected)

    def test_smartphone_creation(self):
        """Тест создания объекта класса Smartphone"""
        with StringIO() as buf, redirect_stdout(buf):
            smartphone = Smartphone('Тестовый смартфон', 'Описание', 5000, 5, 'Высокая', 'МодельY', 64, 'Синий')
            output = buf.getvalue().strip()
            expected = "Создан объект класса Smartphone с параметрами:('Тестовый смартфон', 'Описание', 5000, 5, 'Высокая', 'МодельY', 64, 'Синий'), {}"
            self.assertEqual(output, expected)

    def test_lawngrass_creation(self):
        """Тест создания объекта класса LawnGrass"""
        with StringIO() as buf, redirect_stdout(buf):
            lawn_grass = LawnGrass('Тестовая трава', 'Описание', 300, 15, 'Франция', '7 дней', 'Зелёный')
            output = buf.getvalue().strip()
            expected = "Создан объект класса LawnGrass с параметрами:('Тестовая трава', 'Описание', 300, 15, 'Франция', '7 дней', 'Зелёный'), {}"
            self.assertEqual(output, expected)
