from models.order import Order
import csv
ORDERNR = 0
STARTDATE = 1
ENDDATE = 2
NAME = 3
SSN = 4
CAR = 5
CARNR = 6
STATUS = 7
INSURANCE = 8
# lgoi


class OrderRepo(object):
    def __init__(self):
        '''
        Kallar í order_dict fallið og gefur self.__orders orðabókina.
        '''
        self.__orders = self.order_dict()

    def add_order(self, order_number, order):
        '''
        Bætir við pöntun í orðabók sem unnið er með.
        '''
        self.__orders[order_number] = order

    def remove_order(self, order_number):
        '''
        Notar order_number sem key til að leita í orða með pöntunum,
        ef í dict, þá eyðir fallið þeirri pöntun.
        '''
        for ordernr, value in self.__orders.items():
            if ordernr == order_number:
                print(self.__orders[order_number])
                del self.__orders[order_number]
                return self.__orders
        return False

    def get_order(self, order_number):
        order = self.__orders[order_number]
        return order

    def get_orders(self):
        '''
        Skilar orders orðabók til vinnslu.
        '''
        return self.__orders

    def save_new_orders(self):
        '''
        Vistar upplýsingar úr orðabók í csv skrá sem heldur utan
        um upplýsingarnar.
        '''
        orders_header = "order_number,start,end,name,ssn,car,car_number,\
status_of_car,insurance"
        with open("./data/orders.csv", "w", newline="") as orders_file:
            csv_writer = csv.writer(orders_file)
            csv_writer.writerow(orders_header.split(','))
            for order_number, info in self.__orders.items():
                order_string = info.__repr__().split(",")
                csv_writer.writerow(order_string)

    def order_dict(self):
        '''
        Tekur við gögnum, upplýsingum um pantanir, úr orders.csv og les inn í
        orðabók. Þá er lykillinn pöntunarnúmerið og gildið er Orders
        klasinn með upplýsingunum.
        '''
        order_dict = {}
        with open("./data/orders.csv", "r") as orders_file:
            csv_reader = csv.reader(orders_file)
            next(csv_reader)
            for order in csv_reader:
                order_class = Order(
                    order[ORDERNR],
                    order[STARTDATE],
                    order[ENDDATE],
                    order[NAME],
                    order[SSN],
                    order[CAR],
                    order[CARNR],
                    order[STATUS],
                    order[INSURANCE])
                order_number = order[ORDERNR]
                order_dict[order_number] = order_class
        return order_dict
