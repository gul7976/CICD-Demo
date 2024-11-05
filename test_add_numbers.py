# test_add_numbers.py

import unittest
from add_numbers import add_numbers

class TestAddNumbers(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(add_numbers(5, 7), 12)

    def test_negative_numbers(self):
        self.assertEqual(add_numbers(-3, -6), -9)

    def test_mixed_numbers(self):
        self.assertEqual(add_numbers(10, -5), 5)

    def test_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
