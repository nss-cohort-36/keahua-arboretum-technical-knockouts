from plants import Plant

class IContainsPlants:
    def __init__(self):
        self.__plants = []
        self.__number_of_plants = 0
        self.__max_plants = False

    @property
    def plants(self):
        return self.__plants

    def add_plant(self, plant):
        if type(plant) is Plant:
            self.__plants.append(plant)
        else:
            return f''

    @property
    def number_of_plants(self):
        return self.__number_of_plants

    def increment_plant_count(self):
        self.__number_of_plants += 1

    @property
    def max_plants(self):
        return self.__max_plants

    def set_max_plants(self):
        self.__max_plants = True