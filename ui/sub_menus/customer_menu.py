from models.customer import Customer
from models.order import Order
from services.customerservice import CustomerService
from services.orderservice import OrderService
from ui.ui_standard_functions import UIStandard
import time
HOMECOMMANDS = ["h", "H", "s", "S"]


class CustomerUI(object):
    """Klasi sem sér um viðmót Sölumanns og ferðir þar um"""

    def __init__(self, name, a_type):
        self.__name = name
        self.__order_service = OrderService()
        self.__customer_service = CustomerService()
        self.__uistandard = UIStandard(name, a_type)

    def get_the_customer(self, ssn):
        customer = self.__customer_service.find_customer(ssn)
        return customer

    def customer_menu(self):
        """Prentar viðskiptavinaviðmót sölumanns og tekur við input"""
        choice = ""
        self.__uistandard.clear_screen()
        while choice not in HOMECOMMANDS:
            choice = self.__uistandard.show_menu(
                """Viðskiptavinir\n\n\t1. Leita eftir kennitölu
    \t2. Fá yfirlit yfir alla viðskiptavini\n\t3. Nýr viðskipavinur\n""",
                "Veldu aðgerð: ")
            if choice == "1":
                ssn = input("Kennitala: ")
                customer = self.get_the_customer(ssn)
                # returnar None ef að hann finnst ekki
                if customer:
                    self.find_customer(ssn, customer)
                else:
                    print("Enginn viðskiptavinur skráður á þessa kennitölu")
                    time.sleep(2)

            if choice == "2":
                choice = self.get_customer_list()
            if choice == "3":
                self.new_customer_menu()
        return choice

    def find_customer(self, ssn, customer):
        self.__uistandard.print_header()

        print("Viðskiptavinir - Kennitala\n")
        print("\tViðskiptavinur\n\t{}".format("-"*20))
        print("\t{} - {} - S: {}".format(
            customer.get_ssn(), customer.get_name(),
            customer.get_phone_number()))
        print("\n\tSaga pantana\n\t{}".format("-"*60))
        print("\t{:13}| {:9}| {:7}| {:10}".format(
            "Upphafsdagur", "Pönt.nr.", "Bílnr.", "Verð"))
        print("\t{}".format("-"*60))
        order = self.__order_service.customer_orders(ssn)
        print(order)
        choice = input("\n1. Breyta\n2. Eyða\n\nVeldu aðgerð: ")
        if choice == "1":
            self.change_menu(ssn)
        elif choice == "2":
            choice = input("Ertu viss? ((J)á/(N)ei: ")
            if choice.lower() == 'j':
                self.__customer_service.remove_customer(ssn)
                print("Viðskiptavini hefur verið eytt")
                self.save_program()
            time.sleep(2)
        else:
            print("Aðgerð ekki í boði")
            time.sleep(2)

    def change_menu(self, ssn):
        choice = ""
        while choice not in HOMECOMMANDS:
            print("\nHverju skal breyta?\n{}".format("-"*30))
            choice = input("1. Breyta nafni"
                           "\n2. Breyta símanúmer"
                           "\n3. Breyta kredikortanúmeri"
                           "\n\nVeldu aðgerð: ")
            if choice == "1":
                new_name = input("Nýtt nafn: ")
                self.__customer_service.change_name(ssn, new_name)
                print("Nafni viðskiptavinar hefur verið breytt")
                time.sleep(2)
            elif choice == "2":
                new_phone_number = input("Nýja símanúmerið: ")
                self.__customer_service.change_phone_number(
                    ssn, new_phone_number)
                print("Símanúmeri viðskiptavinar hefur verið breytt")
                time.sleep(2)
            elif choice == "3":
                new_card_number = input("Nýja kortanúmerið: ")
                self.__customer_service.change_card(ssn, new_card_number)
                print("Kreditkortanúmeri viðskiptavinar hefur verið breytt")
                time.sleep(2)
            self.save_program()
        return choice

    def get_customer_list(self):
        """Prentar ut lista yfir alla viðskiptavini með grunnupplýsingum"""
        self.__uistandard.print_header()
        line_seperator = ("-"*100)
        print("{:<100}".format("\nViðskiptavinir - Allir Viðskiptavinir\n"))
        print((line_seperator) + "\n{:^11}| {:^30}| {:^9} |\n".format(
            "Kennitala", "Nafn", "Sími") + (line_seperator))
        string = self.__customer_service.get_list()
        print(string)
        choice = input("B - tilbaka, H - Heim, S - Útskrá: ")
        return choice

    def new_customer_menu(self):
        """biður um nauðsynlegar upplýsingar og býr til viðskiptavin"""
        self.__uistandard.clear_screen()
        self.__uistandard.print_header()
        print("Viðskiptavinir - Nýr viðskiptavinur\n")
        check_string = "1"
        choice = "j"
        while choice == "j":
            ssn = input("\tKennitala: ")
            name = input("\tNafn: ")
            phone_number = input("\tSími: ")
            credit_card_number = input("\tKreditkort: ")
            check_string = self.__customer_service.test_values(
                ssn, name, phone_number, credit_card_number)
            if check_string:
                print()
                print(check_string)
            else:
                print("\nKennitala: {}\nNafn: {}\nSími: {}\nKreditkortanúmer: {}\
\nÖll gildi samþykkt. Er allt rétt skráð inn?".format(
                    ssn, name, phone_number, credit_card_number))
                time.sleep(2)
            choice = input(
                "\nViltu endurtaka skráningu?\nVeldu (J)á til að reyna aftur: "
            )
        if check_string == "":
            a_customer = Customer(ssn, name, phone_number, credit_card_number)
            self.__customer_service.make_customer(a_customer)

            # new_customer = self.__customer_service.find_customer(ssn)
            # print("{:>20}{:>30}{:>20}".format("Kennitala", "Nafn", "Sími"))
            # print(new_customer)
            time.sleep(2)
        self.save_program()

    def save_program(self):
        self.__customer_service.save_program()
