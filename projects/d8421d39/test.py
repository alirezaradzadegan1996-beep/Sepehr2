from calculator import Calculator


def test_add():

    calc = Calculator()

    assert calc.add(
        2,
        3
    ) == 5


if __name__ == "__main__":

    test_add()

    print(
        "✅ calculator test passed"
    )
