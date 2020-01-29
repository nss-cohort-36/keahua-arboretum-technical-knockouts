from animals import Animal
from interfaces import Identifiable
from interfaces.animal import IClimbing

class Gecko(Animal, Identifiable, IClimbing):
    def __init__(self):
        Animal.__init__(self)
        Identifiable.__init__(self)
        self.food = ["Flies", "Ants", "Moths"] 
        self.name = "Gold Dust Day Gecko"