import unittest
from rectangle import area, perimeter


class RectangleTest(unittest.TestCase):
    def test_zero_area(self):
        self.assertEqual(area(0, 0), 0)

    def test_positive_area(self):
        self.assertEqual(area(7, 3), 21)

    def test_negative_area(self):
        self.assertEqual(area(-7, 3), 21)

    def test_zero_perimeter(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_positive_perimeter(self):
        self.assertEqual(perimeter(8, 5), 26)

    def test_negative_perimeter(self):
        self.assertEqual(perimeter(-8, 5), 26)


if __name__ == "__main__":
    unittest.main()
