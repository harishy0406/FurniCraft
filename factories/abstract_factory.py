from abc import ABC, abstractmethod

class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self, spec):
        pass

    @abstractmethod
    def create_sofa(self, spec):
        pass

    @abstractmethod
    def create_table(self, spec):
        pass