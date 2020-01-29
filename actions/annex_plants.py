
import os
from plants import MountainAppleTree
from plants import Silversword
from plants import RainbowEucalyptus
from plants import BlueJadeVine



def annex_plants(kehua):
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
    allowed_habitats = []
    all_habitats = []
    # list_of_habitats.extend(kehua.rivers)
    # list_of_habitats.extend(kehua.swamps)
    # list_of_habitats.extend(kehua.coastlines)
    all_habitats.extend(kehua.grasslands)
    all_habitats.extend(kehua.mountains)
    # list_of_habitats.extend(kehua.forests)

    # filtering out habitats to grab the suitable habitats for each plant
    for habitat in all_habitats:
        if new_plant.name in habitat.plants_allowed:
            allowed_habitats.append(habitat)


    # we are displaying the suitable habitats in menu form so you need a dynamic menu that displays with an index (by number)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    for i,habitat in enumerate(allowed_habitats):
        print(f'{i+1}. {habitat.__class__.__name__}')

    choice = input("Chose your habitat > ")

    selected_habitat = allowed_habitats[choice - 1]


                
