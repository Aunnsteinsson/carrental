import os
from ui.sub_menus.car_menu import CarUI
from ui.sub_menus.employee_menu import EmployeeUI
from ui.ui_standard_functions import UIStandard
from services.orderservice import OrderService
from models.order import Order

HOMECOMMANDS = ["h", "H", "s", "S"]


class AdminUI(object):
    '''
    Klasi fyrir viðmót kerfisstjóra
    '''

    def __init__(self, username):
        self.orderservice = OrderService()
        self.__username = username
        self.__car_ui = CarUI(self.__username, "Kerfisstjóri")
        self.__employee_ui = EmployeeUI(self.__username, "Kerfisstjóri")
        self.__uistandard = UIStandard(self.__username, "Kerfisstjóri")

    def main_menu(self):
        '''Upphafssíða fyrir kerfisstjóra'''
        choice = ""
        while choice not in HOMECOMMANDS:
            os.system('cls')
            choice = self.__uistandard.show_menu(
                "\n\t1. Starfsmenn\n\t2. Nýr starfsmaður\n\t3. Bílayfirlit\n",
                "Veldu síðu: ")
            if choice == "1":
                choice = self.__employee_ui.employee_menu()
            elif choice == "2":
                choice = self.__employee_ui.new_employee()
            elif choice == "3":
                choice = self.__car_ui.car_menu_admin()
            elif choice == "4":
                choice = self.remove_order()
            elif choice == "5":
                choice = self.add_order()

    def remove_order(self):
        print("Eyða pöntun")
        ordernr = input("Pöntnr? ")
        self.orderservice.remove_order(ordernr)

    def add_order(self):
        ordernr = input("nr")
        start = input("start")
        end = input("end")
        car = input("car")
        insurance = input("ins")
        new_order = Order(ordernr, start, end, car, insurance)
        self.orderservice.make_order(new_order)

    def quit(self):
        pass
