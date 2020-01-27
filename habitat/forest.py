from interfaces import IAquatic
from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants



class Forest(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)