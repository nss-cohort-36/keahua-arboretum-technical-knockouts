from animals import Animal
from interfaces import Identifiable

class Goose(Animal, Identifiable):
    def __init__(self):
        Animal.__init__(self)
        Identifiable.__init__(self)
        self.food = ["Silversword", "Blue Jade Vine", "Mountain Apple Tree"] 