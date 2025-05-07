import unittest
from simple.server import add

class TestMathServer(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(2, 3), 5)

    def test_addition_with_negative_numbers(self):
        self.assertEqual(add(-1, -4), -5)

    def test_addition_with_zero(self):
        self.assertEqual(add(0, 5), 5)

if __name__ == "__main__":
    unittest.main()