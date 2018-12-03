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

    def show_menu(self):
        self.print_header()
        print("""1. Pantanir
        2. Fá yfirlit yfir alla viðskiptavini
        3. Viðskiptavinir
        4. Verðlisti\n""")

        choice = input("Veldur síðu: ")
        # Inn í þetta vantar að prenta út það sem er fyrir neðan
        return choice

    def main_menu(self):
        # While skipunin er fkd. Maður festist í henni
        choice = ""
        while choice.lower != "s":
            choice = self.show_menu()
            # Hér vantar svo tengingar í hin viðmótin og að prenta verðlista

    def car_menu(self):
        """Prints car menu and follows up on commands"""
        pass

    def customer_menu(self):
        """Prints customer menu and follows up on commands"""
        pass

    def order_menu(self):
        """Prints order menu and follows up on commands"""

    def quit(self):
        # Hér þarf að ákveða hvort þetta sé við að hætta í login fallinu
        # og þá væri þetta fall tilgangslaust eða hvort að við séum að
        # að kalla á login skjáinn
        pass


k1 = SalesmanUI("gamli")
k1.main_menu()
