import unittest

from src.main import Product, Smartphone, LawnGrass

class TestProductAddition(unittest.TestCase):
    def test_add_same_class(self):
        """Проверка сложения двух объектов одного класса (Smartphone)."""
        smartphone1 = Smartphone(
            name="Phone1",
            description="Desc1",
            price=100.0,
            quantity=2,
            efficiency="High",
            model="Model1",
            memory=128,
            color="Black"
        )
        smartphone2 = Smartphone(
            name="Phone2",
            description="Desc2",
            price=150.0,
            quantity=3,
            efficiency="Medium",
            model="Model2",
            memory=64,
            color="White"
        )
        total = smartphone1 + smartphone2
        expected_total = (100.0 * 2) + (150.0 * 3)  # 200 + 450 = 650
        self.assertEqual(total, expected_total)

    def test_add_different_class(self):
        """Проверка ошибки при сложении объектов разных классов (Smartphone и LawnGrass)."""
        smartphone = Smartphone(
            name="Phone",
            description="Desc",
            price=100.0,
            quantity=1,
            efficiency="High",
            model="Model",
            memory=128,
            color="Black"
        )
        lawn_grass = LawnGrass(
            name="Grass",
            description="Green grass",
            price=20.0,
            quantity=10,
            country="USA",
            germination_period="7 days",
            color="Green"
        )
        with self.assertRaises(TypeError) as context:
            total = smartphone + lawn_grass
        self.assertEqual(str(context.exception), "Можно складывать только объекты одного и того же класса.")

    def test_add_non_product(self):
        """Проверка ошибки при сложении объекта Product с не-продуктом."""
        product = Product(
            name="Generic Product",
            description="Desc",
            price=50.0,
            quantity=5
        )
        non_product = "Я не продукт"
        with self.assertRaises(TypeError) as context:
            total = product + non_product
        self.assertEqual(str(context.exception), "Можно складывать только объекты класса Product.")

if __name__ == '__main__':
    unittest.main()