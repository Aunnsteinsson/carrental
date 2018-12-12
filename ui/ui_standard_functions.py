import os
from datetime import date


class UIStandard(object):
    def __init__(self, name, a_type):
        self.__name = name
        self.__a_type = a_type

    def show_menu(self, text, prompt):
        '''Prentar það menu sem notandi er staddur á.'''
        self.print_header()
        print(text)
        choice = input(prompt)
        return choice

    def print_header(self):
        '''Prentar haus á síðu sem notandi er staddur á'''
        today = date.today()
        print()
        print("{:40s}{:>32}   {}   {:%d. %b %Y}".format(
            "{} - notandi: {}".format(self.__a_type, self.__name),
            "(H)eim", "(S)krá út", today))
        print(("-"*100))

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")
