from models.order import Order
from services.orderservice import OrderService
from ui.sub_menus.customer_menu import CustomerUI
from ui.ui_standard_functions import UIStandard
HOMECOMMANDS = ["h", "H", "s", "S"]


class OrderUI(object):
    """Klasi sem sér um viðmót Sölumanns og ferðir þar um"""

    def __init__(self, name, a_type):
        self.__name = name
        self.__a_type = a_type
        self.__order_service = OrderService()
        self.__uistandard = UIStandard(name, a_type)

    def order_menu(self):
        """Prentar pantana viðmót tekur við inputi"""
        self.__customer_menu = CustomerUI(
            self.__name, self.__a_type)  # PAssar að það sé lesið upp úr customer menu í upphafi
        choice = ""
        while choice not in HOMECOMMANDS:  # Placeholder þangað til ég næ að
            # lata while loopuna virka betur
            choice = self.__uistandard.show_menu(
                "Pantanir\n\t1. Yfirlit pantana\n\t2. Ný pöntun\n", "Veldu aðgerð: ")
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
\t1. Kennitölu\n\t2. Pöntunarnúmeri\n\t3. Allar Pantanir\n""", "Veldu aðgerð: ")
            if choice == "1":
                # TODO Þurfum að geta tengt viðskiptavin við pöntun
                ssn = input("\tKennitala viðskiptavinar: ")
                strengur = self.__order_service.customer_orders(ssn)
                print(strengur)
                # if setning til að athuga hvort manneskjan sé til. Ef svo er
                # þá prentast út upplýsingar um hana, annars er sótt fall til
                # að gera nýjan viðskiptavin
                """customer = self.__customer_menu.get_the_customer(ssn)
                if customer:
                    print(customer)
                else:
                    print("Enginn viðskiptavinur með þessu nafni")
                choice = input("B - tilbaka, H - Heim, S - Útskrá: ")"""
            if choice == "2":  # TODO Þurfum að gefa pöntunarnúmer
                pass
            if choice == "3":
                self.all_orders()
                choice = input("B - tilbaka, H - Heim, S - Útskrá: ")
        return choice

    def all_orders(self):
        self.__uistandard.print_header()
        print("Pantanir - Yfirlit pantana - Allar pantanir")
        print("\t {:11}| {:14}| {:25}| {:11}| {:10}| {:9}| {:10}".format(
            "Dagsetning", "Pöntunarnúmer", "Nafn", "Kennitala",
            "Tegund", "Bílnúmer", "Staða"))
        print("\t", "-"*100)
        string = self.__order_service.show_orders()
        print(string)
        # Sæki drasl1

    def new_order_menu(self):
        self.__uistandard.print_header()
        print("Pantanir - Ný pöntun\n\tTímabil\n\t--------")
        begin_date = input("\tUpphafsdagsetning: ")
        end_date = input("\tSkiladagsetning: ")
        print("\n\tFlokkar\n\t-------\n\t(J)eppi\n\t(F)ólksbíll\n\t(S)endibíll\n")
        type_of_car = input("\tFlokkur: ")
        insurance_price = 100  # Hér þarf að sækja verð
        insurance = input(
            "\tViðbótartrygging (verð {} á dag) (J)á/(N)ei: ".format(
                insurance_price))
        if insurance == "j" or insurance == "J":
            insurance = True
        else:
            insurance = False
        format(insurance_price)
        discount = input("\tAfsláttur(0-20%): ")
        total_price = 10000  # hér þarð að nota aðra klasa
        ssn = input("\tKennitala viðskiptavinar: ")
        # if setning til að athuga hvort manneskjan sé til. Ef svo er
        # þá prentast út upplýsingar um hana, annars er sótt fall til
        # að gera nýjan viðskiptavin
        customer = self.__customer_menu.get_the_customer(ssn)
        if customer:
            customer_name = customer.get_name()
        else:
            print(
                "Viðskiptavinur ekki skráður í kerfið. Vinsamlegast skráðu nauðsynlegar upplýsingar.")
            self.__customer_menu.new_customer_menu()
            customer = self.__customer_menu.get_the_customer(ssn)
            customer_name = customer.get_name()

        print("\n\tViðskiptavinur: {}".format(customer_name))
        payment = input("\tGreiðslumáti: (D)ebit, (K)redit, (P)eningar: ")
        order_number = self.__order_service.make_order_number()
        order = Order(order_number, begin_date, end_date, "viðskiptavinur",
                      "kennitala", type_of_car, "1kkk", "laus", insurance)

        self.__order_service.make_order(order, order_number)

        # kallar á föll og býr til klasa
        print("---------------------\nPöntun Staðfest\n")
        return "h"
