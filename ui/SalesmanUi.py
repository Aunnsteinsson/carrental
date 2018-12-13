from ui.ui_standard_functions import UIStandard
from ui.sub_menus.order_menu import OrderUI
from ui.sub_menus.customer_menu import CustomerUI
from ui.sub_menus.car_menu import CarUI
from ui.sub_menus.price_menu import PriceUI
HOMECOMMANDS = ["h", "H", "s", "S"]


class SalesmanUI(object):
    """Klasi sem sér um viðmót Sölumanns og ferðir þar um"""

    def __init__(self, name, emp_type):
        self.__emp_type = emp_type
        self.__name = name
        self.__uistandard = UIStandard(self.__name, self.__emp_type)
        self.__order_ui = OrderUI(self.__name, self.__emp_type)
        self.__customer_ui = CustomerUI(self.__name, self.__emp_type)
        self.__car_ui = CarUI(self.__name, self.__emp_type)
        self.__price_ui = PriceUI(self.__name, emp_type)

    def main_menu(self):
        choice = ""
        while choice != HOMECOMMANDS[2] and choice != HOMECOMMANDS[3]:
            self.__uistandard.clear_screen()
            choice = self.__uistandard.show_menu(
                """ \n\t1. Pantanir\n\t2. Bílayfirlit
\t3. Viðskiptavinir\n\t4. Verðlisti\n""", "Veldu aðgerð: ")
            self.__uistandard.clear_screen()
            if choice == "1":
                choice = self.__order_ui.order_menu()
                self.__customer_ui = CustomerUI(self.__name, self.__emp_type)
            elif choice == "2":
                choice = self.__car_ui.boss_and_salesman_car_menu()
            elif choice == "3":
                choice = self.__customer_ui.customer_menu()
            elif choice == "4":
                choice = self.__price_ui.salesman_get_price_menu()

        # ég hef ekki hugmynd um hvernig við ætlum að sýna verðlistann
