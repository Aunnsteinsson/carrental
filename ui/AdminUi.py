import os
from ui.sub_menus.car_menu import CarUI
from ui.sub_menus.employee_menu import EmployeeUI
from ui.ui_standard_functions import UIStandard
from services.employeeservice import EmployeeService


HOMECOMMANDS = ["h", "H", "s", "S"]


class AdminUI(object):
    '''
    Klasi fyrir viðmót kerfisstjóra
    '''

    def __init__(self, username):
        self.__username = username
        self.__car_ui = CarUI(self.__username, "Kerfisstjóri")
        self.__employee_ui = EmployeeUI(self.__username, "Kerfisstjóri")
        self.__uistandard = UIStandard(self.__username, "Kerfisstjóri")
        self.__employee_service = EmployeeService()

    def main_menu(self):
        '''Upphafssíða fyrir kerfisstjóra'''
        choice = ""
        while choice not in HOMECOMMANDS:
            os.system('cls')
            choice = self.__uistandard.show_menu("\n\t1. Starfsmenn\n\t2. Nýr starfsmaður\n\t3. Bílayfirlit\n\t4. Save_employees\n",
                                                 "Veldu síðu: ")
            if choice == "1":
                choice = self.__employee_ui.employee_menu()
            elif choice == "2":
                choice = self.__employee_ui.new_employee()
            elif choice == "3":
                choice = self.__car_ui.car_menu_admin()
            elif choice == "4":
                choice = self.save_employees()

    def save_employees(self):
        save = input("Vista breytingar? ((J)á/(N)ei) ")
        if save.lower() == 'j':
            self.__employee_service.save_employees()

    def quit(self):
        pass
# logi
