
import os
from plants import MountainAppleTree
from plants import Silversword
from plants import RainbowEucalyptus
from plants import BlueJadeVine



def annex_plants(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus")
    print("4. Blue Jade Vine")

    choice = input("Choose your plant > ")
   
    new_plant = ""

    if choice == "1":
        new_plant = MountainAppleTree()
    if choice == "2":
        new_plant = Silversword()

    if choice == "3":
        new_plant = RainbowEucalyptus()

    if choice == "4":
        new_plant = BlueJadeVine()

    # We want to print the list of habitats that we are allowed to plant in (amount of plants and habitat)
    # WE need to make an array of all the habits to loop over    
    # list_of_habitats = []
    # list_of_habitats.extend(arboretum.river)
    # list_of_habitats.extend(arboretum.swamp)
    # list_of_habitats.extend(arboretum.coastline)
    # list_of_habitats.extend(arboretum.grassland)
    # list_of_habitats.extend(arboretum.mountain)
    # list_of_habitats.extend(arboretum.forest)

    selected_plant_habitats = new_plant.possible_habitats
    
    for habitat in selected_plant_habitats:
        if habitat == "grasslands":
            if arboretum.grasslands == []:
                print(f'There are no avialable {habitat}')
                input(f"press Enter to continue")

                




    #  Add the enumeration thing to have an index value (ex: make pizza function in pizza exercise)
    # for habitat in list_of_habitats:
        # if new_plant.name in habitat.plants_allowed

        # "name" in new_plant.name is referring to the name of each plant declared in each habitat class
    
    



       

    
# Not exact, but a model for making the next menu dynamically
    # for index, river in enumerate(arboretum.rivers):
    #     print(f'{index + 1}. River {river.id}')

    # print("Release the animal into which biome?")
    # choice = input("> ")



# def annex_habitat(arboretum):
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print("1. River")
#     print("2. Swamp")
#     print("3. Coastline")
#     print("4. Grassland")

#     choice = input("Choose your habitat > ")

#     if choice == "1":
#         river = River()
#         arboretum.rivers.append(river)
#     if choice == "2":
#         pass
