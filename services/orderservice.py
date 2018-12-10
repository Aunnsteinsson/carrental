from repositories.orderrepo import OrderRepo
from models.order import Order


class OrderService(object):
    def __init__(self):
        self.__order_repo = OrderRepo()

    def make_order(self, order):
        self.__order_repo.add_order(order)

    def remove_order(self, order_number):
        self.__order_repo.remove_order(order_number)

    def check_availability(self, start_date, finish_date, start_required_date, finish_required_date):
        if start_required_date in range(start_date, finish_date) or finish_required_date in range(start_date, finish_date):
            return False
        else:
            return True

    def change_time(self, order_number, new_time):
        order = self.__order_repo.get_orders(order_number)
        order.change_time(new_time)

    def change_insurance(self, order_number, new_insurance):
        order = self.__order_repo.get_orders(order_number)
        order.change_insurance(new_insurance)

    def show_orders(self):
        order_dict = self.__order_repo.get_orders()
        string_of_orders = ""
        for order, value in order_dict.items():
            order_string = value.__str__()
            string_of_orders += order_string + "\n"
        return string_of_orders
