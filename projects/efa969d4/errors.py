class CalculatorError(Exception):
    pass


class DivisionByZeroError(CalculatorError):
    pass


class InvalidOperationError(CalculatorError):
    pass
