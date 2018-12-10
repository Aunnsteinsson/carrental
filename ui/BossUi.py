# Teddi sér um þennan fæl
from ui.sub_menus.car_menu import CarUI
from ui.sub_menus.employee_menu import EmployeeUI
from ui.ui_standard_functions import UIStandard
from datetime import date
from services.employeeservice import EmployeeService
from repositories.employeerepo import EmployeeRepo
import os

HOMECOMMANDS = ["h", "s"]
POSSIBLE_ACTIONS = "\t1. Pantanir\n\t2. Bílayfirlit\n\
\t3. Viðskiptavinir\n\t4. Starfsmenn\n\t5. Verðlisti\n\t6. Tekjur\n"


class BossUI(object):
    """ Klasi sem sér um viðmót yfirmanns í kerfi """
    def __init__(self, username):
        self.__username = username  # strengur sem inniheldur notendanafn
        self.__car_ui = CarUI(self.__username, "Yfirmaður")
        self.__employee_ui = EmployeeUI(self.__username, "Yfirmaður")
        self.__uistandard = UIStandard(self.__username, "Yfirmaður")
        self.__employee_service = EmployeeService()

    def print_header(self):
        ''' Prentar út haus fyrir UI '''
        print("{:40s} {:>54}".format(
            "Yfirmaður - notandi: {}".format(self.__username), str(date.today())))
        print(("-"*100))

    def show_menu(self, possible_operations):
        """ Fall sem prentar mögulegar aðgerðir og tekur við skipun """
        os.system('clear')
        self.print_header()
        print(possible_operations)

        choice = input("Veldu síðu: ")
        # Inn í þetta vantar að prenta út það sem er fyrir neðan
        return choice

    def main_menu(self):
        """ Fall sem sýnir aðalviðmót yfirmanns og færir hann á milli falla """
        os.system('clear')
        # Sýnir upphafsviðmót yfirmanns
        choice = ""
        while choice.lower() != HOMECOMMANDS[1]:
            os.system('clear')
            choice = self.show_menu(POSSIBLE_ACTIONS)
            if choice == "1":
                choice = self.show_all_orders()
            elif choice == "2":
                choice = self.__car_ui.boss_and_salesman_car_menu()
            elif choice == "3":
                choice = self.show_customers()
            elif choice == "4":
                self.__employee_ui.show_employees()
            elif choice == "5":
                self.price_menu()
            elif choice == "6":
                self.revenue()

    def show_all_orders(self):
        """ Fall sem prentar út allar pantanir í kerfinu """
        #from services import orderservice
        os.system('clear')
        self.print_header()
        print("\tdagsetning  |  Pönt.nr.  |  Nafn  |  Kennitala  |  Tegund  |  Bílnr.  |  Staða\n"+("-")*100)
        choice = ""
        while choice not in HOMECOMMANDS:
            choice = input("")
        return choice

    def car_menu(self):
        """  Sýnir bílayfirlitsviðmót yfirmanns og kallar á klasa eftir því sem við á """
        os.system('clear')
        choice = ""
        while choice not in HOMECOMMANDS:  # Placeholder
            choice = self.show_menu(
                """Bílayfirlit\n\t1. Allir Bílar
\t2. Lausir Bílar\n\t3. Í útleigu""")
            if choice == "1":
                pass
            if choice == "2":
                pass
            if choice == "3":
                pass
        return choice

    def show_customers(self):
        """ Prentar út alla viðskiptavini á skrá """
        os.system('clear')
        self.print_header()
        print("\tKennitala  |  Nafn  |  Sími\n"+("-")*100)
        choice = ""
        while choice not in HOMECOMMANDS:
            choice = input("")
        return choice

    def price_menu(self):
        """ Sýnir verðlistaviðmót yfirmanns og kallar á klasa eftir því sem við á """
        os.system('clear')
        self.print_header()
        print("Verðlisti\n\t{:<12} | {:<12}".format("Jeppi", "10000/dag"))
        print("\t{:<12} | {:<12}".format("Fólksbíll", "500/dag"))
        print("\t{:<12} | {:<12}".format("Sendibíll", "7000/dag"))
        print("\t{:<12} | {:<12}".format("Aukatrygging", "5000/dag"))
        choice = ""
        while choice not in HOMECOMMANDS:
            choice = input(
                "\nBreyta verði (F)ólksbíll, (J)eppi, (S)endibíll, (A)uka trygging: ")
        return choice

    def revenue(self):
        """ Prentar út tekjur bílaleigu """
        os.system('clear')
        self.print_header()
        print("Tekjur\n\t{:<25} | {:<10}\n\t".format(
            "Pöntunarnúmer", "Tekjur")+("-")*38)
        print("\t{:<25} | {:>10}".format("000001", "120.000 kr"))
        print("\t{:<25} | {:>10}".format("000002", "10.000 kr"))
        print("\n\t{:<25} | {:<10}\n\t".format("Mánuður", "Tekjur")+("-")*38)
        print("\t{:<25} | {:>10}".format("11", "130.000 kr"))
        choice = ""
        while choice not in HOMECOMMANDS:
            choice = input("")
        return choice

    def quit(self):
        """ Fer á upphafsskjá """
        pass