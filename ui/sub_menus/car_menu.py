from models.car import Car
from services.carservice import CarService
from ui.ui_standard_functions import UIStandard
HOMECOMMANDS = ["h", "H", "s", "S"]


class CarUI(object):
    """Klasi sem sér um viðmót Sölumanns og ferðir þar um"""

    def __init__(self, name):
        self.__name = name
        self.__car_service = CarService()
        self.__uistandard = UIStandard(name)

    def car_menu(self):
        """Pprentar bílayfirlits viðmót og tekur við input"""
        choice = ""
        while choice not in HOMECOMMANDS:  # Placeholder
            choice = self.__uistandard.show_menu(
                """Bílayfirlit\n\t1. Allir Bílar
\t2. Lausir Bílar\n\t3. Í útleigu""")
            if choice == "1" or "2" or "3":
                if choice == "1":
                    menu = "sem eru lausir eða í útleigu"
                    listi1 = ["Fratekinn", "Laus"]
                if choice == "2":
                    menu = "sem eru lausir "
                    listi1 = ["Laus"]
                if choice == "3":
                    menu = "sem eru í útleigu"
                    listi1 = ["Fratekinn"]
                second_choice = input(
                    "\t1. Allar gerðir\n\t2. Jeppar\n\t3. Fólksbílar"
                    "\n\t4. Sendibílar")
                if second_choice == "2":
                    the_type = "Jeppar"
                    listi2 = ["Jeppi"]
                elif second_choice == "3":
                    the_type = "Fólksbílar"
                    listi2 = ["Fólksbill"]
                elif second_choice == "4":
                    the_type = "Sendibílar"
                    listi2 = ["Sendibill"]
                else:
                    the_type = "all_cars"
                    listi2 = ["Sendibill", "Folksbill", "Jeppi"]
            choice = self.second_car_menu(the_type, menu, listi1, listi2)
        return choice

    def second_car_menu(self, the_type, menu, listi1, listi2):
        self.__uistandard.print_header()
        print("Bílayfirlit - {} {}".format(the_type, menu))
        print("\tTegund | Bílnúmer | Staða\n\t", "-"*23)
        strengur = self.__car_service.get_list_of_cars(listi2, listi1)
        print(strengur)
        choice = input("Veldu aðgerð: ")
        return choice
