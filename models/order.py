class Order(object):
    def __init__(self, start_date, end_date, car):
        self.__start_date = start_date
        self.__end_date = end_date
        self.__car = car

    def __str__(self):
        pass

    def get_start(self):
        return self.__start_date

    def get_end(self):
        return self.__end_date

    def get_duration(self):
        pass

    def get_price(self):
        pass

    def get_insurance(self):
        pass

    def __repr__(self):
        # return "{},{},{}".format(self.__start_date,
        # self.__end_date, self.__car)
        pass
