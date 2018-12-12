import sys
from repositories.employeerepo import EmployeeRepo
from datetime import date
from getpass import getpass


class LoginUI(object):
    def __init__(self):
        self.__employee_repo = EmployeeRepo()

    def print_header(self):
        '''
         Prentar haus fyrir innskráningu
        '''
        print("{:40s}{:>40}{:>15}".format(
            "Innskráning", "(L)oka kerfi", str(date.today())))
        print(("-"*100))

    def ask_for_username_password(self):
        '''
         Spyr starfsmann um notandanafn og lykilorð
        '''
        username = input("Notendanafn: ")
        if username.lower() == "l":
            sys.exit(0)
        else:
            password = getpass(prompt="Lykilorð: ")
            return username, password

    def check_employee_type(self, username, password):
        '''
         Kíkir hvort notendanafnið sé í employee.csv
         og hvort það passi við lykilorðið, það skilar síðan
         hlutverki og notendanafni
        '''
        employee_dict = self.__employee_repo.get_employees()
        for employee, value in employee_dict.items():
            if username == employee:
                value = employee_dict[username].__repr__(1)
                value_list = value.split(",")
                if password == value_list[1]:
                    return value_list[5], username

    def main_menu(self):
        '''
         Þetta fall kallar í öll innri föllin og skilar
         notendanafni og hluthverki starfsmanns
        '''
        self.print_header()
        username, password = self.ask_for_username_password()
        return self.check_employee_type(username, password)
