from models.order import Order
import csv


class OrderRepo(object):
    def __init__(self):
        pass

    def add_order(self, order):
        '''Bætir við pöntun í geymslu'''
        with open("./data/orders.csv", "a+") as orders_file:
            orders_file.write(order.__repr__() + "\n")

    def remove_order(self, order_number):
        with open("./data/orders.csv", "r") as orders_input:
            with open("./data/orders_edit.csv", "w",
                      newline="") as orders_output:
                csv_reader = csv.reader(orders_input)
                csv_writer = csv.writer(orders_output)
                for row in csv_reader:
                    if row:
                        if row[0] != order_number:
                            csv_writer.writerow(row)

        with open("./data/orders.csv", "w",
                  newline="") as new_orders_file:
            with open("./data/orders_edit.csv", "r") as new_orders_edit:
                csv_reader = csv.reader(new_orders_edit)
                csv_writer = csv.writer(new_orders_file)
                for row in csv_reader:
                    if row:
                        csv_writer.writerow(row)

    def get_orders(self):
        orders = []
        with open("./data/orders.csv", "r") as orders_file:
            csv_reader = csv.reader(orders_file)
            next(csv_reader)
            for line in csv_reader:
                orders.append(line)
        return orders
