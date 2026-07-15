class Cart:

    def __init__(self):
        self.items = []


    def add(self, product):
        self.items.append(product)


    def total(self):
        return sum(
            item.price
            for item in self.items
        )


    def show(self):

        print("Products:")

        for item in self.items:
            print("-", item)

        print(
            "Total:",
            self.total()
        )
