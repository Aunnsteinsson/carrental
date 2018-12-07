from models.order import Order
from services.orderservice import OrderService
from ui.ui_standard_functions import UIStandard
HOMECOMMANDS = ["h", "H", "s", "S"]


class OrderUI(object):
    """Klasi sem sér um viðmót Sölumanns og ferðir þar um"""

    def __init__(self, name, a_type):
        self.__name = name
        self.__order_service = OrderService()
        self.__uistandard = UIStandard(name, a_type)

    def order_menu(self):
        """Prentar pantana viðmót tekur við inputi"""
        choice = ""
        while choice not in HOMECOMMANDS:  # Placeholder þangað til ég næ að
            # lata while loopuna virka betur
            choice = self.__uistandard.show_menu(
                "Pantanir\n\t1. Yfirlit pantana\n\t2. Ný pöntun", "Veldu aðgerð")
            if choice == "1":
                choice = self.order_list_menu()
            elif choice == "2":
                choice = self.new_order_menu()
        return choice

    def order_list_menu(self):
        """Prentar innra pantana viðmót og tekur við input"""
        choice = ""
        while choice not in HOMECOMMANDS:  # Placeholder
            choice = self.__uistandard.show_menu(
                """Pantanir - Yfirlit pantana\n\tSækjaupplýsingar út frá:
\t1. Kennitölu\n\t2. Pöntunarnúmeri\n\t3. Allar Pantanir""", "Veldu aðgerð")
            if choice == "1":  # TODO Þurfum að geta tengt viðskiptavin við pöntun
                pass
            if choice == "2":  # TODO Þurfum að gefa pöntunarnúmer
                pass
            if choice == "3":
                self.all_orders()
        return choice

    def all_orders(self):
        self.__uistandard.print_header()
        print("dagsetning | Pönt.nr |  Nafn  |  Kennitala  | Tegund",
              "Bílnr.  | Staða")
        print("\t", "-"*80)
        # Sæki drasl1

    def new_order_menu(self):
        self.__uistandard.print_header()
        print("Pantanir - Ný pöntun\n\tTímabil\n\t--------")
        begin_date = input("Upphafsdagsetning: ")
        end_date = input("Skiladagsetning: ")
        print("\tFlokkar\n\t-------\n\t(J)eppi\n\t(F)ólksbíll\n\t(S)endibíll\n")
        type_of_car = input("Flokkur: ")
        insurance_price = 100  # Hér þarf að sækja verð
        insurance = input(
            "Viðbótartrygging (verð {} á dag) (J)á/(N)ei: ".format(
                insurance_price))
        format(insurance_price)
        discount = input("Afsláttur(0-20%): ")
        total_price = 10000  # hér þarð að nota aðra klasa
        SSN = input("Kennitala viðskiptavinar: ")
        # if setning til að athuga hvort manneskjan sé til. Ef svo er
        # þá prentast út upplýsingar um hana, annars er sótt fall til
        # að gera nýjan viðskiptavin
        customer_name = "Siggi Gunnars"
        print("{}".format(customer_name))
        payment = input("Greiðslumáti: (D)ebit, (K)redit, (P)eningar: ")
        # self, start_date, end_date, car, insurance=False
        an_order = Order(begin_date, end_date, type_of_car, insurance)
        self.__order_service.make_order(an_order)

        # kallar á föll og býr til klasa
        print("---------------------\nPöntun Staðfest\n")
        return "h"
