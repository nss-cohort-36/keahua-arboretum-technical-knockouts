from animals import Animal
from interfaces import Identifiable

class Ulae(Animal, Identifiable):
    def __init__(self):
        Animal.__init__(self)
        Identifiable.__init__(self)
        self.food = ["Trout", "Mackarel", "Salmon", "Sardine"]
        self.name = "'Ulae" 