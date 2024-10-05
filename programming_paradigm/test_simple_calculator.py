import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)        # Positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)       # Negative and positive
        self.assertEqual(self.calc.add(-1, -1), -2)     # Negative numbers
        self.assertEqual(self.calc.add(0, 0), 0)         # Zeros
        self.assertEqual(self.calc.add(100, 250), 350)  # Larger numbers

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)   # Positive result
        self.assertEqual(self.calc.subtract(3, 5), -2)  # Negative result
        self.assertEqual(self.calc.subtract(-1, -1), 0)  # Zero result
        self.assertEqual(self.calc.subtract(0, 5), -5)    # Subtracting positive from zero
        self.assertEqual(self.calc.subtract(10, 0), 10)   # Subtracting zero

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(3, 4), 12)    # Positive numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)    # Negative and positive
        self.assertEqual(self.calc.multiply(0, 5), 0)      # Multiplying by zero
        self.assertEqual(self.calc.multiply(-1, -1), 1)    # Negative numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10)   # Float multiplication

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)      # Normal division
        self.assertEqual(self.calc.divide(5, 0), None)     # Division by zero
        self.assertEqual(self.calc.divide(-10, 2), -5)     # Negative numerator
        self.assertEqual(self.calc.divide(10, -2), -5)     # Negative denominator
        self.assertEqual(self.calc.divide(-10, -2), 5)     # Both negative
        self.assertEqual(self.calc.divide(9, 3), 3)        # Integer result

if __name__ == "__main__":
    unittest.main()
