import time
import webbrowser
from models.employee import Employee
from services.employeeservice import EmployeeService
from ui.ui_standard_functions import UIStandard
# logi

HOMECOMMANDS = ["h", "s"]
VALIDJOB = ["k", "s", "y"]


class EmployeeUI(object):
    '''
    Klasi sem sér um starfsmenn fyrir kerfisstjóra og yfirmann.
    Þá hefur yfirmaður aðgang að yfirliti yfir starfsmenn en kerfisstjóri
    hefur hefur heimild til að breyta og eyða starfsmanni. Einnig prentast
    lykilorð í yfirliti hjá kerfisstjóra.
    '''

    def __init__(self, username, job_title):
        self.__username = username
        self.__employee_service = EmployeeService()
        self.__uistandard = UIStandard(username, job_title)

    def print_employee_header(self):
        '''
        Prentar haus fyrir starfmannayfirlit kerfisstjóra þar sem hann sér
        einnig lykilorð
        '''
        print("{:<100}".format("\nStarfsmenn - Starfsmannayfirlit kerfisstjóra\n"))
        self.__uistandard.line_seperator()
        print("{:^10s}| {:^10s}| {:^25s}| {:^25s}| {:^10s}| {:^12s}".format(
            "Notandi", "Lykilorð", "Nafn", "Heimilisfang", "Sími", "Hlutverk"))
        self.__uistandard.line_seperator()

    def print_employee_header_boss(self):
        '''
        Prentar haus fyrir starfmannayfirlit yfirmanns
        '''
        print("Starfsmenn - Starfsmannayfirlit yfirmanns")
        print("{:^25s}| {:^10s}| {:^25s}| {:^10s}| {:^12s}".format(
            "Nafn", "Notandi", "Heimilisfang", "Sími", "Hlutverk"))
        self.__uistandard.line_seperator()

    def employee_menu(self):
        '''
        Yfirlit yfir alla starfsmenn fyrirtækis,
        Möguleiki á að eyða og breyta starfsmanni
        '''
        self.__uistandard.clear_screen()
        choice = ""
        get_pass = 1
        while choice.lower() not in HOMECOMMANDS:
            self.__uistandard.clear_screen()
            self.__uistandard.print_header()
            self.print_employee_header()
            # Prentar lista yfir starfsmenn fyrir admin (með passwordi)
            employees_list_string = self.__employee_service.get_employees(
                get_pass)
            print(employees_list_string)
            # aðgerðir tengdar starfsmanni (eyða, breyta)
            print("\nMögulegar aðgerðir\n{}".format("-"*40))
            print("1. Eyða\n2. Breyta\n")
            choice = input("Veldu aðgerð: ")
            if choice == "1":
                # Eyða employee
                self.delete_employee(employees_list_string)
            elif choice == "2":
                # Breyta einhverju við employee
                self.edit_employee()
            return choice

    def delete_employee(self, employees_list_string):
        '''
        Fall sem sér um eyðingu starfsmanns
        '''
        print("\nEyða\n{}".format("-"*40))
        username = input("Notandanafn: ")
        if username.lower() not in HOMECOMMANDS:
            # athugar hvort notandi sé í kerfi
            check = self.__employee_service.check_if_valid(username)
            if check:
                choice = input("Ertu viss? ((J)á/(N)ei): ")
                if choice.lower() == "j":
                    self.__employee_service.remove_employee(username)
                    print("{}\nNotanda hefur verið eytt!\n".format("-"*40))
                    self.save_employees()
                elif choice.lower() == "n":
                    print("{}\nHætt við aðgerð!\n".format(
                        "-"*40))
                time.sleep(2)
            else:
                print("\nNotandanafn ekki á skrá.")
                time.sleep(2)

    def edit_employee(self):
        '''
        Fall sem sér um breytingu á starfsmanni. Hægt er að breyta lykilorði,
        nafni, heimilisfangi, síma.
        '''
        print("\nBreyta\n{}".format("-"*40))
        username = input("Notandanafn: ")
        if username.lower() not in HOMECOMMANDS:
            # athugar hvort notandi sé í kerfi
            check = self.__employee_service.check_if_valid(username)
            if check:
                print("Hverju skal breyta?\n{}".format("-"*40))
                print("\t1. Lykilorð\n\t2. Nafn\n\t3. Heimilisfang\n\t4. Sími\n")
                choice = ""
                new_value = ""
                while choice.lower() not in HOMECOMMANDS:
                    choice = input("Veldu aðgerð: ")
                    if choice == "1":
                        new_value10 = input("Nýtt lykilorð(10*): ")
                    elif choice == "2":
                        new_value25 = input("Nýtt nafn(25*): ")
                    elif choice == "3":
                        new_value25 = input("Nýtt heimilisfang(25*): ")
                    elif choice == "4":
                        try:
                            new_value10 = int(input("Nýr sími(10*): "))
                        except ValueError:
                            print("Passaðu að hafa símanúmer einungis \
tölustafi - fer til baka")
                            time.sleep(2)
                            return choice
                    else:
                        print(choice, "er ekki valmöguleiki, - fer til baka")
                        time.sleep(2)
                        return choice
                    if new_value10 > 11 or new_value25 > 26:
                        print("Passaðu að hafa innsetningu ekki of langa! - fer til \
baka")
                        time.sleep(2)
                        return choice
                    else:
                        self.__employee_service.change_employee(
                            username, choice, new_value)
                        self.save_employees()
                        print("\nNotanda hefur verið breytt")

                        time.sleep(2)
                        return choice
            else:
                print("\nNotandanafn ekki á skrá.")
                time.sleep(2)

    def new_employee(self):
        '''
        Fall sem sér um nýskráningarsíðu starfsmanns.
        '''
        self.__uistandard.clear_screen()
        choice = ""
        while choice.lower() not in HOMECOMMANDS:
            self.__uistandard.print_header()
            print("\t(hámarkslengd*)")
            username = input("\tNotendanafn(10*): ")
            password = input("\tLykilorð(10*): ")
            name = input("\tNafn(25*): ")
            address = input("\tHeimilisfang(25*): ")
            phonenumber = input("\tSími(10*): ")
            phonenumber = self.__employee_service.check_phone(phonenumber)
            if phonenumber == "5812345":
                webbrowser.open("https://www.dominos.is")
            emp_type = ""
            while emp_type.lower() not in VALIDJOB:
                emp_type = input(
                    "\t(S)öludeild, (y)firmaður eða (k)erfisstjóri: ")
            if emp_type.lower() == "k":
                emp_type = "admin"
            elif emp_type.lower() == "y":
                emp_type = "yfirmadur"
            else:
                emp_type = "soludeild"

            if (len(username) > 10 or len(password) > 10 or len(name) > 25 or
                    len(address) > 25 or len(phonenumber) > 10):
                print("\n\tPassaðu að hafa innsetningu á notendanafni, lykilorði\
 og síma ekki lengri en 10 stafi \n\tog nafn og heimilisfang ekki lengra en 25\
 stafi - fer á upphafssíðu!")
                time.sleep(8)
                return choice

            else:
                choice = input(
                    "\tStaðfesta nýjan notanda {} ((J)á/(N)ei): ".format(username))
                if choice.lower() == "j":
                    self.__employee_service.add_employee(
                        username, password, name, address, phonenumber, emp_type)
                    print("\n{}\nNýr notandi hefur verið skráður!\n".format(
                        "-"*40))
                    self.save_employees()
                else:
                    print("\nHætt við aðgerð - Fer á upphafssíðu!")
                time.sleep(2)
                return choice

    def show_employees(self):
        """
        Prentar út alla starfsmenn í kerfi fyrir yfirmann án lykilorðs
        """
        self.__uistandard.clear_screen()
        self.__uistandard.print_header()
        self.print_employee_header_boss()
        employees_list_string = self.__employee_service.get_employees()
        print(employees_list_string)
        choice = ""
        print("\nMögulegar aðgerðir\n{}".format("-"*25))
        print("1. Fara til baka\n")
        while choice.lower() not in HOMECOMMANDS:
            choice = input("\nVeldu aðgerð: ")
        return choice

    def save_employees(self):
        self.__employee_service.save_employees()
