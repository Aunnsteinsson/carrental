from repositories.orderrepo import OrderRepo
from models.order import order


class OrderService(object):
    def __init__(self):
        self.__order_repo = OrderRepo()

    def make_order(self, order):
        self.__order_repo.add_order(order)

    def remove_order(self, order_number):
        self.__order_repo.remove_order(order_number)

    def check_availability(self):
        pass

    def change_time(self):
        pass

    def change_insurance(self):
        pass

    def show_orders(self):
        order_dict = self.__order_repo.get_orders()
        string_of_orders = ""
        for kennitala, value in order_dict.items():
            order_string = value.__str__()
            string_of_orders += order_string + "\n"
        return string_of_orders
