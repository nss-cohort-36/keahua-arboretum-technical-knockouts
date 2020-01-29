from animals import Animal
from interfaces import Identifiable
from interfaces.animal import IAquaticPrey

class Spider(Animal, Identifiable, IAquaticPrey):
    def __init__(self):
        Animal.__init__(self)
        Identifiable.__init__(self)
        self.food = ["Flies", "Ants", "Moths"]
        self.name = "Hawaiian Happy-Face Spider"