from datetime import date
HEIMSETNINGAR = ["h", "H", "s", "S"]


class SalesmanUI(object):
    def __init__(self, name):
        self.__name = name

    def print_header(self):
        '''prints header for sign-in screen'''
        # Hér þarf að laga print setninguna svo dagsetningin sé ekki lengst
        # til haegri
        print("{:40s} {:>54}".format(
            "Söludeild - notandi: {}".format(self.__name), str(date.today())))
        print(("-"*100))

    def show_menu(self, texti):
        self.print_header()
        print(texti)

        choice = input("Veldu aðgerð: ")
        # Inn í þetta vantar að prenta út það sem er fyrir neðan
        return choice

    def main_menu(self):
        # While skipunin er fkd. Maður festist í henni
        choice = ""
        while choice != HEIMSETNINGAR[2] and choice != HEIMSETNINGAR[3]:
            choice = self.show_menu(
                """ \t1. Pantanir\n\t2. Bílayfirlit
\t3. Viðskiptavinir\n\t4. Verðlisti\n""")
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
        choice = ""
        while choice not in HEIMSETNINGAR:  # Placeholder þangað til ég næ að
            # lata while loopuna virka betur
            choice = self.show_menu(
                "Pantanir\n\t1. Yfirlit pantana\n\t2. Ný pöntun")
            if choice == "1":
                choice = self.order_list_menu()
            elif choice == "2":
                # CustomerService.make_customer()
                pass
        return choice

    def order_list_menu(self):
        choice = ""
        while choice not in HEIMSETNINGAR:  # Placeholder
            choice = self.show_menu(
                """Pantanir - Yfirlit pantana\n\tSækjaupplýsingar út frá:
\t1. Kennitölu\n\t2. Pöntunarnúmeri\n\t3. Allar Pantanir""")
            if choice == "1":
                pass
            if choice == "2":
                pass
            if choice == "3":
                pass
        return choice

    def customer_menu(self):
        """Prints customer menu and follows up on commands"""
        choice = ""
        while choice not in HEIMSETNINGAR:  # Placeholder
            choice = self.show_menu(
                """Viðskiptavinir\n\t1. Leita eftir kennitölu
\t2. Fá yfirlit yfir alla viðskiptavini\n\t3. Nýr viðskipavinur""")
            if choice == "1":
                pass
            if choice == "2":
                pass
            if choice == "3":
                pass
        return choice

    def car_menu(self):
        """Prints car menu and follows up on commands"""
        choice = ""
        while choice not in HEIMSETNINGAR:  # Placeholder
            choice = self.show_menu(
                """Bílayfirlit\n\t1. Allir Bílar
\t2. Lausir Bílar\n\t3. Í útleigu""")
            if choice == "1":
                pass
            if choice == "2":
                pass
            if choice == "3":
                pass
        return choice


k1 = SalesmanUI("Gamli")
k1.main_menu()
