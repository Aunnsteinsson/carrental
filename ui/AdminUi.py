from datetime import date
HEIMSETNINGAR = ["h", "H", "s", "S"]


class AdminUI(object):
    def __init__(self, username):
        self.__username = username

    def print_header(self):
        '''prints header for sign-in screen'''
        print("{:40s} {:>39}".format(
            "Kerfisstjóri - notandi: {}".format(self.__username), str(
                date.today())))
        print(("-"*80))

    def show_menu(self, texti):
        self.print_header()
        print(texti)

        choice = input("Veldu síðu: ")

        return choice

    def main_menu(self):
        '''Upphafssíða fyrir kerfisstjóra'''
        choice = ""
        while choice not in HEIMSETNINGAR:
            choice = self.show_menu(
                "\n\n1. Starfsmenn\n\n\2. Nýr starfsmaður\n\n3. Bílayfirlit\n")
            if choice == 1:
                choice = self.employee_menu
            # elif choice == 2:
                # choice =  # new employee
            elif choice == 3:
                choice = self.car_menu

    def car_menu(self):
        pass

    def employee_menu(self):
        pass

    def new_employee(self):
        pass

    def quit(self):
        pass


def main():
    test = AdminUI("logigeir")
    test.main_menu()


main()
