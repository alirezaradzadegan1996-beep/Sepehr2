class ProductManager:

    def __init__(self, database):
        self.database = database

        self.products = [
            "Laptop",
            "Phone",
            "Tablet"
        ]


    def list_products(self):

        return self.products
