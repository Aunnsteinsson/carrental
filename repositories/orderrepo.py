from models.order import Order
import csv
ORDERNR = 0
STARTDATE = 1
ENDDATE = 2
CAR = 3
INSURANCE = 4
# lgoi


class OrderRepo(object):
    def __init__(self):
        global orders_dict
        self.__orders = order_dict

    def add_order(self, order_number, order):
        '''
        Bætir við pöntun í dictionary sem unnið er með.
        '''
        self.__orders[order_number] = order

    def remove_order(self, order_number):
        '''
        Notar order_number sem key til að leita í dictionary með pöntunum,
        ef í dict, þá eyðir fallið þeirri pöntun.
        '''
        for ordernr, value in self.__orders.items():
            if ordernr == order_number:
                print(self.__orders[order_number])
                del self.__orders[order_number]
                return self.__orders
        return False

    def get_orders(self):
        '''
        Skilar orders dictionary til vinnslu.
        '''
        return self.__orders

    def save_new_orders(self):
        orders_header = "order_number,start,end,car,insurance"
        with open("./data/orders.csv", "w", newline="") as orders_file:
            csv_writer = csv.writer(orders_file)
            csv_writer.writerow(orders_header.split(','))
            for order_number, info in self.__orders.items():
                order_string = info.__repr__().split(",")
                csv_writer.writerow(order_string)


def order_dict():
    order_dict = {}
    with open("./data/orders.csv", "r") as orders_file:
        csv_reader = csv.reader(orders_file)
        next(csv_reader)
        for order in csv_reader:
            order_class = Order(
                order[ORDERNR], order[STARTDATE], order[ENDDATE],
                order[CAR], order[INSURANCE])
            order_number = order[ORDERNR]
            order_dict[order_number] = order_class
    return order_dict


order_dict = order_dict()
