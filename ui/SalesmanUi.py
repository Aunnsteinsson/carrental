from datetime import date


class SalesmanUI(object):
    def __init__(self, name):
        self.__name = name

    def print_header(self):
        '''prints header for sign-in screen'''
        # Hér þarf að laga print setninguna svo dagsetningin sé ekki lengst til hægri
        right_justified = 65-len(self.__name)
        print("{} {:>{}}".format(
            "Söludeild - notandi: {}".format(self.__name), str(date.today()), right_justified))
        print(("-"*80))

    def show_menu(self, texti):
        self.print_header()
        print(texti)

        choice = input("Veldu síðu: ")
        # Inn í þetta vantar að prenta út það sem er fyrir neðan
        return choice

    def main_menu(self):
        # While skipunin er fkd. Maður festist í henni
        choice = ""
        while choice.lower() != "s":
            choice = self.show_menu(
                "\t1. Pantanir\n\t2. Bílayfirlit\n\t3. Viðskiptavinir\n\t4. Verðlisti\n")
            if choice == "1":
                choice = self.order_menu()
            elif choice == "2":
                choice = self.car_menu()
            elif choice == "3":
                self.customer_menu()
            elif choice == "4":
                pass
                # ég hef ekki hugmynd um hvernig við ætlum að sýna verðlistann

    def order_menu(self):
        """Prints order menu and follows up on commands"""
        while 1 > 0:
            choice = self.show_menu(
                "Pantanir\n\n1. Yfirlit pantana\n2. Ný pöntun")
            if choice == "1":
                # CustomerService.show_list()
                pass
            elif choice == "2":
                # CustomerService.make_customer()
                pass
            elif choice == "h":
                return choice
            elif choice == "s":
                return choice

    def customer_menu(self):
        """Prints customer menu and follows up on commands"""
        pass

    def car_menu(self):
        """Prints car menu and follows up on commands"""

    def quit(self):
        # Hér þarf að ákveða hvort þetta sé við að hætta í login fallinu
        # og þá væri þetta fall tilgangslaust eða hvort að við séum að
        # að kalla á login skjáinn
        pass


k1 = SalesmanUI("gamli")
k1.main_menu()
