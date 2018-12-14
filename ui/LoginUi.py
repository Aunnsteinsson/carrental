import sys
import os
import time
import webbrowser
from repositories.employeerepo import EmployeeRepo
from datetime import date
from getpass import getpass


class LoginUI(object):
    def __init__(self):
        self.__employee_repo = EmployeeRepo()

    def print_header(self):
        '''Prentar haus fyrir innskráningu'''
        today = date.today()
        print(("-"*100))
        print("{:40s}{:>27}   {}     \
{:%d. %b %Y}".format("Innskráning",
                     "Senda inn (a)thugasemd",
                     "(L)oka kerfi",
                     today))
        print(("-"*100))

    def tjasl_rental_header(self):
        '''Prentar Tjasl rental í
         skrautskrift með stórum stöfum'''
        print()
        print("    ______    __  ______  ______  __           ______  ______  \
__   __  ______  ______  __        ")
        print("   /\\__  _\\  /\\ \\/\\  __ \\/\\  ___\\/\\ \\         /\\  == \
\\/\\  ___\\/\\ \"-.\\ \\/\\__  _\\/\\  __ \\/\\ \\         ")
        print("   \\/_/\\ \\/ _\\_\\ \\ \\  __ \\ \\___  \\ \\ \\____    \\ \\ \
 __<\\ \\  __\\\\ \\ \\-.  \\/_/\\ \\/\\ \\  __ \\ \\ \\____    ")
        print("      \\ \\_\\/\\_____\\ \\_\\ \\_\\/\\_____\\ \\_____\\    \\ \
\\_\\ \\_\\ \\_____\\ \\_\\\\\"\\_\\ \\ \\_\\ \\ \\_\\ \\_\\ \\_____\\   ")
        print("       \\/_/\\/_____/\\/_/\\/_/\\/_____/\\/_____/     \\/_/ /_/\
\\/_____/\\/_/ \\/_/  \\/_/  \\/_/\\/_/\\/_____/ ")

    def ask_for_username_password(self):
        '''Spyr starfsmann um notandanafn og lykilorð'''
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
        elif username.lower() == "lexmachine":
            self.easter_egg()
        else:
            password = getpass(prompt="Lykilorð: ")
            return username, password

    def check_employee_type(self, username, password):
        '''Kíkir hvort notendanafnið sé í employee.csv
         og hvort það passi við lykilorðið, það skilar síðan
         hlutverki og notendanafni'''
        employee_dict = self.__employee_repo.get_employees()
        for employee, value in employee_dict.items():
            if username == employee:
                value = employee_dict[username].__repr__(1)
                value_list = value.split(",")
                if password == value_list[1]:
                    return value_list[5], username

    def easter_egg(self):
        '''Shhhhh'''
        for _ in range(4):
            os.system("cls" if os.name == "nt" else "clear")
            print("\tEASTER", end="")
            time.sleep(0.2)
            print("\tEGG")
            time.sleep(0.2)
        print("")
        print("                                      TJASLTJAS")
        print("                                  LTJASLTJASLTJASLT")
        print("                              JASLTJASLTJASLTJASLTJASL")
        print("                      TJASLTJASLTJASL           TJASLTJA")
        print("                   SLTJASLTJASLT                  JASLTJA")
        print("                 SLTJASLTJASLTJA                   SLTJAS")
        print("                 LTJASLTJASLTJASL                   TJASL")
        print("                 TJASLTJASLT JASLTJ    ASLTJASLTJA  SLTJA")
        print("                 SLTJASLTJASLTJASLTJ ASLTJASLTJASLTJ ASLT")
        print("                 JASLTJASLTJASLTJA  SLTJASLTJASLTJASLTJAS")
        print("                LTJAS  LTJASLTJASL  TJASLTJASLTJASLTJASLT")
        print("               JASLTJASLTJASLTJASLT JASLTJASLTJ ASLTJASLT")
        print("              JASLTJASLTJASLTJASL   TJASLTJASLTJASLTJASLT")
        print("             JASLTJASLTJASLTJASLTJASLTJASLTJASLTJ  ASLTJ")
        print("            ASLTJ          ASLTJASLTJASLTJASL     TJASLT")
        print("           JASLT                      JASLTJA     SLTJAS")
        print("          LTJASL                                 TJASLT")
        print("         JASLTJ                                 ASLTJA")
        print("        SLTJAS                                  LTJASL")
        print("        TJASL                      TJAS        LTJASL")
        print("        TJAS                      LTJAS LTJ   ASLTJA")
        print("        SLTJ                      ASLTJASLTJ  ASLTJ            \
             ASLTJASLT")
        print("       JASLT                      JASLTJASL  TJASL             \
           TJASLTJASLTJ")
        print("       ASLTJ                     ASLTJASLTJ ASLTJ               \
        ASLTJA    SLTJ")
        print("       ASLTJ                     ASLTJASLT  JASLT               \
      JASLTJA    SLTJA")
        print("       SLTJA                    SLTJASLTJ  ASLTJA               \
    SLTJASL     TJASL")
        print("       TJASL                    TJASLTJA   SLTJASLTJASLTJASLTJA\
   SLTJASL     TJASL")
        print("        TJAS                   LTJASLTJ    ASLTJASLTJASLTJASLTJA\
SLTJASL      TJASL")
        print("        TJAS                   LTJASLT     JASLT   JASLT   JASL\
TJASLT      JASLTJ")
        print("        ASLT                  JASLTJAS      LTJ   ASLTJASLTJASL\
TJAS      LTJASL")
        print(
            "        TJASL               TJASL TJASL         TJASLTJASLTJASLTJ\
    A     SLTJASL")
        print("         TJAS             LTJAS  LTJASLT         JASLTJASLTJASL\
TJASL   TJASLTJA")
        print("         SLTJA            SLTJASLTJASLTJ                     ASLT\
JASL    TJASLTJAS")
        print("          LTJAS            LTJASLTJASLT              JASL       \
TJASLT  JASL TJASL")
        print("          TJASLT              JASL                   TJAS        \
LTJASL  TJASLTJA")
        print("           SLTJAS                                LTJ              \
ASLTJ    ASLT")
        print("            JASLTJAS                            LTJA             \
 SLTJA     SLTJ")
        print("               ASLTJAS                          LTJA             \
 SLTJASLTJASLTJ")
        print("     ASL        TJASLTJASL                       TJAS           L\
TJASLTJASLTJAS")
        print("    LTJASLT    JASLTJASLTJASLTJA                  SLT        \
 JASLTJA    S")
        print("    LTJASLTJASLTJA SLTJASLTJASLTJASLTJAS           LTJA   \
 SLTJASL")
        print("    TJAS LTJASLTJASLTJA    SLTJASLTJASLTJA SLTJASLTJ\
ASLTJASLTJAS")
        print("     LTJA  SLTJASLTJA         SLTJASLTJAS LTJASLTJASLTJ\
ASLTJA")
        print("      SLTJ   ASLTJA         SLTJASLTJASL TJASL TJASLTJASLT")
        print("       JASLTJASLT           JASLTJASLTJ  ASLT")
        print("        JASLTJA              SLTJASLT   JASL")
        print("          TJA                SLTJAS    LTJA")
        print("                              SLTJAS  LTJA")
        print("                               SLTJASLTJA")
        print("                                 SLTJASL")
        time.sleep(5)
        sys.exit(0)

    def main_menu(self):
        '''Þetta fall kallar í öll innri föllin og skilar
         notendanafni og hluthverki starfsmanns'''
        self.tjasl_rental_header()
        self.print_header()
        username, password = self.ask_for_username_password()
        return self.check_employee_type(username, password)
