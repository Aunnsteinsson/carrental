from datetime import date
from getpass import getpass
import csv


class LoginUI(object):
    def __init__(self):
        pass

    def print_header(self):
        '''
         Prentar haus fyrir innskráningu
        '''
        print("{:40s} {:>55}".format("Innskráning", str(date.today())))
        print(("-"*100))

    def ask_for_username_password(self):
        '''
         Spyr starfsmann um notandanafn og lykilorð
        '''
        username = input("Notendanafn: ")
        password = getpass(prompt="Lykilorð: ")
        return username, password

    def check_employee_type(self, username, password):
        '''
         Kíkir hvort notendanafnið sé í employee.csv
         og hvort það passi við lykilorðið, það skilar síðan
         hlutverki og notendanafni
        '''
        with open("./data/employees.csv", "r") as employees_file:
            csv_reader = csv.reader(employees_file)
            next(csv_reader)
            for employee in csv_reader:
                if username == employee[0]:
                    if password == employee[1]:
                        return employee[5]

    def main_menu(self):
        '''
         Þetta fall kallar í öll innri föllin og skilar
         notendanafni og hluthverki starfsmanns
        '''
        self.print_header()
        username, password = self.ask_for_username_password()
        return(self.check_employee_type(username, password))
