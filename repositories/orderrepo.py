from models.order import Order
import csv


class OrderRepo(object):
    def __init__(self):
        pass

    def add_order(self, order):
        with open("./data/orders.csv", "a+") as orders_file:
            orders_file.write(order.__repr__() + "\n")

    def remove_order(self, order_number):
        pass

    def get_orders(self):
        orders = []
        with open("./data/orders.csv", "r") as orders_file:
            csv_reader = csv.reader(orders_file)
            for line in csv_reader:
                orders.append(line)
        return orders
