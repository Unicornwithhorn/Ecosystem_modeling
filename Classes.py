import random
from Abiotic_ecoparameters import abundance

class Ecosystem:
    def __init__(self, name, river_size, geomorphological_level, underlying_surface, soil):
        self.name = name
        self.river_size = river_size
        self.geomorphological_level = geomorphological_level
        self.underlying_surface = underlying_surface
        self.soil = soil
        self.uid = 1
        self.path = 'Species.txt'
        self.species = []
    def __str__(self):
        return (f'{self.uid}) Урочище {self.name}. Ширина образующего водотока - {self.river_size} м. Расположение на '
                f'катене - {self.geomorphological_level}, подстилающие породы - {self.underlying_surface}.'
                f'Тип почв - {self.soil}')
    def create_species_list(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for i in range(random.randint(0,30)):
            self.species.append(f'{random.choice(data)}&{random.choice(abundance)}')

    def show_species(self):
        for i in self.species:
            print(i)


# class Vegetation:
#     def __init__(self, forest, undergrowth, bush, grass):
#         self.forest: list[Trees]
#         self.undergrowth: list[Trees]
#         self.bush: list[Bush]
#         self.grass: list[Grass]


class Ecosystem_list:
    def __init__(self, path: str, path2: str):
        self.ecosystems: list[Ecosystem] = []
        self.vegetable: list[Vegetation] = []
        self.path = path
        self.path2 = path2
    def add_ecosystem(self, new: Ecosystem):
        self.ecosystems.append(new)

    def delete_ecosystem(self, number):
        self.ecosystems.pop(number - 1)
        i = 1
        for element in self.ecosystems:
            element.uid = str(i)
            i += 1

    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        with open(self.path2, 'r', encoding='UTF-8') as file:
            data2 = file.readlines()
        for landscape in data:
            uid, name, river_size, geomorphological_level, underlying_surface, soil = landscape.strip().split(':')
            ecosystem = Ecosystem(name, river_size, geomorphological_level, underlying_surface, soil)
            ecosystem.uid = uid
            for plant in data2:
                uid_species, species_name = landscape.strip().split(':')
                if uid_species == uid:
                    ecosystem.species.append(species_name)
            self.ecosystems.append(ecosystem)

    # def vegetation_create(self)
    #     with open(self.path2, 'r', encoding='UTF-8') as file:
    #         data = file.readlines()
    #     for landscape in data:
    #         uid, name, river_size, geomorphological_level, underlying_surface, soil = landscape.strip().split(':')
    #         ecosystem = Ecosystem(name, river_size, geomorphological_level, underlying_surface, soil)
    #         ecosystem.uid = uid
    #         self.ecosystems.append(ecosystem)

    def safe_ecosystem(self):
        data_file = open(self.path, 'w', encoding='UTF-8')
        for i in self.ecosystems:
            data_file.writelines(f'{i.uid}:{i.name}:{i.river_size}:{i.geomorphological_level}:{i.underlying_surface}:'
                                 f'{i.soil}\n')
        data_file.close()
        data_file2 = open(self.path2, 'w', encoding='UTF-8')
        for i in self.ecosystems:
            for element in i.species:
                data_file2.writelines(f'{i.uid}:{element}\n')
        data_file2.close()
class Menu:
    def __init__(self, text, number_of_points):
        self.text = text
        self.number_of_points = number_of_points

