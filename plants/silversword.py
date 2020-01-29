from .plants import Plants

class Silversword(Plants):
    def __init__(self):
      super().__init__()
      self.location =""
      self.name = "Silversword"
      # self.possible_habitats.append("grasslands")
 

#  interface for where each plant is allowed to go instead of self.__natural_habitats = ["Grassland"]   