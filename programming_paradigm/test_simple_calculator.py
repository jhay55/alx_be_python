import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(15, 3), 18)
        self.assertEqual(self.calc.add(-6, 6), 0)
        self.assertEqual(self.calc.add(-1, -71), -72)
        
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(8,13), -5)
        self.assertEqual(self.calc.subtract(-1,-1), 0)
        self.assertEqual(self.calc.subtract(-1,1), -2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(99, 10), 990)
        self.assertEqual(self.calc.multiply(-12, 12), -144)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-2, -30), 60)
        self.assertEqual(self.calc.multiply(60, 0), 0)

        
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(0, 7), 0)
        self.assertEqual(self.calc.divide(-60, 2), -30)
        self.assertEqual(self.calc.divide(-6, 2), -3)

        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(33, 0)

if __name__ == "__main__":
    unittest.main() 
