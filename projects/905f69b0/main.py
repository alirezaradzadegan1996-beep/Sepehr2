"""
Project : 905f69b0
Type    : ecommerce
"""

from product import Product
from cart import Cart


def main():

    cart = Cart()

    cart.add(Product("Phone", 1000))

    cart.show()


if __name__ == "__main__":
    main()
