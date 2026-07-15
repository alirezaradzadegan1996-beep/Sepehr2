class Cart:

    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def remove(self, product):
        if product in self.products:
            self.products.remove(product)

    def total(self):
        return sum(p.price for p in self.products)

    def show(self):
        print("Products:")
        for p in self.products:
            print("-", p)
        print("Total:", self.total())
