from datetime import date, datetime
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
from models.order import Order

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
        self.__customer_menu = CustomerUI(self.__username, emp_type)
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
                choice = self.__customer_menu.get_customer_list()
            elif choice == "4":
                choice = self.__employee_ui.show_employees()
            elif choice == "5":
                choice = self.__price_ui.boss_change_price_menu()
            elif choice == "6":
                choice = self.revenue()

    def revenue(self):

        new_sday = input("Upphafsdagur tímabils (dd): ")
        new_smon = input("Upphafsmánuður tímabils(mm): ")
        new_syear = input("Upphafs ár tímabils (yyyy): ")
        new_eday = input("Lokadagur tímabils (dd): ")
        new_emon = input("Lokamánuður tímabils (mm): ")
        new_eyear = input("Lokaár tímabils (yyyy): ")
        begin_date = "{}-{}-{}".format(new_syear, new_smon, new_sday)
        end_date = "{}-{}-{}".format(new_eyear, new_emon, new_eday)
        total_rev, string_of_order_and_rev = self.__order_service.get_total_rev(
            begin_date, end_date)
        begin_date = "{}/{}/{}".format(new_sday, new_smon, new_syear)
        end_date = "{}/{}/{}".format(new_eday, new_emon, new_eyear)
        self.__uistandard.clear_screen()
        self.__uistandard.print_header()
        self.__uistandard.line_seperator()
        """ Prentar út tekjur bílaleigu """
        print("Tekjur\n\n{:^25} | {:^15}\n".format(
            "Pönt.nr.", "Tekjur")+("-")*36)
        print(string_of_order_and_rev)
        print("Tímabil frá {} til {}".format(
            begin_date, end_date))
        print("\n{:<15} | {:>11,.0f} {:<4}".format(
            "Heildartekjur tímabils", total_rev, "ISK"))
        choice = ""
        while choice.lower() not in HOMECOMMANDS:
            choice = input("\n(H)eim - (S)krá út: ")
        return choice
