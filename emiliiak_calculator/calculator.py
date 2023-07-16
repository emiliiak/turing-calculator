"""
Calculator Class
----------------

The Calculator class is a part of the Calculator Package and provides basic arithmetic operations such as addition, subtraction, multiplication, division, and taking the n-th root of a number.

Usage:
- Create an instance of the Calculator class.
- Use the available methods to perform arithmetic operations.
"""

class Calculator:
    def __init__(self) -> None:
        """
        Initialisation of a new Calculator object.
        The calculator's memory is set to 0 by initialisation.
        """
        self.memory: float = 0
        
    def add(self, num: float) -> float:
        """
        Addition action.

        Args:
            num (float): The number to be added.

        Returns:
            float: The updated value in the calculator's memory.
        """
        self.memory += num
        return self.memory

    def subtract(self, num: float) -> float:
        """
        Subtraction action.

        Args:
            num (float): The number to be subtracted.

        Returns:
            float: The updated value in the calculator's memory.
        """
        self.memory -= num
        return self.memory

    def multiply(self, num: float) -> float:
        """
        Multiplication action.

        Args:
            num (float): The number to multiply by.

        Returns:
            float: The updated value in the calculator's memory.
        """
        self.memory *= num
        return self.memory

    def divide(self, num: float) -> float:
        """
        Division action.

        Args:
            num (float): The number to divide by.

        Returns:
            float: The updated value in the calculator's memory.

        Raises:
            ZeroDivisionError: If the divisor is zero.
        """
        if num != 0:
            self.memory /= num
        return self.memory

    def root(self, n: float) -> float:
        """
        Take (n) root of a number.

        Args:
            n (float): The root value.

        Returns:
            float: The updated value in the calculator's memory.
        """
        self.memory **= (1 / n)
        return self.memory
    
    def reset(self) -> float:
        """
        Reset the calculator's memory to 0.

        Returns:
            float: The updated value in the calculator's memory.
        """
        self.memory = 0
        return self.memory
