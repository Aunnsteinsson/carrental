from datetime import date
from models.customer import Customer
from models.order import Order
from models.car import Car
from models.employee import Employee
from services.carservice import CarService
from services.customerservice import CustomerService
from services.employeeservice import EmployeeService
from services.orderservice import OrderService
HOMECOMMANDS = ["h", "H", "s", "S"]


class SalesmanUI(object):
    """Klasi sem sér um viðmót Sölumanns og ferðir þar um"""

    def __init__(self, name):
        self.__name = name
        self.__customer_service = CustomerService()
        self.__car_service = CarService()
        self.__order_service = OrderService()
        self.__employee_service = EmployeeService()

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

    def main_menu(self):
        choice = ""
        while choice != HOMECOMMANDS[2] and choice != HOMECOMMANDS[3]:
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
        """Prentar pantana viðmót tekur við inputi"""
        choice = ""
        while choice not in HOMECOMMANDS:  # Placeholder þangað til ég næ að
            # lata while loopuna virka betur
            choice = self.show_menu(
                "Pantanir\n\t1. Yfirlit pantana\n\t2. Ný pöntun")
            if choice == "1":
                choice = self.order_list_menu()
            elif choice == "2":
                choice = self.new_order_menu()
        return choice

    def order_list_menu(self):
        """Prentar innra pantana viðmót og tekur við input"""
        choice = ""
        while choice not in HOMECOMMANDS:  # Placeholder
            choice = self.show_menu(
                """Pantanir - Yfirlit pantana\n\tSækjaupplýsingar út frá:
\t1. Kennitölu\n\t2. Pöntunarnúmeri\n\t3. Allar Pantanir""")
            if choice == "1":  # TODO Þurfum að geta tengt viðskiptavin við pöntun
                pass
            if choice == "2":  # TODO Þurfum að gefa pöntunarnúmer
                pass
            if choice == "3":
                self.all_orders()
        return choice

    def all_orders(self):
        self.print_header()
        print("dagsetning | Pönt.nr |  Nafn  |  Kennitala  | Tegund",
              "Bílnr.  | Staða")
        print("\t", "-"*80)
        # Sæki drasl1

    def new_order_menu(self):
        self.print_header()
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
        #self, start_date, end_date, car, insurance=False
        an_order = Order(begin_date, end_date, type_of_car, insurance)
        self.__order_service.make_order(an_order)

        # kallar á föll og býr til klasa
        print("---------------------\nPöntun Staðfest\n")
        return "h"

    def customer_menu(self):
        """Prentar viðskiptavinaviðmót sölumanns og tekur við input"""
        choice = ""
        while choice not in HOMECOMMANDS:
            choice = self.show_menu(
                """Viðskiptavinir\n\t1. Leita eftir kennitölu
\t2. Fá yfirlit yfir alla viðskiptavini\n\t3. Nýr viðskipavinur""")
            if choice == "1":
                ssn = input("Kennitala: ")
                customer = self.__customer_service.find_customer(ssn)
                # returnar None ef að hann finnst ekki
                if customer:
                    self.find_customer(ssn, customer)
                else:
                    print("Enginn viðskiptavinur skráður á þessa kennitölu")

            if choice == "2":
                string = self.get_customer_list()
                print(string)
            if choice == "3":
                self.new_customer_menu()
        return choice

    def find_customer(self, ssn, customer):
        self.print_header()
        print("Viðskiptavinir - Kennitala\n")
        print(customer)
        # self.__order_service.showorders(customer)
        # þetta vantar alveg inn
        choice = input("\t1. Breyta\n\t2. Eyða\n\tVeldu aðgerð: ")
        if choice == "1":
            self.change_menu(ssn)
        if choice == "2":
            self.__customer_service.remove_customer(ssn)
            print("Viðskiptavini hefur verið eytt")
        else:
            print("Aðgerð ekki í boði")

    def change_menu(self, ssn):
        what_to_change = input("1 Breyta nafni"
                               "\n2. Breyta símanúmer"
                               "\n3. Breyta kredikortanúmeri")
        if what_to_change == "1":
            new_name = input("Nýtt nafn")
            self.__customer_service.change_name(ssn, new_name)
        if what_to_change == "2":
            new_phone_number = input("Nýja símanúmerið")
            self.__customer_service.change_phone_number(ssn, new_phone_number)
        if what_to_change == "3":
            new_card_number = input("Nýja kortanúmerið")
            self.__customer_service.change_card(ssn, new_card_number)

    def get_customer_list(self):
        """Prentar ut lista yfir alla viðskiptavini með grunnupplýsingum"""
        self.print_header()
        print("Viðskiptavinir - Allir Viðskiptavinir")
        print("\t Kennitala     | Nafn        | Sími")
        print("-"*50)
        string = self.__customer_service.get_list()
        print(string)
        choice = input("Veldu aðgerð")
        if choice in HOMECOMMANDS:
            return choice
        else:
            return None

    def new_customer_menu(self):
        """biður um nauðsynlegar upplýsingar og býr til viðskiptavin"""
        self.print_header
        print("Viðskiptavinir - Nýr viðskiptavinur\n")
        ssn = input("\tKennitala: ")
        name = input("\tNafn: ")
        phone_number = input("\tSími: ")
        credit_card_number = input("\tKreditkort: ")
        a_customer = Customer(ssn, name, phone_number, credit_card_number)
        self.__customer_service.make_customer(a_customer)

    def car_menu(self):
        """Pprentar bílayfirlits viðmót og tekur við input"""
        choice = ""
        while choice not in HOMECOMMANDS:  # Placeholder
            choice = self.show_menu(
                """Bílayfirlit\n\t1. Allir Bílar
\t2. Lausir Bílar\n\t3. Í útleigu""")
            if choice == "1" or "2" or "3":
                if choice == "1":
                    menu = "sem eru lausir eða í útleigu"
                    listi1 = ["Fratekinn", "Laus"]
                if choice == "2":
                    menu = "sem eru lausir "
                    listi1 = ["Laus"]
                if choice == "3":
                    menu = "sem eru í útleigu"
                    listi1 = ["Fratekinn"]
                second_choice = input(
                    "\t1. Allar gerðir\n\t2. Jeppar\n\t3. Fólksbílar"
                    "\n\t4. Sendibílar")
                if second_choice == "2":
                    the_type = "Jeppar"
                    listi2 = ["Jeppi"]
                elif second_choice == "3":
                    the_type = "Fólksbílar"
                    listi2 = ["Fólksbill"]
                elif second_choice == "4":
                    the_type = "Sendibílar"
                    listi2 = ["Sendibill"]
                else:
                    the_type = "all_cars"
                    listi2 = ["Sendibill", "Folksbill", "Jeppi"]
            choice = self.second_car_menu(the_type, menu, listi1, listi2)
        return choice

    def second_car_menu(self, the_type, menu, listi1, listi2):
        self.print_header()
        print("Bílayfirlit - {} {}".format(the_type, menu))
        print("\tTegund | Bílnúmer | Staða\n\t", "-"*23)
        strengur = self.__car_service.get_list_of_cars(listi2, listi1)
        print(strengur)
        choice = ""
        while choice not in HOMECOMMANDS:
            choice = input("Veldu aðgerð: ")
        return choice
