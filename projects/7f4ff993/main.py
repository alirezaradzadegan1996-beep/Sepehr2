from product import Product
from cart import Cart

def main():

    cart = Cart()

    p = Product("Phone", 1000)

    cart.add(p)

    cart.show()


if __name__ == "__main__":
    main()
