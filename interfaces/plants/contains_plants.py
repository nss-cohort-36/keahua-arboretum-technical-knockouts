class IContainsPlants:
    def __init__(self):
        self.__plants = []
        self.__number_of_plants = 0

    @property
    def plants(self):
        return self.__plants