from calculator import add, subtract, multiply, divide


def run_tests():

    assert add(2,3) == 5
    assert subtract(5,2) == 3
    assert multiply(4,3) == 12
    assert divide(10,2) == 5

    print("Calculator tests passed")


if __name__ == "__main__":
    run_tests()
