from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, id, name, price, desc, image=None):
        self.id = id
        self.name = name
        self.price = price
        self.desc = desc
        self.image = image or ""

    @abstractmethod
    def describe(self):
        pass

    def get_price(self):
        return self.price

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price, "desc": self.desc, "image": self.image}