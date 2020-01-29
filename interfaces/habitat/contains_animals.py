class IContainsAnimals():

    def __init__(self):
        self.__animals = []
        self.__animal_count = 0
        
    @property
    def animals(self):
        return self.__animals

    def add_animal(self, animal):
        self.__animals.append(animal)

    @property
    def animal_count(self):
        return self.__animal_count

    def increment_animal_count(self):
        self.__animal_count += 1
