from repositories.orderrepo import OrderRepo
from models.order import Order
from repositories.carrepo import CarRepo
from models.car import Car
from models.customer import Customer
from datetime import date, timedelta


class OrderService(object):
    def __init__(self):
        self.__order_repo = OrderRepo()

    def make_order(self, order, order_number):
        self.__order_repo.add_order(order, order_number)

    def make_order_number(self):
        new_order_number = 0
        for order_number in self.__order_repo.get_orders():
            order_num = int(order_number)
            if order_num > new_order_number:
                new_order_number = order_num
        new_order_number += 1
        return new_order_number

    def remove_order(self, order_number):
        self.__order_repo.remove_order(order_number)

    def check_availability(self, start_date, finish_date):
        list_startdate = start_date.split("/")
        list_finishdate = finish_date.split("/")
        start_year, start_month, start_day = int(list_startdate[2]), int(
            list_startdate[1]), int(list_startdate[0])
        finish_year, finish_month, finish_day = int(list_finishdate[2]), int(
            list_finishdate[1]), int(list_finishdate[0])
        start_date = date(start_year, start_month, start_day)
        finish_date = date(finish_year, finish_month, finish_day)
        step = timedelta(days=1)
        unavailable_list = []
        while start_date <= finish_date:
            unavailable_list.append(start_date)
            start_date += step

    def get_car(self, a_type, duration):
        pass

    def get_customer_name(self, customer):
        name = customer.get_name()
        return name

    def customer_orders(self, ssn):
        order = self.__order_repo.get_orders()
        string_of_orders = ""
        for key, orders in order.items():
            if ssn == orders.get_ssn():
                order_string = orders.__str__()
                string_of_orders += order_string + "\n"
        return string_of_orders

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
