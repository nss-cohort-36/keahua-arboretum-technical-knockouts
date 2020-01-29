from animals import Animal
from interfaces import Identifiable
from interfaces.animal import IPerching, ICaveDwelling

class Opeapea(Animal, Identifiable, IPerching, ICaveDwelling):
    def __init__(self):
        Animal.__init__(self)
        Identifiable.__init__(self)
        self.food = ["Flies", "Ants", "Silversword", "Blue Jade Vine"] 
        self.name = "Ope'ape'a"