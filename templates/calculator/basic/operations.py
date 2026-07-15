from errors import DivisionByZeroError


class OperationRegistry:

    def __init__(self):
        self.operations = {}

    def register(self, name, operation):
        self.operations[name] = operation

    def execute(self, name, a, b):
        if name not in self.operations:
            raise KeyError(
                f"Unknown operation: {name}"
            )

        return self.operations[name](a, b)


def divide(a, b):
    if b == 0:
        raise DivisionByZeroError(
            "Division by zero is not allowed"
        )

    return a / b
