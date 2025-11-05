from factories.abstract_factory import FurnitureFactory
from products.base import Product

class VictorianProduct(Product):
    def describe(self):
        return f"{self.name}: {self.desc} (Victorian style)"

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self, spec):
        return VictorianProduct(**spec)

    def create_sofa(self, spec):
        return VictorianProduct(**spec)

    def create_table(self, spec):
        return VictorianProduct(**spec)