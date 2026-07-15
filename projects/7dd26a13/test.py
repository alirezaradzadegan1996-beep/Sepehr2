from product import Product
from cart import Cart


def test_cart():

    cart = Cart()

    cart.add(
        Product("Phone", 1000)
    )

    assert cart.total() == 1000


if __name__ == "__main__":

    test_cart()

    print("Tests Passed")
