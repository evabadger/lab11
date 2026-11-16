import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 5), 3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(3, 7), -4)
        self.assertEqual(sub(5, 5), 0)

    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(5, 25), 5)
        self.assertEqual(divide(-2, 10), -5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(10, 100), 2)
        self.assertAlmostEqual(log(3, 27), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 8)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self):
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(0), 0)
        self.assertAlmostEqual(square_root(2), 1.41421356237)

        with self.assertRaises(ValueError):
            square_root(-4)

if __name__ == "__main__":
    unittest.main()
