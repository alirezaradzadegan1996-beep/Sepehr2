from calculator import Calculator
from history import CalculationHistory


def main():

    calc = Calculator()
    history = CalculationHistory()

    result = calc.add(5, 3)

    history.add(
        "5 + 3",
        result
    )

    print(result)
    print(history.get_all())


if __name__ == "__main__":
    main()
