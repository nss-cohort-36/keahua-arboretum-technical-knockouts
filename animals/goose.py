from animals import Animal
from interfaces import Identifiable
from interfaces.animal import IWalking

class Goose(Animal, Identifiable, IWalking):
    def __init__(self):
        Animal.__init__(self)
        Identifiable.__init__(self)
        self.food = ["Silversword", "Blue Jade Vine", "Mountain Apple Tree"] 
        self.name = "Nene Goose"