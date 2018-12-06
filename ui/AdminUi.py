import os
import time
from datetime import date
from models.employee import Employee
from services.employeeservice import EmployeeService
from services.carservice import CarService
from repositories.employeerepo import EmployeeRepo

HOMECOMMANDS = ["h", "H", "s", "S"]
VALIDJOB = ["k", "s", "y"]


class AdminUI(object):
    def __init__(self, username):
        self.__username = username
        self.__employee_service = EmployeeService()
        self.__car_service = CarService()
        self.__employee_repo = EmployeeRepo()

    def print_header(self):
        '''Prentar haus fyrir Kerfisstjóra'''
        print("{:40s} {:>39}".format(
            "Kerfisstjóri - notandi: {}".format(self.__username), str(
                date.today())))
        print(("-"*80))

    def show_menu(self, text, prompt):
        '''Prentar það menu sem notandi er staddur á.'''
        self.print_header()
        print(text)

        choice = input(prompt)

        return choice

    def main_menu(self):
        '''Upphafssíða fyrir kerfisstjóra'''
        choice = ""
        while choice not in HOMECOMMANDS:
            os.system('cls')
            choice = self.show_menu(
                "\n\t1. Starfsmenn\n\t2. Nýr starfsmaður\n\t3. Bílayfirlit\n",
                "Veldu síðu: ")
            if choice == "1":
                choice = self.employee_menu()
            elif choice == "2":
                choice = self.new_employee()
            elif choice == "3":
                choice = self.car_menu()

    def print_car_header(self, status_of_car):
        self.print_header()
        print("Bílayfirlit - {}".format(status_of_car))
        print("\t{:<20} | {:<20} | {:<20}".format(
            "Tegund", "Bílnúmer", "Staða"))
        print("\t{}".format("-"*60))

    def print_cars(self, status):
        os.system('cls')
        self.print_car_header(status)
        # sækja upplýsingar til prentunar út frá "status" í parameter

        print("\t{:<20} | {:<20} | {:<20}".format(
            "Jeppi", "K1NG", "þriggjaDekkja"))
        # prenta upplýsingar um bíl

    def car_menu(self):
        '''Bílayfirlit menu fyrir Kerfisstjóra'''
        os.system('cls')
        choice = ""
        while choice not in HOMECOMMANDS:
            choice = self.show_menu(
                "Bílayfirlit\n\t1. Allir bílar\n\t2. Lausir bílar\n\t3. Í útleigu\n\t\
4. Nýskrá bíl\n\t5. Afskrá bíl\n", "Veldu aðgerð: ")
            if choice == "1":
                self.print_cars("Allir bílar")
            elif choice == "2":
                self.print_cars("Lausir bílar")
            elif choice == "3":
                self.print_cars("Í útleigu")
            elif choice == "4":
                # self.__car_service.make_car()
                pass
            elif choice == "5":
                licence_plate = input("Númer bíls: ")
                # athuga hvort bíll sé á skrá.
                self.__car_service.remove_car(licence_plate)
                print("\nBíl með númerið {} hefur verið eytt!".format(
                    licence_plate))

    def print_employee_header(self):
        '''Prentar haus fyrir starfmannayfirlit'''
        print("{:<10s}| {:<10s}| {:<10s}| {:<10s}| {:<10s}| {:<20s}".format(
            "Notandi", "Lykilorð", "Nafn", "Hlutverk", "Sími", "Heimilisfang"))
        print("-"*80)

    def print_empoloyee(self, employee):
        '''prentar lista yfir employees'''
        pass

    def employee_menu(self):
        '''Yfirlit yfir alla starfsmenn fyrirtækis,
        Möguleiki á að eyða starfsmanni'''
        os.system('cls')
        choice = ""
        get_pass = 1
        while choice not in HOMECOMMANDS:
            self.print_header()
            self.print_employee_header()
            # Prentar lista yfir starfsmenn
            employees_list = self.__employee_service.get_employees(get_pass)
            for employee in employees_list:
                print(employee)
            # aðgerðir tengdar starfsmanni (eyða, breyta)
            print("\nEyða starfsmanni?\n{}".format("-"*40))
            print("1. Eyða\n2. Breyta\n")
            choice = input("Veldu aðgerð: ")
            if choice == "1":
                # Eyða employee
                print("\nEyða\n{}".format("-"*40))
                username = input("Notandanafn: ")
                # check ef employee er til í kerfi(empl.csv), þá halda áfram,
                # annars láta vita að notandi er ekki til

                choice = input("Ertu viss? ((J)á/(N)ei): ")
                if choice.lower() == "j":
                    self.__employee_repo.remove_employee(username)
                    print("{}\nNotanda hefur verið eytt!\n".format("-"*40))
                elif choice.lower() == "n":
                    print("{}\nNotanda hefur ekki verið eytt!\n".format(
                        "-"*40))
                time.sleep(3)
                choice = "h"
            elif choice == "2":
                # Breyta einhverju við employee
                self.edit_employee()

    def edit_employee(self):
        '''Menu fyrir breytingu á starfsmanni'''
        print("\nBreyta\n{}".format("-"*40))
        username = input("Notandanafn: ")
        # checka ef notandanafn er til
        print("Hverju skal breyta?\n{}".format("-"*40))
        print("\t1. Lykilorð\n\t2. Nafn\n\t3. Heimilisfang\n\t4. Sími\n")
        choice = ""
        new_value = ""
        while choice not in HOMECOMMANDS:
            choice = input("Veldu aðgerð: ")
            if choice == "1":
                new_value = input("Nýtt lykilorð: ")
            elif choice == "2":
                new_value = input("Nýtt nafn: ")
            elif choice == "3":
                new_value = input("Nýtt heimilisfang: ")
            elif choice == "4":
                new_value = input("Nýr sími: ")

            # Skoða bug
            self.__employee_repo.change_info_of_employee(
                username, choice, new_value)
        choice = "h"

    def new_employee(self):
        '''Býr til nýjan starfsmann'''
        os.system('cls')
        choice = ""
        while choice not in HOMECOMMANDS:
            self.print_header()
            username = input("\tNotendanafn: ")
            password = input("\tLykilorð: ")
            name = input("\tNafn: ")
            address = input("\tHeimilisfang: ")
            phonenumber = input("\tSími: ")
            emp_type = ""
            while emp_type not in VALIDJOB:
                emp_type = input(
                    "\t(S)öludeild, (y)firmaður eða (k)erfisstjóri: ")
            if emp_type.lower() == "k":
                emp_type = "admin"
            elif emp_type.lower() == "y":
                emp_type = "yfirmadur"
            else:
                emp_type = "soludeild"
            an_employee = Employee(username, password, name,
                                   address, phonenumber, emp_type)
            choice = input(
                "\tStaðfesta nýjan notanda {} ((J)á/(N)ei): ".format(username))
            if choice.lower() == "j":
                self.__employee_service.add_employee(an_employee)
                print("\n{}\nNýr notandi hefur verið skráður!\n".format(
                    "-"*40))
            else:
                print("\nAction aborted! - Returning home")
            time.sleep(3)
            choice = "h"

    def quit(self):
        pass
