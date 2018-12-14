import time
from services.carservice import CarService
from ui.ui_standard_functions import UIStandard

HOMECOMMANDS = ["h", "s"]


class PriceUI(object):

    def __init__(self, name, a_type):
        self.__username = name
        self.__car_service = CarService()
        self.__uistandard = UIStandard(name, a_type)

    def get_price_dict(self):
        price_dict = self.__car_service.get_car_prices()
        return price_dict

    def print_price_menu(self):
        """ Sýnir verðlistaviðmót yfirmanns og kallar á klasa eftir því sem við á """
        self.__uistandard.print_header()
        price_dict = self.get_price_dict()
        self.__uistandard.location_header("Verðlisti")
        print("{:^15} | {:^15}".format("Tegund", "Verð/dag"))
        self.__uistandard.line_seperator()
        for types, price in price_dict.items():
            # Þessi lykkja er nauðsynleg vegna þess að .csv skrár lesa ekki íslenska stafi
            price = float(price)
            if types == "folksbill":
                types = "Fólksbíll"
            elif types == "sendibill":
                types = "Sendibíll"
            elif types == "jeppi":
                types = "Jeppi"
            elif types == "trygging":
                types = "Aukatrygging"
            print("{:<15} | {:>12,.0f} {}".format(types, price, "ISK"))

    def salesman_get_price_menu(self):
        self.print_price_menu()
        choice = ""
        while choice.lower() not in HOMECOMMANDS:
            choice = input("\nVeldu aðgerð: ")
        return choice

    def boss_change_price_menu(self):
        choice = ""
        while choice.lower() not in HOMECOMMANDS and choice.lower() != "b":
            self.__uistandard.clear_screen()
            self.print_price_menu()
            print("\n\nMögulegar aðgerðir\n{}".format("-"*25))
            print("1. Breyta verði á tegund\n")
            choice = input("\nVeldu aðgerð: ")
            if choice.lower() == "1":
                choice = "j"
                while choice.lower() == 'j':
                    self.__uistandard.clear_screen()
                    self.print_price_menu()
                    car_choice = input("""\nVeldu það verð sem þú vilt breyta - (F)ólksbíl, \
(J)eppi, (S)endibíll, (T)rygging, (A)uka trygging: """)
                    if car_choice.lower() == "f":
                        a_type = "folksbill"
                    elif car_choice.lower() == "j":
                        a_type = "jeppi"
                    elif car_choice.lower() == "s":
                        a_type = "sendibill"
                    elif car_choice.lower() == "t":
                        a_type = "skyldutrygging"
                    elif car_choice.lower() == "a":
                        a_type = "aukatrygging"
                    else:
                        return choice
                    new_price = input("\nNýtt verð: ")
                    self.__car_service.change_price_of_type(a_type, new_price)
                    print("\nVerði breytt!\n")
                    time.sleep(1)
                    choice = input(
                        "Viltu breyta öðru verði? ((J)á/(N)ei) ").lower()
        return choice
