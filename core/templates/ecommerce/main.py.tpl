from product import ProductManager
from cart import Cart
from database import Database
from user import UserManager


def main():

    print("🛒 Ecommerce App")

    db = Database()

    products = ProductManager(db)

    users = UserManager(db)

    cart = Cart()


    print("\n📦 Products:")

    for p in products.list_products():
        print("-", p)


    cart.add("Laptop")
    cart.add("Phone")


    print("\n🛒 Cart:")
    print(cart.items)


    print("\n👤 Users:")
    print(users.list_users())


    print("\n✅ Store running successfully")


if __name__ == "__main__":
    main()
