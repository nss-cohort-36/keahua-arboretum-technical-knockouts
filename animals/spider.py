from animals import Animal
from interfaces import Identifiable

class Spider(Animal, Identifiable):
    def __init__(self):
        Animal.__init__(self)
        Identifiable.__init__(self)
        self.food = ["Flies", "Ants", "Moths"]
        self.name = "Hawaiian Happy-Face Spider"