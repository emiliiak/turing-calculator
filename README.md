Calculator Package
=================

The Calculator Package is a Python package that provides a Calculator class capable of performing basic arithmetic operations.

Features
--------

The Calculator class supports the following arithmetic operations:

- Addition
- Subtraction
- Multiplication
- Division
- Taking the n-th root of a number

The Calculator performs actions with a value inside its memory, manipulating the memory starting from 0 until it is reset.

Installation
------------

You can install the Calculator Package using pip. Open a terminal or command prompt and run the following command:

::

    pip install ekarpiuk-calculator

Usage
-----

To use the Calculator Package in your Python program, follow these steps:

1. Import the `Calculator` class from the package:

    .. code-block:: python

        from emiliiak_calculator.calculator import Calculator

2. Create an instance of the `Calculator` class:

    .. code-block:: python

        calculator = Calculator()

3. Perform arithmetic operations using the available methods:

   - Addition:

     .. code-block:: python

        result = calculator.add(2)  # Add 2 to the calculator's memory

   - Subtraction:

     .. code-block:: python

        result = calculator.subtract(1)  # Subtract 1 from the calculator's memory

   - Multiplication:

     .. code-block:: python

        result = calculator.multiply(3)  # Multiply the calculator's memory by 3

   - Division:

     .. code-block:: python

        result = calculator.divide(2)  # Divide the calculator's memory by 2

   - Root:

     .. code-block:: python

        result = calculator.root(2)  # Calculate the square root of the calculator's memory

   - Reset:

     .. code-block:: python

        result = calculator.reset()  # Reset the calculator's memory to 0

   Note: The methods return the updated value in the calculator's memory.

Example
-------

Here's an example that demonstrates the usage of the Calculator Package:

.. code-block:: python

    from calculator.calculator import Calculator

    calculator = Calculator()
    result = calculator.add(2)
    print(result)  # Output: 2

    result = calculator.multiply(3)
    print(result)  # Output: 6

    result = calculator.divide(2)
    print(result)  # Output: 3.0

    result = calculator.root(2)
    print(result)  # Output: 1.7320508075688772

    result = calculator.reset()
    print(result)  # Output: 0

------------------------------------------------------------------------------------------

Feel free to customize the instructions and examples to suit your specific package implementation and requirements.