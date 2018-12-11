class Order(object):
    '''Pöntunar klasi, tekur inn pöntunarnúmer, upphafsdag, 
    skiladag, bílaflokk og viðbótartryggingu'''

    def __init__(self, order_number, start_date, end_date, name, ssn, car,
                 car_number, status_of_car, insurance=False):
        self.__order_number = order_number
        self.__start_date = start_date
        self.__end_date = end_date
        self.__name = name
        self.__ssn = ssn
        self.__car = car
        self.__car_number = car_number
        self.__status = status_of_car
        self.__insurance = insurance

    def get_order_number(self):
        return self.__order_number

    def get_start(self):
        return self.__start_date

    def get_end(self):
        return self.__end_date

    def get_insurance(self):
        return self.__insurance

    def get_car(self):
        return self.__car

    def change_start(self, new_start):
        self.__start_date = new_start

    def change_end(self, new_end):
        self.__end_date = new_end

    def change_insurance(self, new_insurance):
        self.__insurance = new_insurance

    def change_car(self, new_car):
        self.__car = new_car

    def __str__(self, info_to_print=0):
        '''Annars vegar skilar upplýsingum prentuðum með án kennitölu.
        Það er nýtt þegar pöntun er sköðuð út frá Kennitölu.
        Hins vegar skilar upplýsingum með kommu á milli, notað til skráningar
        í geymslu.'''
        if info_to_print == 1:
            return "\t {:11}| {:14}| {:10}| {:9}| {:10}".format(
                self.__start_date, self.__order_number, self.__car,
                self.__car_number, self.__status)
        else:
            return "\t {:11}| {:14}| {:25}| {:11}| {:10}| {:9}| {:10}".format(
                self.__start_date, self.__order_number, self.__name,
                self.__ssn, self.__car, self.__car_number, self.__status)

    def __repr__(self, ):
        return "{},{},{},{},{}".format(self.__order_number, self.__start_date,
                                       self.__end_date, self.__car,
                                       self.__insurance)
