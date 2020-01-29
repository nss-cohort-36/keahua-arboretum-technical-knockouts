from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from interfaces import Identifiable
from interfaces import Ihas_plants
from interfaces import Ihas_animals



class Grassland(IContainsAnimals, IContainsPlants, Identifiable):

     def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)
      self.plants_allowed = ["silversword", "blue jade vine"]
      self.plants_capacity = 15
    #   Ihas_plants.__init__(self)
      Ihas_animals.__init__(self)

      def add_animal(self, animal):
        try:
            if animal.fly:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Only Select animals with the ability to fly")
        
      def add_plant(self, plant):
        try:
            if plant.freshwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants that require brackish water or stagnant water to a Grassland biome")
