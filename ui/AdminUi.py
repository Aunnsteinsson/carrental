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
            if choice == 1:
                choice = self.employee_menu
            # elif choice == 2:
                # choice =  # new employee
            elif choice == 3:
                choice = self.car_menu

    def car_menu(self):
        '''Bílayfirlit fyrir Kerfisstjóra'''
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

    def employee_menu(self):
        '''Yfirlit yfir alla starfsmenn fyrirtækis,
        Möguleiki á að eyða starfsmanni'''
        choice = ""
        while choice not in HOMECOMMANDS:
            self.print_header()
            self.print_employee_header()
            # Finna leið til að prenta starfsmenn rétt
            employees_list = self.__employee_repo.get_employees()
            print(employees_list)
            # aðgerðir tengdar starfsmanni (eyða, breyta)
            print("\nEyða starfsmanni?\n{}".format("-"*40))
            print("1. Eyða\n2. Breyta\n")
            choice = input("Veldu aðgerð: ")
            if choice == "1":
                print("\nEyða\n{}".format("-"*40))
                # empl = input("Notandanafn: ")
                choice = input("Ertu viss? ((J)á/(N)ei): ")
                if choice.lower() == "j":
                    # Hér þarf að tengja við remove_employee í emprepo
                    print("{}\nNotanda hefur verið eytt!\n".format("-"*40))
                elif choice.lower() == "n":
                    print("{}\nNotanda hefur ekki verið eytt!\n".format(
                        "-"*40))
            elif choice == "2":
                # hér þarf að tengja við change_info í emprepo
                pass

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
            self.__employee_service.add_employee(an_employee)

    def quit(self):
        pass
