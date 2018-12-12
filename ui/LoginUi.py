import sys
import time
import webbrowser
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
    #     print()
    #     print("{:72}        __-------__".format(" "))
    #     print("{:72}      / _---------_ \\".format(" "))
    #     print("{:72}     / /           \\ \\".format(" "))
    #     print("{:72}     | |           | |".format(" "))
    #     print((" "*16), " --,--         .     ,--.         .      ."
    #           "                  |_|___________|_|")
    #     print((" "*16), "   | . ,-. ,-. |     |__/ ,-. ,-. |- ,-. |"
    #           "              /-\\|                 |/-\\")
    #     print((" "*16), "   | | ,-| `-. |     | \\  |-' | | |  ,-| "
    #           "|             | _ |\\       0       /| _ |")
    #     print((" "*16), "   ' | `-^ `-' `'    '  ` `-' ' ' `' `-^ `'"
    #           "            |(_)| \\      !      / |(_)|")
    #     print((" "*16), "    `'                                     "
    #           "            |___|__\\_____!_____/__|___|")
    #     print("{:72}[_________|TJASL|_________]".format(" "))
    #     print("{:72} ||||     ~~~~~~~     ||||".format(" "))
    #     print("{:72} `--'                 `--'".format(" "))
        print(("-"*100))
        print("{:40s}{:>20}    {}{:>15}".format("Innskráning",
                                                "Senda inn (a)thugasemd",
                                                "(L)oka kerfi",
                                                str(date.today())))
        print(("-"*100))

    def tjasl_rental_header(self):
        print()
        print("    ______    __  ______  ______  __           ______  ______  __   __  ______  ______  __        ")
        print("   /\\__  _\\  /\\ \\/\\  __ \\/\\  ___\\/\\ \\         /\\  == \\/\\  ___\\/\\ \"-.\\ \\/\\__  _\\/\\  __ \\/\\ \\         ")
        print("   \\/_/\\ \\/ _\\_\\ \\ \\  __ \\ \\___  \\ \\ \\____    \\ \\  __<\\ \\  __\\\\ \\ \\-.  \\/_/\\ \\/\\ \\  __ \\ \\ \\____    ")
        print("      \\ \\_\\/\\_____\\ \\_\\ \\_\\/\\_____\\ \\_____\\    \\ \\_\\ \\_\\ \\_____\\ \\_\\\\\"\\_\\ \\ \\_\\ \\ \\_\\ \\_\\ \\_____\\   ")
        print("       \\/_/\\/_____/\\/_/\\/_/\\/_____/\\/_____/     \\/_/ /_/\\/_____/\\/_/ \\/_/  \\/_/  \\/_/\\/_/\\/_____/ ")

    def sports_car(self):
        print()
        print((" "*10), '                                   _._')
        print((" "*10), '                              _.-="_-         _')
        print((" "*10), '                         _.-="   _-          | ||"""""""---.\
_______     __..')
        print((" "*10), '             ___.===""""-.______-,,,,,,,,,,,,`-""----" """""\
       """""  __')
        print((" "*10), '      __.--""     __        ,""                  o \\         \
  __        z__|')
        print((" "*10), ' __-""=======.--""  ""--.=================================.--""\
  ""--.=======:')
        print((" "*10), '7       LwL : /        \\ : |========================|    : /  \
      \\ :  LwL :')
        print((" "*10), 'V___________:|          |: |========================|    :|    \
      |:   _-"')
        print((" "*10), ' V__________: \\        / :_|=======================/_____: \\    \
    / :__-"')
        print((" "*10), '            "  ""____""                                  ""  \
""____""')

    def ask_for_username_password(self):
        '''
         Spyr starfsmann um notandanafn og lykilorð
        '''
        username = input("Notendanafn: ")
        if username.lower() == "l":
            print("Loka kerfi...")
            time.sleep(2)
            sys.exit(0)
        elif username.lower() == "a":
            print("Fer á heimasíðu og loka kerfi...")
            time.sleep(2)
            webbrowser.open(
                "https://github.com/Aunnsteinsson/carrental_issue_repo\
/issues/new")
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
        self.tjasl_rental_header()
        self.sports_car()
        self.print_header()
        username, password = self.ask_for_username_password()
        return self.check_employee_type(username, password)
