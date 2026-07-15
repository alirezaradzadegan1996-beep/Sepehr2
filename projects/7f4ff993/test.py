from product import Product

def test_product():

    p = Product("Book", 20)

    assert p.price == 20


if __name__ == "__main__":
    test_product()
    print("All tests passed.")
