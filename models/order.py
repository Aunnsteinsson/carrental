class Order(object):
    '''Pöntunar klasi, tekur inn pöntunarnúmer, upphafsdag, 
    skiladag, bílaflokk og viðbótartryggingu'''

    def __init__(self, order_number, start_date, end_date, car, insurance=False):
        self.__order_number = order_number
        self.__start_date = start_date
        self.__end_date = end_date
        self.__car = car
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

    def __str__(self):
        '''Prentaðar út þær upplýsingar sem tilheyra pöntun.'''
        return "Pöntunarnúmer: {}, Upphafsdagur: {}, Skiladagur: {}, Bíll: {}, \
Viðbótartrygging: {}".format(self.__order_number, self.__start_date,
                             self.__end_date, self.__car,
                             self.__insurance)

    def __repr__(self):
        return "{},{},{},{},{}".format(self.__order_number, self.__start_date,
                                       self.__end_date, self.__car,
                                       self.__insurance)
