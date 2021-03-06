import datetime
import calendar
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
        self.__customer_menu = CustomerUI(self.__username, emp_type)
        self.__price_ui = PriceUI(self.__username, emp_type)
        self.__order_ui = OrderUI(self.__username, emp_type)
        self.__order_service = OrderService()

    def main_menu(self):
        """ Fall sem sýnir aðalviðmót yfirmanns og færir hann á milli falla """
        choice = ""
        while choice.lower() != HOMECOMMANDS[1]:
            self.__uistandard.clear_screen()
            choice = self.__uistandard.show_menu("{:^100}".format("YFIRMAÐUR"), "\t1. Pantanir\n\t2. Bílayfirlit\n\
\t3. Viðskiptavinir\n\t4. Starfsmenn\n\t5. Verðlisti\n\t6. Tekjur\n",
                                                 "Veldu síðu: ")
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
        return choice

    def revenue(self):
        """Fall sem sér um upphafssíðu tekjuyfirlits"""
        choice = ""
        while choice.lower() not in HOMECOMMANDS:
            self.__uistandard.clear_screen()
            self.__uistandard.print_header()
            self.__uistandard.location_header("Tekjuyfirlit")
            print("\n\t1. Fyrir sérstakt tímabil\n\t2. Fyrir ákveðið ár\n")
            choice = input("Veldu aðgerð: ")
            if choice == "1":
                choice = self.revenue_for_time_period()
            elif choice == "2":
                choice = self.revenue_in_year()
        return choice

    def revenue_for_time_period(self):
        """Fall sem sér um að gefa tekjuyfirlit fyrir innslegið timabíl.
         Biður um skráningu tímabils og prentar yfirlit"""
        choice = "j"
        while choice not in HOMECOMMANDS and choice != "b" and choice != "n":
            if choice.lower() == "j":
                self.__uistandard.clear_screen()
                self.__uistandard.print_header()
                self.__uistandard.location_header("Tekjuyfirlit")
                print()
                check_string = "Strengur til að athuga hvort dagar séu rétt\
 skráðir inn"
                while check_string:
                    new_sday = input("Upphafsdagur (dd): ")
                    new_smon = input("upphafsmánuður (mm): ")
                    new_syear = input("Upphafsár (yyyy): ")
                    new_eday = input("Skiladagur (dd): ")
                    new_emon = input("Skilamánuður (mm): ")
                    new_eyear = input("Skilaár (yyyy): ")
                    check_string = self.__uistandard.check_if_date_is_valid(
                        new_sday, new_smon, new_syear, new_eday,
                        new_emon,
                        new_eyear)
                    print(check_string)
                begin_date = "{}-{}-{}".format(new_syear, new_smon, new_sday)
                end_date = "{}-{}-{}".format(new_eyear, new_emon, new_eday)
                list_of_dates = self.__order_service.list_of_days(
                    begin_date, end_date)
                (total_rev,
                 string_of_order_and_rev) = self.__order_service.get_total_rev(
                    list_of_dates)
                begin_date = "{}/{}/{}".format(new_sday, new_smon, new_syear)
                end_date = "{}/{}/{}".format(new_eday, new_emon, new_eyear)
                self.__uistandard.clear_screen()
                self.__uistandard.print_header()
                self.__uistandard.location_header(
                    "Tekjuyfirlit fyrir sérstakt tímabil")
                print("Tekjur tímabils: {} til {}\n\n\n\t{:^15} | \
{:^14}".format(begin_date, end_date, "Pöntunarnúmer",
                    "Tekjur án vsk.")+("\n\t")+("-")*34)
                print(string_of_order_and_rev)
                print("\t {:>15}|{:<15}".format(("-")*15, ("-")*15))
                print("{:^13}  | {:>10,.0f} {:<4}\n".format(
                    "Heildartekjur tímabils", total_rev, "ISK"))
                choice = ""
                while choice != "j" and choice != "n":
                    choice = input(
                        "\nViltu skoða yfirlit yfir annað tímabil? ((J)á / (N)ei)\n\n\
Veldu aðgerð: ").lower()
        choice = self.__uistandard.back_input()
        return choice

    def revenue_in_year(self):
        """Fall sem sér um að gefa tekjuyfirlit fyrir innslegið ár.
         Biður um skráningu árs og prentar yfirlit"""
        choice = "j"
        while choice not in HOMECOMMANDS and choice != "b" and choice != "n":
            print("Vandamálið er annarsstaðar")
            if choice.lower() == "j":
                # Síða fyrir innskráningu árs sem skoða á tekjur frá.
                self.__uistandard.clear_screen()
                self.__uistandard.print_header()
                self.__uistandard.location_header("Tekjur - Fyrir ákveðið ár")
                tester = True
                while tester:
                    try:
                        year = int(input("\n\tSláðu inn ár: "))
                        if len(str(year)) == 4:
                            tester = False
                        else:
                            print("Árið {} er ekki í boði".format(year))
                    except ValueError:
                        print("Árið {} er ekki í boði".format(year))
                list_of_months_and_rev = []
                total_revenue_of_year = 0
                for month in range(1, 13):
                    num_days = calendar.monthrange(year, month)[1]
                    list_of_dates = [datetime.date(year, month, day)
                                     for day in range(1, num_days+1)]
                    (total_rev,
                     string_of_order_and_rev) = self.__order_service.get_total_rev(
                        list_of_dates)
                    total_revenue_of_year += total_rev
                    temp_list = [month, total_rev]
                    list_of_months_and_rev.append(temp_list)
                # Tekjur fyrir ákveðið ár prentaðar
                self.__uistandard.clear_screen()
                self.__uistandard.print_header()
                self.__uistandard.location_header("Tekjur - Fyrir ákveðið ár")
                print("Yfirlit yfir tekjur ársins {}\n\n".format(year))
                print("\t{:^15} | {:^14}".format(
                    "Númer mánaðar", "Tekjur án vsk."))
                print("\t" + ("-")*34)
                for listi in list_of_months_and_rev:
                    print("\t{:^15} | {:>10,.0f} {:<4}".format(
                        (listi[0]), (listi[1]), "ISK"))
                print("\t {:>15}|{:<15}".format(("-")*15, ("-")*15))
                print("   {:>18}   | {:>10,.0f} {:<4}\n".format(
                    "Tekjur árs", total_revenue_of_year, "ISK"))
                choice = ""
                while choice != "j" and choice != "n":
                    choice = input(
                        "\nViltu skoða yfirlit yfir annað ár? ((J)á / (N)ei)\n\n\
Veldu aðgerð: ").lower()
        choice = self.__uistandard.back_input()
        return choice
