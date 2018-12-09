from models.order import Order
import copy
import csv
ORDERNR = 0
STARTDATE = 1
ENDDATE = 2
CAR = 3
INSURANCE = 4

# virkar ekki að gera dict eins og Denni er að gera með customer


class OrderRepo(object):
    def __init__(self):
        self.__original_orders = self.order_dict()
        self.__new_orders = copy.deepcopy(self.__original_orders)
        print("first: {}".format(self.__original_orders))
        print("first new: {}".format(self.__new_orders))

    def order_dict(self):
        order_dict = {}
        with open("./data/orders.csv", "r") as orders_file:
            csv_reader = csv.reader(orders_file)
            next(csv_reader)
            try:
                for order in csv_reader:
                    order_class = Order(
                        order[ORDERNR], order[STARTDATE], order[ENDDATE],
                        order[CAR], order[INSURANCE])
                    order_number = order[ORDERNR]
                    order_dict[order_number] = order_class
            except IndexError:
                return order_dict
        return order_dict

    def save_new_orders(self, new_orders):
        orders_header = "order_number,start,end,car,insurance"
        with open("./data/orders.csv", "w", newline="") as orders_file:
            csv_writer = csv.writer(orders_file)
            csv_writer.writerow(orders_header.split(','))
            for order_number, info in new_orders.items():
                info = info.strip()
                order_string = info.__repr__().split(",")
                csv_writer.writerow(order_string)

    def add_order(self, order_number, order):
        '''
        Bætir við pöntun í dictionary sem unnið er með.
        '''
        order_info = order.__repr__()
        self.__new_orders[order_number] = order_info

        return self.__new_orders

    def remove_order(self, order_number):
        '''
        Notar order_number sem key til að leita í dictionary með pöntunum,
        ef í dict, þá eyðir fallið þeirri pöntun.
        '''
        for ordernr, value in self.__new_orders.items():
            if ordernr == order_number:
                print(self.__new_orders[order_number])
                del self.__new_orders[order_number]
                return self.__new_orders
        return False
        # with open("./data/orders.csv", "r") as orders_input:
        #     with open("./data/orders_edit.csv", "w",
        #               newline="") as orders_output:
        #         csv_reader = csv.reader(orders_input)
        #         csv_writer = csv.writer(orders_output)
        #         for row in csv_reader:
        #             if row:
        #                 if row[0] != order_number:
        #                     csv_writer.writerow(row)

        # with open("./data/orders.csv", "w",
        #           newline="") as new_orders_file:
        #     with open("./data/orders_edit.csv", "r") as new_orders_edit:
        #         csv_reader = csv.reader(new_orders_edit)
        #         csv_writer = csv.writer(new_orders_file)
        #         for row in csv_reader:
        #             if row:
        #                 csv_writer.writerow(row)

    def get_orders(self):
        '''
        Skilar orders dictionary til vinnslu.
        '''
        return self.__new_orders
