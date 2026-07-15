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
