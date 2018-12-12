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

    def price_menu(self):
            """ Sýnir verðlistaviðmót yfirmanns og kallar á klasa eftir því sem við á """
            price_dict = self.get_price_dict()
            print("Verðlisti:\n\n{:^15} | {:^15}".format("Tegund", "Verð/dag")+("\n")+("-")*34)
            for types, price in price_dict.items():
                #Þessi lykkja er nauðsynleg vegna þess að .csv skrár lesa ekki íslenska stafi
                price = float(price)
                if types == "folksbill":
                    types = "Fólksbíll"
                elif types == "sendibill":
                    types = "Sendibíll"
                elif types == "jeppi":
                    types = "Jeppi"
                elif types == "trygging":
                    types = "Aukatrygging"
                print("{:<15} | {:>12,.2f} {}".format(types, price, "ISK"))
            choice = ""
            while choice.lower() not in HOMECOMMANDS:
                choice = input("\n(H)eim - (S)krá út - (B)reyta verði: ")    
                if choice.lower() == "b":
                    car_choice = input(
                        "\nVeldu það verð sem þú vilt breyta - (F)ólksbíl, (J)eppi, (S)endibíll, (A)uka trygging: ")
                    if car_choice.lower() == "f":
                        a_type = "folksbill"
                    elif car_choice.lower() == "j":
                        a_type = "jeppi"
                    elif car_choice.lower() == "s":
                        a_type = "sendibill"
                    elif car_choice.lower() == "a":
                        a_type = "trygging"
                    else:
                        return choice
                    new_price = input("\nNýtt verð: ")
                    self.__car_service.change_price_of_type(a_type, new_price)
                    choice = input("\nVerði breytt!\n\nVeldu (H) til að fara heim, eða (S) til að skrá þig út: ")
            return choice