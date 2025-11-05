class PricingStrategy:
    def calculate(self, items):
        raise NotImplementedError

class NoDiscount(PricingStrategy):
    def calculate(self, items):
        return sum(i.get('price', 0) for i in items)

class FestiveDiscount(PricingStrategy):
    def __init__(self, percent=10):
        self.percent = percent

    def calculate(self, items):
        subtotal = sum(i.get('price', 0) for i in items)
        return subtotal * (1 - self.percent/100.0)

class FlatCoupon(PricingStrategy):
    def __init__(self, amount=20):
        self.amount = amount

    def calculate(self, items):
        subtotal = sum(i.get('price', 0) for i in items)
        return max(0, subtotal - self.amount)