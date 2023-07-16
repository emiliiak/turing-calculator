import unittest
from emiliiak_calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment before each test case.

        Creates a new Calculator instance to use in the test methods.
        """
        self.calculator = Calculator()

    def test_addition(self):
        """
        Test the addition functionality of the Calculator class.

        Verifies that the add() method correctly adds a number to the calculator's memory.
        """
        self.assertEqual(self.calculator.add(2), 2)

    def test_subtraction(self):
        """
        Test the subtraction functionality of the Calculator class.

        Verifies that the subtract() method correctly subtracts a number from the calculator's memory.
        """
        self.assertEqual(self.calculator.subtract(2), -2)

    def test_multiplication(self):
        """
        Test the multiplication functionality of the Calculator class.

        Verifies that the multiply() method correctly multiplies the calculator's memory by a number.
        """
        self.assertEqual(self.calculator.multiply(2), 0)

    def test_division(self):
        """
        Test the division functionality of the Calculator class.

        Verifies that the divide() method correctly divides the calculator's memory by a number.
        """
        self.assertEqual(self.calculator.divide(2), 0)

    def test_root(self):
        """
        Test the root functionality of the Calculator class.

        Verifies that the root() method correctly calculates the n-th root of the calculator's memory.
        """
        self.assertEqual(self.calculator.root(2), 0.0)

    def test_reset(self):
        """
        Test the reset functionality of the Calculator class.

        Verifies that the reset() method correctly resets the calculator's memory to 0.
        """
        self.assertEqual(self.calculator.reset(), 0)

if __name__ == '__main__':
    unittest.main()
