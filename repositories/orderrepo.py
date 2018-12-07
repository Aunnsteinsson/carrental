from models.order import Order
import csv
ORDERNR = 0
STARTDATE = 1
ENDDATE = 2
CAR = 3
INSURANCE = 4

# virkar ekki að gera dict eins og Denni er að gera með customer


class OrderRepo(object):
    def __init__(self):
        pass
        #     self.__order = self.order_dict()

        # def order_dict(self):
        #     order_dict = {}
        #     with open("./data/orders.csv", "r") as orders_file:
        #         csv_reader = csv.reader(orders_file)
        #         next(csv_reader)
        #         for order in csv_reader:
        #             order_class = Order(
        #                 order[ORDERNR], order[STARTDATE], order[ENDDATE],
        #                 order[CAR], order[INSURANCE])
        #             order_number = order[ORDERNR]
        #             order_dict[order_number] = order_class
        #     return order_dict

    def add_order(self, order):
        '''
        Bætir við pöntun í csv skrá, skrifast inn eftir repr falli
        í Order klasanum.
        '''
        with open("./data/orders.csv", "a+") as orders_file:
            orders_file.write(order.__repr__() + "\n")

    def remove_order(self, order_number):
        '''
        Notar order_number sem key til að leita í dictionary með pöntunum,
        ef í dict, þá eyðir fallið þeirri pöntun.
        '''
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
        # for ordernr, value in self.__order.items():
        #     if ordernr == order_number:
        #         print(self.__order[order_number])
        #         del self.__order[order_number]
        #         return self.__order
        # return False

    def get_order(self, order_number):
        '''
        Ef pöntunarnúmerið sem leitað er að er til í dictionary 
        yfir pantanir skilar það upplýsingum pöntunar, annars False
        '''
        for ordernr, value in self.__order.items():
            if ordernr == order_number:
                return self.__order[order_number]
        return False

    def all_orders(self):
        '''
        Skilar öllum pöntunum
        '''
        return self.__order

    # def overwrite
