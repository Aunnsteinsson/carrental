from datetime import date
import time
from models.car import Car
from services.carservice import CarService
from ui.ui_standard_functions import UIStandard
HOMECOMMANDS = ["h", "s"]


class CarUI(object):
    """Klasi sem sér um viðmót Sölumanns og ferðir þar um"""

    def __init__(self, name, a_type):
        self.__username = name
        self.__car_service = CarService()
        self.__uistandard = UIStandard(name, a_type)

    # def print_car_header(self, status_of_car):  #Það er aldrei kallað í þetta fall. Á líklega að setja það í second car menu
    #    self.__uistandard.print_header()
    #    print("Bílayfirlit - {}".format(status_of_car))
    #    print("\t{:<20} | {:<20} | {:<20}".format(
    #        "Tegund", "Bílnúmer", "Staða"))
    #    print("\t{}".format("-"*60))

    # def print_cars(self, status):       #Það er aldrei kallað í þetta fall, Veit ekki alveg í hvað á að nota það
    #    os.system('cls')
    #    self.print_car_header(status)
    #    # sækja upplýsingar til prentunar út frá "status" í parameter

        # print("\t{:<20} | {:<20} | {:<20}".format(
        #     "Jeppi", "K1NG", "þriggjaDekkja"))
        # prenta upplýsingar um bíl

    def car_menu_admin(self):
        '''Bílayfirlit menu fyrir Kerfisstjóra'''
        choice = ""
        while choice.lower() not in HOMECOMMANDS:
            self.__uistandard.clear_screen()
            choice = self.__uistandard.show_menu(
                "Bílayfirlit\n\t1. Allir bílar\n\t2. Lausir bílar\n\t3. Í útleigu\n\t\
4. Nýskrá bíl\n\t5. Afskrá bíl\n", "Veldu aðgerð: ")

            if choice == "1" or choice == "2" or choice == "3":
                choice = self.show_cars(choice)
            elif choice == "4":
                new_car = self.add_new_car()
                self.__car_service.make_car(new_car)
            elif choice == "5":
                licence_plate = input("Númer bíls til afskráningar: ")
                self.check_if_licence_plate(licence_plate)
                # if licence_plate in `...... þarf að geta checkað hvort númeraplata sé á skrá??`
                print()
                approve_remove_car = input(
                    "Viltu eyða bíl með bílnúmerið {} ((J)á/(N)ei): ".format(
                        licence_plate))
                if approve_remove_car.lower() == 'j':
                    self.__car_service.remove_car(licence_plate)
                    print("\nBíl með númerið {} hefur verið eytt!".format(
                        licence_plate))
                else:
                    print("\nHætt við aðgerð!")
                time.sleep(2)
            return choice

    def check_if_licence_plate(self, licence_plate):
        value = self.__car_service.show_cars(licence_plate)
        print(value)

    def get_car_prices_dict(self):
        price_dict = self.__car_service.get_car_prices()
        return price_dict

    def add_new_car(self):
        self.__uistandard.clear_screen()
        approve_plate = ""
        while approve_plate.lower() != "j":
            self.__uistandard.clear_screen()
            self.__uistandard.print_header()
            print("\tFlokkar\n\t{}".format("-"*10))
            print("\t(J)eppi\n\t(F)ólksbíll\n\t(S)endibíll\n")
            a_type = input("Flokkur: ")
            if a_type.lower() == 'j':
                a_type = "Jeppi"
            elif a_type.lower() == 'f':
                a_type = "Folksbill"
            elif a_type.lower() == 's':
                a_type = "Sendibill"
            license_plate = input("Bílnúmer: ")
            print()
            approve_plate = input("Skrá {} með númerið {}\
 ((J)á/(N)ei)? ".format(
                a_type, license_plate))
            price_dict = self.get_car_prices_dict()
            new_car = Car(license_plate, a_type, price_dict)
        else:
            print("\nBíll hefur verið skráður!")
            time.sleep(2)
            return new_car

    def boss_and_salesman_car_menu(self):
        """Pprentar bílayfirlits viðmót og tekur við input"""
        choice = ""
        while choice not in HOMECOMMANDS:  # Placeholder
            choice = self.__uistandard.show_menu(
                """Bílayfirlit\n\t1. Allir Bílar
\t2. Lausir Bílar\n\t3. Í útleigu""", "Veldu Aðgerð")
            choice = self.show_cars(choice)
        return choice

    def show_cars(self, choice):
        if choice == "1" or choice == "2" or choice == "3":
            if choice == "1":
                menu = "sem eru lausir eða í útleigu"
                status_list = ["Fratekinn", "Laus"]
            if choice == "2":
                menu = "sem eru lausir "
                status_list = ["Laus"]
            if choice == "3":
                menu = "sem eru í útleigu"
                status_list = ["Fratekinn"]
            print("\n\t1. Allar gerðir\n\t2. Jeppar\n\t3. Fólksbílar"
                  "\n\t4. Sendibílar\n")
            second_choice = input("Veldu síðu: ")
            if second_choice == "2":
                the_type = "Jeppar"
                type_list = ["Jeppi"]
            elif second_choice == "3":
                the_type = "Fólksbílar"
                type_list = ["Fólksbill"]
            elif second_choice == "4":
                the_type = "Sendibílar"
                type_list = ["Sendibill"]
            else:
                the_type = "all_cars"
                type_list = ["Sendibill", "Folksbill", "Jeppi"]
            choice = self.second_car_menu(
                the_type, menu, status_list, type_list)
        return choice

    def second_car_menu(self, the_type, menu, status_list, type_list):
        self.__uistandard.print_header()
        print("Bílayfirlit - {} {}".format(the_type, menu))
        print("\t{:<20} | {:<20} | {:<20}".format(
            "Tegund", "Bílnúmer", "Staða"))
        print("\t{}".format("-"*60))
        strengur = self.__car_service.get_list_of_cars(
            type_list, status_list)
        print(strengur)
        choice = input("Veldu aðgerð: ")
        return choice
