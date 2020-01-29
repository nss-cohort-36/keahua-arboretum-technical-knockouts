import os



def feed_animal(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Pueo")
    print("2. River Dolphins")
    print("3. 'Ulae")
    print("4. Nene Goose") 
    print("5. Kīkākapu")
    print("6. Ope'ape'a")
    print("7. Hawaiian Happy-Face Spider")

    choice = input("Choose animal to feed > ")


    # # ran a nested 4 loop in order to access all the animals in the arboretum and have them appended to the all_animals list

    # all_animals = []     
    # for river in arboretum.rivers:
    #     for animal in river.animals:
    #         all_animals.append(animal)
    # for swamp in arboretum.swamps:
    #     for animal in swamp.animals:
    #         all_animals.append(animal)
    # for mountain in arboretum.mountains:
    #     for animal in mountain.animals:
    #         all_animals.append(animal)
    # for grassland in arboretum.grasslands:
    #     for animal in grassland.animals:
    #         all_animals.append(animal)
    # for forest in arboretum.forests:
    #     for animal in forest.animals:
    #         all_animals.append(animal)
    # for coastline in arboretum.coastlines:
    #     for animal in coastline.animals:
    #         all_animals.append(animal)

    # # index starts at 1 looping through all the animals and printing them based on index position

    # index = 1
    # for animal in all_animals:
    #     print(f'{index} {animal.name} {animal.id}')
    #     index += 1


    