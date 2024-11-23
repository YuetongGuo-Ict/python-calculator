import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()

def test_add(self):
    self.assertEqual(add(3, 5), 8)
    self.assertEqual(add(-3, 2), -1)

def test_subtract(self):
    self.assertEqual(subtract(7, 4), 3)
    self.assertEqual(subtract(0, 7), -7)

def test_multiply(self):
    self.assertEqual(multiply(9, 12), 108)
    self.assertEqual(multiply(-12, 5), -60)

def test_divide(self):
    self.assertEqual(divide(10, 2), 5)
    self.assertRaises(ZeroDivisionError, divide, 5, 0)

def test_modulo(self):
    self.assertEqual(modulo(10, 3), 1)
    self.assertRaises(ZeroDivisionError, modulo, 5, 0)