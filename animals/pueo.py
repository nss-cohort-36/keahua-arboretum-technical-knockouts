from animals import Animal
from interfaces import Identifiable
from interfaces.animal import IPerching
from interfaces.animal import IWalking

class Pueo(Animal, Identifiable, IPerching, IWalking):
    def __init__(self):
        Animal.__init__(self)
        Identifiable.__init__(self)
        self.food = ["Mouse", "Rat", "Hamster"]
        self.name = "Pueo" 