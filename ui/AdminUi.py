from datetime import date
from models.employee import Employee
from services.employeeservice import EmployeeService
from repositories.employeerepo import EmployeeRepo

HOMECOMMANDS = ["h", "H", "s", "S"]


class AdminUI(object):
    def __init__(self, username):
        self.__username = username
        self.__employee_service = EmployeeService()
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
            choice = self.show_menu(
                "\n\t1. Starfsmenn\n\t2. Nýr starfsmaður\n\t3. Bílayfirlit\n",
                "Veldu síðu: ")
            if choice == "1":
                choice = self.employee_menu()
            elif choice == "2":
                choice = self.new_employee()
            elif choice == "3":
                choice = self.car_menu()

    def car_menu(self):
        '''Bílayfirlit menu fyrir Kerfisstjóra'''
        choice = ""
        while choice not in HOMECOMMANDS:
            choice = self.show_menu(
                "Bílayfirlit\n\t1. Allir bílar\n\t2. Lausir bílar\n\t3. Í útleigu\n\t\
4. Nýskrá bíl\n\t5. Afskrá bíl\n", "Veldu aðgerð: ")
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass

        return choice

    def print_employee_header(self):
        '''Prentar haus fyrir starfmannayfirlit'''
        print("{:<10s}| {:<10s}| {:<10s}| {:<10s}| {:<10s}| {:<20s}".format(
            "Nafn", "Notandi", "Lykilorð", "Hlutverk", "Sími", "Heimilisfang"))
        print("-"*80)

    def print_empoloyee_list(self, employee_list):
        '''prentar lista yfir employees'''
        pass

    def employee_menu(self):
        '''Yfirlit yfir alla starfsmenn fyrirtækis,
        Möguleiki á að eyða starfsmanni'''
        choice = ""
        while choice not in HOMECOMMANDS:
            self.print_header()
            self.print_employee_header()
            # Finna leið til að prenta starfsmenn rétt
            employees_list = self.__employee_repo.get_employees()
            # self.print_employee_list(employees_list)
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
        choice = ""
        while choice not in HOMECOMMANDS:
            self.print_header()
            username = input("\tNotendanafn: ")
            password = input("\tLykilorð: ")
            name = input("\tNafn: ")
            address = input("\tHeimilisfang: ")
            phonenumber = input("\tSími: ")
            emp_type = input("\t(S)öludeild, (y)firmaður eða (k)erfisstjóri: ")
            if emp_type.lower() == "k":
                emp_type = "admin"
            elif emp_type.lower() == "y":
                emp_type = "yfirmadur"
            else:
                emp_type = "soludeild"
            an_employee = Employee(username, password, name,
                                   address, phonenumber, emp_type)
            choice = input(
                "Staðfesta nýjan notanda {} ((J)á/(N)ei): ".format(username))
            if choice.lower() == "j":
                self.__employee_service.add_employee(an_employee)
                print("\n{}\nNýr notandi hefur verið skráður!\n".format("-"*40))
                choice = "h"
            else:
                print("Action aborted!")
                choice = "h"

    def new_car(self):
        pass

    def quit(self):
        pass
