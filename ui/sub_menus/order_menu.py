from models.order import Order
from models.car import Car
from services.orderservice import OrderService
from services.carservice import CarService
from ui.sub_menus.customer_menu import CustomerUI
from ui.ui_standard_functions import UIStandard
from datetime import datetime
from datetime import date
import time
HOMECOMMANDS = ["h", "H", "s", "S"]


class OrderUI(object):
    """Klasi sem sér um viðmót Sölumanns og ferðir þar um"""

    def __init__(self, name, a_type):
        self.__name = name
        self.__a_type = a_type
        self.__order_service = OrderService()
        self.__car_service = CarService()
        self.__customer_menu = CustomerUI(
            self.__name, self.__a_type)

        self.__uistandard = UIStandard(name, a_type)

    def order_menu(self):
        """Prentar pantana viðmót tekur við inputi"""
        self.__order_service = OrderService()
        choice = ""
        while choice not in HOMECOMMANDS:
            self.__uistandard.clear_screen()
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
        while choice not in HOMECOMMANDS:
            self.__uistandard.clear_screen()
            choice = self.__uistandard.show_menu(
                """Pantanir - Yfirlit pantana\n\nSækja upplýsingar út frá:\n\n\t\
1. Kennitölu\n\t2. Pöntunarnúmeri\n\t3. Allar Pantanir\n""", "Veldu aðgerð: ")
            if choice == "1":
                ssn = input("\nKennitala viðskiptavinar: ")
                choice = self.ssn_order_menu(ssn)

            elif choice == "2":
                order_number = input("Hvaða pöntun viltu fá að sjá? ")
                choice = self.get_single_order(order_number)

            elif choice == "3":
                self.__uistandard.clear_screen()
                self.all_orders()
                choice = self.__uistandard.back_input()
        return choice

    def print_full_order_header(self):
        return "{:^11}| {:^11}| {:^9}| {:^30}| {:^11}| {:^7}|\
 {:^16}| {:^9}| {:^6}\n{}".format(
            "Upphafsd.",
                    "Skilad.",
                    "Pönt.nr.",
                    "Nafn",
                    "Kennitala",
                    "Bílnr.",
                    "Verð",
                    "Viðb.Try.",
                    "Afsl.",
                    "-"*126)

    def ssn_order_menu(self, ssn):
        self.__uistandard.clear_screen()
        self.__uistandard.print_header()
        customer = self.__customer_menu.get_the_customer(ssn)
        if not customer:
            print("Enginn viðskiptavinur með þessa kennitölu")
            time.sleep(2)
            return customer
        else:
            print("\t{} - {}\n\t{}".format(customer.get_name(), ssn, "-"*50))
            print("\t{:^11}| {:^9}| {:^11}| {:^7}".format(
                "Upphafsd.", "Pönt.nr.", "Tegund", "Bílnr."))
            print("\t{}".format("-"*50))
            order = self.__order_service.customer_orders(ssn, 1)
            print(order)
            choice = self.__uistandard.back_input()
        return choice

    def get_single_order(self, order_number):
        choice = ""
        self.__uistandard.clear_screen()
        while choice not in HOMECOMMANDS and choice != "2" and choice != "b":
            self.__uistandard.clear_screen()
            self.__uistandard.print_header()
            the_order = self.__order_service.find_order(order_number)
            if not the_order:
                print("Pöntunarnúmer ekki á skrá")
                time.sleep(2)
                return the_order
            else:
                self.__uistandard.clear_screen()
                order_header = self.print_full_order_header()
                strengur = "Pantanir - Yfirlit pantana- Pöntunarnúmer\n\n\
Pöntun: {}\n{}\n{}\n{}\n\n1. Breyta Pöntun\n2. Bakfæra pöntun\n\
".format(order_number, " -"*15, order_header, the_order)
                choice = self.__uistandard.show_menu(
                    strengur, "Veldu aðgerð: ").lower()
                if choice == "1":
                    self.change_order_menu(order_number, the_order)
                elif choice == "2":
                    self.__order_service.remove_order(order_number)
                    print("Pöntun hefur verið Bakfærð")
                    time.sleep(3)
        return choice

    def change_order_menu(self, order, the_order):
        print("Hverju skal breyta?\n\n1. Tímabil\n2. Bíll\n3. Tryggingar\n\
4. Viðskiptavinur\n5. Afsláttur\n")
        choice = input("Veldu aðgerð: ")
        if choice == "1":
            new_sday = input("Nýr upphafsdagur (dd): ")
            new_smon = input("Nýr upphafsmánuður (mm): ")
            new_syear = input("Nýtt upphafsár (yyyy): ")
            new_eday = input("Nýr skiladagur (dd): ")
            new_emon = input("Nýr skilamánuður (mm): ")
            new_eyear = input("Nýtt skilaár (yyyy): ")

            begin_date = "{}-{}-{}".format(new_syear, new_smon, new_sday)
            end_date = "{}-{}-{}".format(new_eyear, new_emon, new_eday)

            string_of_dates = self.__order_service.change_time(
                order, begin_date, end_date)
            print(string_of_dates)
            if len(string_of_dates) > 20:
                choice_of_car = input(
                    "Bílnúmer bíls sem skal breyta: ").upper()
                self.__order_service.change_car_again(choice_of_car, order)
                self.__order_service.add_dates_to_car(
                    begin_date, end_date, choice_of_car)
            time.sleep(2)
        elif choice == "2":
            licence_plate = the_order.get_car()
            the_car = self.__car_service.show_cars(licence_plate)
            car_type = the_car.get_type()
            string_of_cars = self.__order_service.change_car(car_type, order)
            print(string_of_cars)
            choice_of_car = input("Skráðu bílnúmer nýs bíls: ").upper()
            listi = the_order.get_duration()
            self.__order_service.change_car_again(choice_of_car, order)
            self.__order_service.add_dates_to_car(
                listi[0], listi[-1], choice_of_car, order)
        elif choice == "3":
            insurance = input("Viltu tryggingu? ((J)á/(N)ei): ")
            if insurance.lower() == "j":
                insurance = True
            else:
                insurance = False
            self.__order_service.change_insurance(order, insurance)
        elif choice == "4":
            ssn = input("Hver er kennitala viðskiptavinar? ")
            customer = self.__customer_menu.get_the_customer(ssn)
            if customer:
                print(customer)
                self.__order_service.change_customer(order, ssn)
            else:
                print("Enginn viðskiptavinur með þessa kennitölu")
                time.sleep(3)
        elif choice == "5":
            tester = True
            while tester:
                discount = input(
                    "Hvað viltu að nýji afslátturinn sé mörg prósent?").replace("%", "")
                try:
                    discount = float(discount)
                    if discount >= 1:
                        self.__order_service.change_discount(order, discount)
                        tester= False
                    elif 1 > discount > 0:
                        discount = discount *100
                        self.__order_service.change_discount(order,discount)
                        tester = False
                    else: 
                        print("Afslátturinn vitlaust sleginn inn, reyndu aftur")
                except ValueError:
                    print("{} er ekki tala, reyndu aftur".format(discount))

        return choice

    def all_orders(self):
        self.__uistandard.print_header()
        print("Pantanir - Yfirlit pantana - Allar pantanir\n")
        print(self.print_full_order_header())
        string = self.__order_service.show_orders()
        print(string)
        # Sæki drasl1

    def new_order_menu(self):
        availablecars = ""
        while availablecars == "":
            dates_okay = False
            self.__uistandard.print_header()
            print("Pantanir - Ný pöntun\n\tTímabil\n\t--------")
            while not dates_okay:
                begin_day = input("\tUpphafsdagur: ")
                begin_month = input("\tUpphafsmánuður: ")
                begin_year = input("\tUpphafsár: ")
                end_day = input("\tSkiladagur: ")
                end_month = input("\tSkilamánuður: ")
                end_year = input("\tSkilaár: ")
                try:
                    begining_date = date(
                        int(begin_year), int(begin_month), int(begin_day))
                    ending_date = date(
                        int(end_year), int(end_month), int(end_day))
                    if begining_date < ending_date:
                        dates_okay = True
                    else:
                        print("Ekki hægt að leiga bíl í minna en einn dag")
                except ValueError:
                    print("Vinsamlegast skráðu daga og mánuði á heiltölu \
    forminu 1,2,3... og ár á forminu 2018, 2019... ")

            begin_date = begin_year + "-" + begin_month + "-" + begin_day
            end_date = end_year + "-" + end_month + "-" + end_day
            list_of_days = self.__order_service.list_of_days(
                begin_date, end_date)
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
            if availablecars == "":
                print("Engir bílar í boði af þessari gerð á þessum tíma.")
                print("Vinsamlegast skráðu inn aðrar dagsetningar")
                time.sleep(2)
        print(availablecars)
        licence_plate = input("Skrifa bílnúmer: ").upper()
        order_number = self.__order_service.make_order_number()
        price = self.__order_service.price_of_rent(
            licence_plate, 0, False, begin_date, end_date)
        print("Verð með skyldutryggingu en án aukatrygginga: {}".format(price))
        # Hér þarf að sækja verð
        extra_insurance_price = self.__order_service.get_price_of_extra_insurance()
        insurance = input(
            "\tViðbótartrygging (verð {} á dag) (J)á/(N)ei: ".format(
                extra_insurance_price))
        if insurance.lower() == "j":
            insurance = True
            price = self.__order_service.price_of_rent(
                licence_plate, 0, True, begin_date, end_date)
            print("Verð með aukatryggingum: {}".format(price))
        else:
            insurance = False

        tester = True
        while tester:
            discount = input(
                "\tSkrifaðu hversu mörg prósent afslátturinn á að vera ef einhver: ").replace("%", "")
            try:
                discount = float(discount)
                if discount >= 1:
                    discount = discount
                    tester= False
                elif 1 > discount > 0:
                    discount = discount *100
                    tester = False
                else: 
                    print("Aflátturinn vitlaust sleginn inn, reyndu aftur")
            except ValueError:
                print("{} er ekki tala, reyndu aftur".format(discount))
        total_price = self.__order_service.price_of_rent(
            licence_plate, discount, insurance, begin_date, end_date)
        if total_price != price:
            print("Heildarverð með afslætti: {}".format(
                total_price))  # hér þarð að nota aðra klasa
        ssn = input("\tKennitala viðskiptavinar: ")
        # if setning til að athuga hvort manneskjan sé til. Ef svo er
        # þá prentast út upplýsingar um hana, annars er sótt fall til
        # að gera nýjan viðskiptavin
        choice = ""
        customer = self.__customer_menu.get_the_customer(ssn)
        if customer:
            customer_name = customer.get_name()
        else:
            while choice != "j" and choice != "n":
                choice = input(
                        "Viðskiptavinur ekki skráður í kerfið. Má bjóða þér að skrá inn nýjan viðskiptavin? (J)á eða (N)ei? ").lower()
                if choice == "j":
                    ssn = self.__customer_menu.new_customer_menu()
                    customer = self.__customer_menu.get_the_customer(ssn)
                    customer_name = customer.get_name()
                if choice == "n":
                    print("Enginn nýr viðskiptavinur skráður. Notandi sendur heim")
                    time.sleep(2)
        if choice != "n":
            print("\n\tViðskiptavinur: {}".format(customer_name))
            payment = input("\tGreiðslumáti: (D)ebit, (K)redit, (P)eningar: ")
            order_number = self.__order_service.make_order_number()
            order =Order(order_number, list_of_days, ssn, customer_name,
                        licence_plate, total_price, insurance, discount)
            self.__order_service.add_dates_to_car(
                begin_date, end_date, licence_plate, order_number)

            self.__order_service.make_order(order_number, order)

        # kallar á föll og býr til klasa
            print("---------------------\nPöntun Staðfest\n")
            time.sleep(2)
        return "h"
