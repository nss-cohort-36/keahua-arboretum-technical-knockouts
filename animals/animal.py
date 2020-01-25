class Animal:
    def __init__(self):
        self.__species = ""
        # self.age = 0
        self.__food = ["random food"]
        self.__allowed_habitats = []

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, species):
        if type(species) is str:
            self.__species = species
        else:
            return "Please input a string for the species name!"

    @property
    def food(self):
        return self.__food

    @food.setter
    def food(self, food):
        if type(food) is list:
            self.__food.extend(food)
        else:
            return "Please input a list of foods for the animal."

    @property
    def allowed_habitats(self):
        return self.__allowed_habitats

    @allowed_habitats.setter
    def allowed_habitats(self, allowed_habitats):
        if type(allowed_habitats) is list:
            self.__allowed_habitats = allowed_habitats
        else:
            return "Please input a list of habitats for the animal."
    

 