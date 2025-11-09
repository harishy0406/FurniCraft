# Modified Cart logic
class ShoppingCart:
    _instance = None

    def __init__(self):
        self.items = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ShoppingCart()
        return cls._instance

    def add(self, product):
        self.items.append(product)

    def clear(self):
        self.items = []

    def total(self):
        return sum(item.get('price', 0) for item in self.items)

    def items_count(self):
        return len(self.items)