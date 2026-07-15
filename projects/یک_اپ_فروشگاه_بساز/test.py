from product import ProductManager
from database import Database


def run_tests():

    db = Database()

    products = ProductManager(db)


    assert len(products.list_products()) > 0


    print("Ecommerce tests passed")


if __name__ == "__main__":

    run_tests()
