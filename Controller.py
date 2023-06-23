import random
from Menu import *
from Console import menu, show_ecosystems
import Abiotic_ecoparameters
from Classes import Ecosystem, Ecosystem_list
from Text import *
def start(ecosystem_list: Ecosystem_list):
    choice = menu(start_menu)
    count_of_ecosystems = len(ecosystem_list.ecosystems)
    match choice:
        case 1:
            ecosystem_list.add_ecosystem(random_ecosystem_create(count_of_ecosystems))
            start(ecosystem_list)
        case 2:
            print(sorry_user)
            start(ecosystem_list)
        case 3:
            show_ecosystems(ecosystem_list)
            choice = menu(choose_or_exit)
            match choice:
                case 1:
                    your_ecosystem = after_show(ecosystem_list)
                    print(you_chose)
                    print(your_ecosystem)
                    work_with_ecosystem(your_ecosystem, ecosystem_list)
                case 2:
                    start(ecosystem_list)
        case 4:
            ecosystem_list.safe_ecosystem()
            start(ecosystem_list)
        case 5:
            pass
def random_ecosystem_create(count_of_ecosystems):
    sex = random.randint(1,3)
    match sex:
        case 1: ecosystem_name = random.choice(Abiotic_ecoparameters.first_names_of_place_female)\
                                     + ' ' + random.choice(Abiotic_ecoparameters.last_name_of_place_female)
        case 2: ecosystem_name = random.choice(Abiotic_ecoparameters.first_names_of_place_male)\
                                     + ' ' + random.choice(Abiotic_ecoparameters.last_name_of_place_male)
        case 3: ecosystem_name = random.choice(Abiotic_ecoparameters.first_names_of_place_med)\
                                     + ' ' + random.choice(Abiotic_ecoparameters.last_name_of_place_med)
    geomorphological_level = random.choice(Abiotic_ecoparameters.geomorphical_level_set)
    if geomorphological_level == Abiotic_ecoparameters.geomorphical_level_set[3]:
        underlying_surface = random.choice(Abiotic_ecoparameters.underlying_surface_set[:9])
        soil = random.choice(Abiotic_ecoparameters.soils_set[:11])
    elif geomorphological_level == Abiotic_ecoparameters.geomorphical_level_set[2]:
        underlying_surface = random.choice(Abiotic_ecoparameters.underlying_surface_set[8:11])
        soil = random.choice(Abiotic_ecoparameters.soils_set[:11])
    elif geomorphological_level == Abiotic_ecoparameters.geomorphical_level_set[1]:
        underlying_surface = random.choice(Abiotic_ecoparameters.underlying_surface_set[8:])
        soil = random.choice(Abiotic_ecoparameters.soils_set[9:])
    else:
        underlying_surface = random.choice(Abiotic_ecoparameters.underlying_surface_set[11:])
        soil = random.choice(Abiotic_ecoparameters.soils_set[9:])

    ecosystem = Ecosystem(ecosystem_name, random.randint(1,10), geomorphological_level, underlying_surface, soil)
    count_of_ecosystems+=1
    ecosystem.uid = count_of_ecosystems
    print(you_create)
    print(ecosystem)
    return ecosystem
def after_show(ecosystem_list: Ecosystem_list):
    while True:
        choice_after_show = input(choice_from_ecosystems)
        if choice_after_show.isdigit():
            # choice_after_show = int(choice_after_show)
            for element in ecosystem_list.ecosystems:
                if element.uid == choice_after_show:
                    return element
        print(input_error)

def work_with_ecosystem(ecosystem: Ecosystem, ecosystem_list: Ecosystem_list):
    choice = menu(ecosystem_main_work_menu)
    match choice:
        case 1:
            # print(ecosystem.uid + 1)
            ecosystem_list.delete_ecosystem(int(ecosystem.uid))
            start(ecosystem_list)
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            start(ecosystem_list)