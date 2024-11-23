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

def test_add_additional(self):
    self.assertEqual(self.calc.add(5, 0), 5)
    self.assertEqual(self.calc.add(0, 0), 0)

def test_subtract_additional(self):
    self.assertEqual(self.calc.subtract(0, 5), -5)
    self.assertEqual(self.calc.subtract(5, 0), 5)

def test_multiply_additional(self):
    self.assertEqual(self.calc.multiply(0, 5), 0)
    self.assertEqual(self.calc.multiply(-1, 5), -5)

def test_divide_additional(self):
    self.assertEqual(self.calc.divide(0, 5), 0) 
    self.assertAlmostEqual(self.calc.divide(1, 9), 0.111111, places=5) 


def test_modulo_additional(self):
    self.assertEqual(self.calc.modulo(100, 7), 2)
    self.assertEqual(self.calc.modulo(5, 5), 0)



