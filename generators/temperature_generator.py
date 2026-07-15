import os


class TemperatureGenerator:


    def generate(self, path, goal):

        os.makedirs(
            path,
            exist_ok=True
        )


        main_code = """
from temperature import celsius_to_fahrenheit, celsius_to_kelvin


def main():

    print("Temperature Converter")

    c = 25

    print("Celsius:", c)

    print(
        "Fahrenheit:",
        celsius_to_fahrenheit(c)
    )

    print(
        "Kelvin:",
        celsius_to_kelvin(c)
    )


if __name__ == "__main__":
    main()
"""


        temperature_code = """
def celsius_to_fahrenheit(c):

    return (c * 9/5) + 32



def celsius_to_kelvin(c):

    return c + 273.15
"""


        test_code = """
from temperature import celsius_to_fahrenheit, celsius_to_kelvin


def test():

    assert celsius_to_fahrenheit(0) == 32

    assert celsius_to_kelvin(0) == 273.15


    print("Temperature tests passed")


if __name__ == "__main__":

    test()
"""


        self.write(
            path,
            "main.py",
            main_code
        )

        self.write(
            path,
            "temperature.py",
            temperature_code
        )

        self.write(
            path,
            "test.py",
            test_code
        )


        return True



    def write(self, path, name, content):

        with open(
            os.path.join(path,name),
            "w",
            encoding="utf-8"
        ) as f:

            f.write(content)
