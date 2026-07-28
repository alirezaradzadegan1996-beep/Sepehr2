from core.kernel.bootstrap import *
from core.cortex.cortex import cortex

def main():

    cortex.boot()

    while True:

        text = input("\n👤 ")

        if text in [
            "exit",
            "quit",
            "خروج"
        ]:
            break

        print(cortex.think(text))

if __name__ == "__main__":
    main()
