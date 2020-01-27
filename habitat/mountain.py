from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from interfaces import Identifiable
from interfaces import Ihas_animals



class Mountain():

     def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)
      self.plants_allowed = ["Mountain Apple Tree"]
      self.plants_capacity = 4
      
      


    #   def add_animal(self, animal):
    #     try:
    #         if animal.aquatic and animal.cell_type == "hypertonic":
    #             self.animals.append(animal)
    #     except AttributeError:
    #         raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")
        

# ERN = mountain()
# print(ERN.plants_allowed)
# print(ERN.plants_capacity)