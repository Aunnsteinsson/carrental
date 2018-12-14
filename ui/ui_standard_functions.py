import os
from datetime import date
HOMECOMMANDS = ["s", "h"]


class UIStandard(object):
    def __init__(self, name, a_type):
        self.__name = name
        self.__a_type = a_type

    def show_menu(self, text_of_location, text, prompt):
        """Prentar það menu sem notandi er staddur á."""
        self.print_header()
        self.location_header(text_of_location)
        print(text)
        choice = input(prompt)
        return choice

    def print_header(self):
        """Prentar haus á síðu sem notandi er staddur á"""
        today = date.today()
        print()
        print("{:40s}{:>32}   {}   {:%d. %b %Y}".format(
            "{} - notandi: {}".format(self.__a_type, self.__name),
            "(H)eim", "(S)krá út", today))
        self.line_seperator()

    def line_seperator(self):
        """Fall sem prentar 100 bandstrik, notað til að aðskilja línur
         í viðmóti."""
        print("-"*100)

    def clear_screen(self):
        """Hreinsar skjá í terminal, virkar fyrir Windows og macOS"""
        os.system("cls" if os.name == "nt" else "clear")

    def back_input(self):
        """Fall sem kallað er á þegar hægt er að fara til baka um síðu"""
        choice = ""
        while choice.lower() != "b" and choice.lower() not in HOMECOMMANDS:
            choice = input(
                "Veldu aðgerð (H), (S) eða (B)akka: ")
        return choice

    def location_header(self, text_to_print):
        print()
        print(text_to_print)
        print()
        self.line_seperator()

    def check_if_date_is_valid(self, begin_day, begin_month, begin_year,
                               end_day, end_month, end_year):
        try:
            begining_date = date(
                int(begin_year), int(begin_month), int(begin_day))
            ending_date = date(
                int(end_year), int(end_month), int(end_day))
            if begining_date < ending_date:
                return ""
            else:
                return "Ekki hægt að leiga bíl í minna en einn dag"
        except ValueError:
            return "Vinsamlegast skráðu daga og mánuði á heiltölu á \
forminu 1,2,3... og ár á forminu 2018, 2019... "
