import unittest

from app.calculator import multiply_values, sum_values


class CalculatorTests(unittest.TestCase):
    def test_sum_values(self):
        self.assertEqual(sum_values(2, 3), 5)

    def test_multiply_values(self):
        self.assertEqual(multiply_values(2, 3), 6)


if __name__ == "__main__":
    unittest.main()
