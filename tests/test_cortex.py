from core.cortex.cortex import cortex


def hello(name):
    return f"سلام {name}"


def main():
    cortex.register("hello", hello)

    result = cortex.execute("hello", "علیرضا")

    print("Result:", result)
    print("Status:", cortex.status())


if __name__ == "__main__":
    main()
