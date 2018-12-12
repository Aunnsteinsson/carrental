from datetime import date
from repositories.employeerepo import EmployeeRepo
from services.employeeservice import EmployeeService
from ui.ui_standard_functions import UIStandard
from ui.sub_menus.car_menu import CarUI
from ui.sub_menus.employee_menu import EmployeeUI
from services.orderservice import OrderService
from ui.sub_menus.customer_menu import CustomerUI
from services.carservice import CarService
from ui.sub_menus.price_menu import PriceUI
from ui.sub_menus.order_menu import OrderUI

HOMECOMMANDS = ["h", "s"]


class BossUI(object):
    """ Klasi sem sér um viðmót yfirmanns í kerfi """

    def __init__(self, username, emp_type):
        self.__username = username  # strengur sem inniheldur notendanafn
        self.__car_ui = CarUI(self.__username, emp_type)
        self.__employee_ui = EmployeeUI(self.__username, emp_type)
        self.__uistandard = UIStandard(self.__username, emp_type)
        self.__employee_service = EmployeeService()
        self.__order_service = OrderService()
        self.__customer_ui = CustomerUI(self.__username, emp_type)
        self.__car_service = CarService()
        self.__price_ui = PriceUI(self.__username, emp_type)
        self.__order_ui = OrderUI(self.__username, emp_type)

    def main_menu(self):
        """ Fall sem sýnir aðalviðmót yfirmanns og færir hann á milli falla """
        choice = ""
        while choice.lower() != HOMECOMMANDS[1]:
            self.__uistandard.clear_screen()
            choice = self.__uistandard.show_menu("\t1. Pantanir\n\t2. Bílayfirlit\n\
\t3. Viðskiptavinir\n\t4. Starfsmenn\n\t5. Verðlisti\n\t6. Tekjur\n", "Veldu síðu: ")
            self.__uistandard.clear_screen()
            if choice == "1":
                choice = self.__order_ui.order_list_menu()
            elif choice == "2":
                choice = self.__car_ui.boss_and_salesman_car_menu()
            elif choice == "3":
                choice = self.__customer_ui.get_customer_list()
            elif choice == "4":
                choice = self.__employee_ui.show_employees()
            elif choice == "5":
                choice = self.__price_ui.boss_change_price_menu()
            elif choice == "6":
                choice = self.revenue()

    def show_all_orders(self):
        """ Fall sem prentar út allar pantanir í kerfinu """
        #from services import orderservice
        print("\tdagsetning  |  Pönt.nr.  |  Nafn  |  Kennitala  |  Tegund  |  Bílnr.  |  Staða\n" + ("-")*100)
        self.__order_service.show_orders()
        choice = ""
        while choice.lower() not in HOMECOMMANDS:
            choice = input("\n(H)eim - (S)krá út: ")
        return choice

    """ def show_customers(self):
        print("\tKennitala  |  Nafn  |  Sími\n"+("-")*100)
        choice = ""
        while choice.lower() not in HOMECOMMANDS:
            choice = input("\n(H)eim - (S)krá út: ")
        return choice """

    def revenue(self):
        """ Prentar út tekjur bílaleigu """
        print("Tekjur\n\t{:<25} | {:<10}\n\t".format(
            "Pöntunarnúmer", "Tekjur")+("-")*38)
        print("\t{:<25} | {:>10}".format("000001", "120.000 kr"))
        print("\t{:<25} | {:>10}".format("000002", "10.000 kr"))
        print("\n\t{:<25} | {:<10}\n\t".format("Mánuður", "Tekjur")+("-")*38)
        print("\t{:<25} | {:>10}".format("11", "130.000 kr"))
        choice = ""
        while choice.lower() not in HOMECOMMANDS:
            choice = input("\n(H)eim - (S)krá út: ")
        return choice
