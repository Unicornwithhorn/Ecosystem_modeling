class Ecosystem:
    def __init__(self, name, river_size, geomorphological_level, underlying_surface, soil):
        self.name = name
        self.river_size = river_size
        self.geomorphological_level = geomorphological_level
        self.underlying_surface = underlying_surface
        self.soil = soil
        self.uid = 1
    def __str__(self):
        return (f'{self.uid}) Урочище {self.name}. Ширина образующего водотока - {self.river_size} м. Расположение на '
                f'катене - {self.geomorphological_level}, подстилающие породы - {self.underlying_surface}.'
                f'Тип почв - {self.soil}')

# class Vegetation:
#     def __init__(self, forest, undergrowth, bush, grass, moss_and_lichen):
#         self.forest: list[Trees]
#         self.undergrowth: list[Trees]
#         self.bush: list[Bush]
#         self.grass: list[Grass]
#         self.moss_and_lichen: list[Moss_and_lichen]

class Ecosystem_list:
    def __init__(self, path: str):
        self.ecosystems: list[Ecosystem] = []
        self.vegetable: list[Vegetation] = []
        self.path = path
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
        for landscape in data:
            uid, name, river_size, geomorphological_level, underlying_surface, soil = landscape.strip().split(':')
            ecosystem = Ecosystem(name, river_size, geomorphological_level, underlying_surface, soil)
            ecosystem.uid = uid
            self.ecosystems.append(ecosystem)

    def safe_ecosystem(self):
        data_file = open(self.path, 'w', encoding='UTF-8')
        for i in self.ecosystems:
            data_file.writelines(f'{i.uid}:{i.name}:{i.river_size}:{i.geomorphological_level}:{i.underlying_surface}:'
                                 f'{i.soil}\n')
        data_file.close()
class Menu:
    def __init__(self, text, number_of_points):
        self.text = text
        self.number_of_points = number_of_points

