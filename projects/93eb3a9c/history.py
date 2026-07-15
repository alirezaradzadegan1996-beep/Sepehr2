class CalculationHistory:

    def __init__(self):
        self.items = []

    def add(self, expression, result):
        self.items.append({
            "expression": expression,
            "result": result
        })

    def get_all(self):
        return list(self.items)

    def clear(self):
        self.items.clear()
