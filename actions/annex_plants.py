
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
