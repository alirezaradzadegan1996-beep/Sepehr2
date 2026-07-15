from temperature import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin
)


def run_tests():

    assert celsius_to_fahrenheit(0) == 32

    assert fahrenheit_to_celsius(32) == 0

    assert celsius_to_kelvin(0) == 273.15


    print("Temperature tests passed")


if __name__ == "__main__":
    run_tests()
