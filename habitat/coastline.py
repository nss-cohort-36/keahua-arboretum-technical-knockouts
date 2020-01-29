from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from interfaces import Identifiable


class Coastline(IContainsAnimals, IContainsPlants, Identifiable):
    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)

    def add_animal(self, animal):
        try:
            if animal.swim:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Only Select animals with the ability to swim")

    def add_plant(self, plant):
        try:
            if plant.saltwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants that require brackish water or stagnant water to a Grassland biome")

    def check_animal(self, animal):
        if animal.cell_type == "isotonic" or animal.cell_type == "hypotonic":
            return True
        else:
            return False