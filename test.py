import unittest

class TestFigure (unittest.TestCase):

    def test_rect (self):
        self.assertEqual (str(Rect ("синего", 3, 2)), "Прямоугольник синего цвета, шириной 3 и высотой 2, площадью 6.", "Неверный формат вывода данных о прямоугольнике")

    def test_square (self):
        self.assertEqual (str(Square ("красного", 5)), "Квадратик красного цвета, со стороной 5, площадью 25.", "Неверный формат вывода данных о квадрате")

    def test_circle (self):
        self.assertEqual (str(Circle ("зелёного", 5)), "Круг зелёного цвета, радиусом 5, площадью 78.53981633974483.", "Неверный формат вывода данных о круге")


    def test_circle_must_be_fallen (self):
        self.assertEqual (str(Circle ("зелёного", 1)), "Круг зелёного цвета, радиусом 5, площадью 78.53981633974483.", "Неверный формат вывода данных о круге")
