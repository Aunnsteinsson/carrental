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
                "Bílayfirlit\n\t1. Allir bílar\n\t2. Lausir bílar\n\t3.Bílar sem ekki eru tilbúnir til útleigu\n\t\
4. Nýskrá bíl\n\t5. Afskrá bíl\n", "Veldu aðgerð: ")

            if choice == "1" or choice == "2" or choice == "3":
                choice = self.show_cars(choice)
            elif choice == "4":
                new_car = self.add_new_car()
                self.__car_service.make_car(new_car)
            elif choice == "5":
                licence_plate = input("Númer bíls til afskráningar: ")
                if self.check_if_licence_plate(licence_plate) is False:
                    print("Bílnúmer er ekki á skrá\n")
                    time.sleep(2)
                else:
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
        return self.__car_service.show_cars(licence_plate)

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
                a_type = "jeppi"
            elif a_type.lower() == 'f':
                a_type = "folksbill"
            elif a_type.lower() == 's':
                a_type = "sendibill"
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
<<<<<<< HEAD
          #  self.__uistandard.print_location_header("Yfirmaður - Bílayfirlit")
=======
>>>>>>> f33b8d56be9c4e13fac7d460109c477459f4058f
            choice = self.__uistandard.show_menu(
                """Bílayfirlit\n\t1. Allir Bílar
\t2. Lausir Bílar\n\t3. Bílar sem eru ekki tilbúnir til útleigu\n\t4. Afhenda eða taka á móti bíl\n""", "Veldu Aðgerð: ")
            choice = self.show_cars(choice)
            choice = self.return_car_menu(choice)
        return choice

    def return_car_menu(self, choice):
        while choice not in HOMECOMMANDS:
            licence_plate = input(
                "Hvert er bílnúmerið á bílnum sem þú vilt breyta stöðunni á? ").upper()
            the_car = self.__car_service.show_cars(licence_plate)
            if the_car:
                print("{:^8} | {:^12} | {:^15} | {:^30} | {:^15} ".format(
                    "Bílnúmer", "Tegund", "Verð/dag", "Staða bíls", "Næsta bókun"))
                print(the_car)
                status = input("Er bíllinn í stæði? (J)á eða (N)ei ").lower()
                if status == "j" or status == "n":
                    self.__car_service.change_status(status, the_car)
                    print("Breyting móttekin. Hér er núverandi staða bíls")
                    print("{:^8} | {:^12} | {:^15} | {:^30} | {:^15} ".format(
                        "Bílnúmer", "Tegund", "Verð/dag", "Staða bíls", "Næsta bókun"))
                    print(the_car)
                else:
                    print("Ekki rétt skipun. Engin breyting verður gerð")
            else:
                print("Enginn bíll með þetta bílnúmer")
            choice = ""
            while choice not in HOMECOMMANDS and choice != "a":
                choice = input(
                    "Veldu aðgerð: (H)eim, (S)krá út eða (A) til að halda áfram: ").lower()
        return choice

    def show_cars(self, choice):
        if choice == "1" or choice == "2" or choice == "3":
            if choice == "1":
                menu = "sem eru lausir eða í útleigu"
                status_list = ["Hefur ekki enn verið skilað",
                               "Leigður en ekki sóttur", "Í útleigu", "Tilbúinn til útleigu"]
            if choice == "2":
                menu = "sem eru lausir "
                status_list = ["Tilbúinn til útleigu"]
            if choice == "3":
                menu = "sem eru ekki tilbúnir til útleigu"
                status_list = ["Hefur ekki enn verið skilað",
                               "Leigður en ekki sóttur", "Í útleigu"]
            print("\n\t1. Allar gerðir\n\t2. Jeppar\n\t3. Fólksbílar"
                  "\n\t4. Sendibílar\n")
            second_choice = input("Veldu síðu: ")
            if second_choice == "2":
                the_type = "Jeppar"
                type_list = ["jeppi"]
            elif second_choice == "3":
                the_type = "Fólksbílar"
                type_list = ["folksbill"]
            elif second_choice == "4":
                the_type = "Sendibílar"
                type_list = ["sendibill"]
            elif second_choice in HOMECOMMANDS:
                return second_choice
            elif second_choice == "1":
                the_type = "Allir bílar"
                type_list = ["sendibill", "folksbill", "jeppi"]
            else:
                print("Val ekki í boði. Notandi sendur aftur heim")
                time.sleep(3)
                return "h"
            choice = self.second_car_menu(
                the_type, menu, status_list, type_list)
        return choice

    def second_car_menu(self, the_type, menu, status_list, type_list):
        self.__uistandard.clear_screen()
        self.__uistandard.print_header()
        line_seperator = ("-"*100)
        print("Bílayfirlit - {} {}".format(the_type, menu))
        print(line_seperator)
        print("{:^8} | {:^12} | {:^15} | {:^30} | {:^15} ".format(
            "Bílnúmer", "Tegund", "Verð/dag", "Staða bíls", "Næsta bókun"))
        print(line_seperator)
        strengur = self.__car_service.get_list_of_cars(
            type_list, status_list)
        if strengur == "":
            strengur = (
                "\nÞví miður eru engir bílar sem uppfylla þessi leitarskilyrði\n")
        print(strengur)
        choice = ""
        while choice not in HOMECOMMANDS and choice != "a":
            choice = input(
                "Veldu aðgerð: (H)eim, (S)krá út eða (A) fyrir að afhenda eða taka á móti bíl: ").lower()
        return choice
