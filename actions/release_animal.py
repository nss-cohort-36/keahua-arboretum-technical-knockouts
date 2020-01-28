from animals import Gecko, RiverDolphin, Goose, Kikakapu, Pueo, Ulae, Opeapea, Spider

# you will pass keahua in as the arboretum
def release_animal(arboretum):
    animal = None

    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kikakapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Hawaiian Happy-Face Spider")

    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = Gecko()

    if choice == "2":
        animal = RiverDolphin()

    if choice == "3":
        animal = Goose()
    
    if choice == "4":
        animal = Kikakapu()
    
    if choice == "5":
        animal = Pueo()

    if choice == "6":
        animal = Ulae()

    if choice == "7":
        animal = Opeapea()

    if choice == "8":
        animal = Spider()

# create animal instance
#iterate over every habitat list in keahua
# put habitats in mega list called all_habitats
# also have a set called all_habitats_set that you can loop through to figure out type of habitat animal can go into


    for index, river in enumerate(arboretum.rivers):
        print(f'{index + 1}. River {river.id}')

    print("Release the animal into which biome?")
    choice = input("> ")
    # check to see which biomes animal can be added to
    # display appropriate biomes
    
    arboretum.rivers[int(choice) - 1].animals.append(animal)


