from animals import Animal
from interfaces import Identifiable

class Pueo(Animal, Identifiable):
    def __init__(self):
        Animal.__init__(self)
        Identifiable.__init__(self)
        self.food = ["Mouse", "Rat", "Hamster"] 