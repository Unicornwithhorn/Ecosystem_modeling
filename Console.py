import Text
from Text import *
from Classes import Menu, Ecosystem_list, Ecosystem

def menu(current_menu: Menu ) -> int:
    print(current_menu.text)
    while True:
        choice = input(Text.menu_choice)
        if choice.isdigit() and 0 < int(choice) < current_menu.number_of_points + 1:
            return int(choice)
        print(Text.input_error)

def show_ecosystems(list_of_ecosystems: Ecosystem_list):
    print('  № Название урочища          Шир.водотока  Подстил.поверхность            Почвы')
    for point in list_of_ecosystems.ecosystems:
        print(f'{point.uid:>3} {point.name:>25} {point.river_size:>11}м {point.underlying_surface:>30} {point.soil:>30}')




