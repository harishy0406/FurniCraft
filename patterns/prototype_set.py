import copy

class FurnitureSet:
    def __init__(self, style, chair, sofa, table):
        self.style = style
        self.chair = chair
        self.sofa = sofa
        self.table = table

    def clone(self):
        return copy.deepcopy(self)

    def to_list(self):
        return [self.chair, self.sofa, self.table]