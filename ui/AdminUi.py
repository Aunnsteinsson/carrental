from ui.sub_menus.car_menu import CarUI
from ui.sub_menus.employee_menu import EmployeeUI
from ui.ui_standard_functions import UIStandard


HOMECOMMANDS = ["h", "s"]


class AdminUI(object):
    '''
    Klasi fyrir viðmót kerfisstjóra
    '''

    def __init__(self, username, emp_type):
        self.__username = username
        self.__car_ui = CarUI(self.__username, emp_type)
        self.__employee_ui = EmployeeUI(self.__username, emp_type)
        self.__uistandard = UIStandard(self.__username, emp_type)

    def main_menu(self):
        '''Upphafssíða fyrir kerfisstjóra'''
        choice = ""
        while choice.lower() != HOMECOMMANDS[1]:
            self.__uistandard.clear_screen()
            choice = self.__uistandard.show_menu("{:^100}".format("KERFISSTJÓRI"), "\t1. Starfsmenn\n\t2. Nýr starfsmaður\n\t3. Bílayfirlit\n", "Veldu síðu: ")
            if choice == "1":
                choice = self.__employee_ui.employee_menu()
            elif choice == "2":
                choice = self.__employee_ui.new_employee()
            elif choice == "3":
                choice = self.__car_ui.car_menu_admin()

    def quit(self):
        pass
# logi
