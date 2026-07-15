class InputValidator:

    @staticmethod
    def validate_number(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be numeric")

        return value

    @classmethod
    def validate_pair(cls, a, b):
        cls.validate_number(a)
        cls.validate_number(b)

        return a, b
