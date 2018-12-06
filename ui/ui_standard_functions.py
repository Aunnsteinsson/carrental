from datetime import date


class UIStandard(object):
    def __init__(self, name):
        self.__name = name

    def print_header(self):
        '''prentar haus á síðum notanda'''
        # Hér þarf að laga print setninguna svo dagsetningin sé ekki lengst
        # til haegri
        print("{:40s} {:>54}".format(
            "Söludeild - notandi: {}".format(self.__name), str(date.today())))
        print(("-"*100))

    def show_menu(self, texti):
        self.print_header()
        print(texti)

        choice = input("Veldu aðgerð: ")
        # Inn í þetta Sendibílartar að prenta út það sem er fyrir neðan
        return choice
