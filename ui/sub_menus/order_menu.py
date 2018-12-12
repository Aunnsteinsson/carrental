from models.order import Order
from models.car import Car
from services.orderservice import OrderService
from services.carservice import CarService
from ui.sub_menus.customer_menu import CustomerUI
from ui.ui_standard_functions import UIStandard
from datetime import date
import time
HOMECOMMANDS = ["h", "H", "s", "S"]


class OrderUI(object):
    """Klasi sem sér um viðmót Sölumanns og ferðir þar um"""

    def __init__(self, name, a_type):
        self.__name = name
        self.__a_type = a_type
        self.__order_service = OrderService()
        self.__car_service = CarService
        self.__uistandard = UIStandard(name, a_type)

    def order_menu(self):
        """Prentar pantana viðmót tekur við inputi"""
        self.__customer_menu = CustomerUI(
            self.__name, self.__a_type)  # PAssar að það sé lesið upp úr customer menu í upphafi
        choice = ""
        while choice not in HOMECOMMANDS:  # Placeholder þangað til ég næ að
            # lata while loopuna virka betur
            choice = self.__uistandard.show_menu(
                "Pantanir\n\t1. Yfirlit pantana\n\t2. Ný pöntun\n",
                "Veldu aðgerð: ")
            if choice == "1":
                choice = self.order_list_menu()
            elif choice == "2":
                choice = self.new_order_menu()
        return choice

    def order_list_menu(self):
        """Prentar innra pantana viðmót og tekur við input"""
        choice = ""
        self.__uistandard.clear_screen()
        while choice not in HOMECOMMANDS:  # Placeholder
            choice = self.__uistandard.show_menu(
                """Pantanir - Yfirlit pantana\n\nSækja upplýsingar út frá:\n\n\t\
1. Kennitölu\n\t2. Pöntunarnúmeri\n\t3. Allar Pantanir\n""", "Veldu aðgerð: ")
            if choice == "1":
                print("-"*40)
                # TODO Þurfum að geta tengt viðskiptavin við pöntun
                ssn = input("\n\tKennitala viðskiptavinar: ")
                # if setning til að athuga hvort manneskjan sé til. Ef svo er
                # þá prentast út upplýsingar um hana, annars er sótt fall til
                # að gera nýjan viðskiptavin
                customer = self.__customer_menu.get_the_customer(ssn)
                if customer:
                    print(customer)
                    order = self.__order_service.customer_orders(ssn)
                    print(order)
                else:
                    print("Enginn viðskiptavinur með þessu nafni")
                choice = input("B - til baka, H - Heim, S - Útskrá: ")
            if choice == "2":  # TODO Þurfum að gefa pöntunarnúmer
                self.get_single_order()
            if choice == "3":
                self.all_orders()
                choice = input("B - tilbaka, H - Heim, S - Útskrá: ")
        return choice

    def get_single_order(self):
        order = input("Hvaða pöntun viltu fá að sjá?")
        the_order = self.__order_service.find_order(order)
        strengur = "Pantanir - Yfirlit pantana- Pöntunarnúmar\n\Pöntun númer {}\n1. Breyta Pöntun\n2. Bakfæra pöntun\n3. Sjá upplýsingar".format(
            order)
        choice = self.__uistandard.show_menu(strengur, "Veldu aðgerð:")
        if choice == "1":
            self.change_order_menu(order, the_order)
        if choice == "2":
            self.__order_service.remove_order(order)
        if choice == "3":
            print(the_order)
            time.sleep(5)

    def change_order_menu(self, order, the_order):
        choice = self.__uistandard.show_menu(
            "Pantanir - Yfirlit pantana-\nHverju skal breyta?\n1. Tímabil\n2. Bíll\n3. Tryggingar\n4. Viðskiptavinur\n5. Afsláttur\n", "Veldu aðgerð: ")
        if choice == "1":
            begin_date = input("Nýi upphafsdagur")
            end_date = input("nýi lokadagur")
            strengur = self.__order_service(order, begin_date, end_date)
            print(strengur)
            if len(strengur) > 20:
                choice_of_car = input("Skrifaðu bílnúmers bíls")
                self.__order_service.change_car_again(choice_of_car, order)
                self.__order_service.add_dates_to_car(
                    begin_date, end_date, choice_of_car)
        if choice == "2":
            licence_plate = the_order.get_car()
            the_car = self.__car_service.show_cars(licence_plate)
            type = the_car.get_type()
            string_of_cars = self.__order_service.change_car(type, order)
            print(string)
            choice_of_car = ("Skrifaði ´bilnúmer bíls")
            listi = the_order.get_duration()
            self.__order_service.change_car_again(choice_of_car, order)
            self.__order_service.add_dates_to_car(
                listi[0], listi[-1], choice_of_car)
        if choice == "3":
            insurance = input("Viltu tryggingu? (J)á eða (N)ei")
            if insurance.lower() == "j":
                insurance = True
            else:
                insurance = False
            self.__order_service.change_insurance(order, insurance)
        if choice == "4":
            ssn = input("Hver er kennitala viðskiptavinar? ")
            customer = self.__customer_menu.get_the_customer(ssn)
            if customer:
                print(customer)
                order = self.__order_service.customer_orders(ssn)
                print(order)
            else:
                print("Enginn viðskiptavinur með þessu nafni")
        if choice == "5":
            discount = input(
                "Hvað viltu að nýji afslátturinn sé mörg prósent?")
            self.__order_service.change_discount(order, discount)

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
        begin_day = input("\tUpphafsdagur: ")
        begin_month = input("\tUpphafsmánuður")
        begin_year = input("\tUpphafsár")
        end_day = input("\tSkiladagur: ")
        end_month = input("\tSkilamánuður")
        end_year = input("\tSkilaár")
        begin_date = begin_day + "/" + begin_month + "/" + begin_year
        end_date = end_day + "/" + end_month + "/" + end_year
        list_of_days = self.__order_service.list_of_days(begin_date, end_date)
        print("\n\tFlokkar\n\t-------\n\t(J)eppi\n\t(F)ólksbíll\n\t(S)endibíll\n")
        type_of_car = input("\tFlokkur: ")
        if type_of_car == "j":
            type_list = ["jeppi"]
        elif type_of_car == "f":
            type_list = ["folksbill"]
        elif type_of_car == "s":
            type_list = ["sendibill"]
        else:
            type_list = ["sendibill", "folksbill", "jeppi"]
        availablecars = self.__order_service.find_available_cars(
            type_list, begin_date, end_date)
        print(availablecars)
        licence_plate = input("Skrifa bílnúmer: ").upper()
        order_number = self.__order_service.make_order_number()
        price = self.__order_service.price_of_rent(
            licence_plate, 0, False, begin_date, end_date)
        print("Verð án trygginga: {}".format(price))
        # Hér þarf að sækja verð
        insurance_price = self.__order_service.get_price_of_insurance()
        insurance = input(
            "\tViðbótartrygging (verð {} á dag) (J)á/(N)ei: ".format(
                insurance_price))
        if insurance.lower() == "j":
            insurance = True
        else:
            insurance = False
        format(insurance_price)
        discount = input(
            "\tSkrifaðu hversu mörg prósent afslátturinn á að vera ef einhver: ")
        total_price = self.__order_service.price_of_rent(
            licence_plate, discount, insurance, begin_date, end_date)  # hér þarð að nota aðra klasa
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
        order = Order(order_number, list_of_days, ssn,
                      licence_plate, total_price, insurance, discount)
        self.__order_service.add_dates_to_car(
            begin_date, end_date, licence_plate, order_number)

        self.__order_service.make_order(order_number, order)

        # kallar á föll og býr til klasa
        print("---------------------\nPöntun Staðfest\n")
        return "h"
