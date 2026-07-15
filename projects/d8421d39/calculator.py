from validator import InputValidator
from errors import DivisionByZeroError


class Calculator:

    def add(self, a, b):
        InputValidator.validate_pair(a, b)
        return a + b

    def subtract(self, a, b):
        InputValidator.validate_pair(a, b)
        return a - b

    def multiply(self, a, b):
        InputValidator.validate_pair(a, b)
        return a * b

    def divide(self, a, b):
        InputValidator.validate_pair(a, b)

        if b == 0:
            raise DivisionByZeroError(
                "division by zero"
            )

        return a / b
