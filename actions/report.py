def build_facility_report(arboretum):
    display_habitat_info(arboretum.mountains)
    display_habitat_info(arboretum.grasslands)
    display_habitat_info(arboretum.rivers)
    display_habitat_info(arboretum.forests)
    display_habitat_info(arboretum.swamps)
    display_habitat_info(arboretum.coastlines)

# takes a list of habitats and displays each habitat and the animals contained in it
def display_habitat_info(habitat_list):
    for habitat in habitat_list:
        print(f'{habitat.name} [{str(habitat.id)[0:8]}]')
        # need the name of the animal list variable
        for animal in habitat.animal_list:
            print(f'{animal.name} ({str(animal.id)[0:8]})')

    for grassland in arboretum.grasslands:
        print(f'Grassland [{grassland.id}]')

    for swamp in arboretum.swamps:
        print(f'Swamp [{swamp.id}]')

    for coastline in arboretum.coastlines:
        print(f'Coastline [{coastline.id}]')

    for forest in arboretum.forests:
        print(f'Forest [{forest.id}]')

    for mountains in arboretum.mountains:
        print(f'Mountains [{mountains.id}]')

    input("\n\nPress any key to continue...")