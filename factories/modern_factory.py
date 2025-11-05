from factories.abstract_factory import FurnitureFactory
from products.base import Product

class ModernProduct(Product):
    def describe(self):
        return f"{self.name}: {self.desc} (Modern style)"

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self, spec):
        return ModernProduct(**spec)

    def create_sofa(self, spec):
        return ModernProduct(**spec)

    def create_table(self, spec):
        return ModernProduct(**spec)