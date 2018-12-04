class Order(object):
    def __init__(self, start_date, end_date, car, insurance=False):
        self.__start_date = start_date
        self.__end_date = end_date
        self.__car = car
        self.__insurance = insurance

    def get_start(self):
        return self.__start_date

    def get_end(self):
        return self.__end_date

    def get_insurance(self):
        return self.__insurance

    def change_start(self, new_start):
        self.__start_date = new_start
        return new_start

    def change_end(self, new_end):
        self.__end_date = new_end

    def change_insurance(self, new_ins):
        self.__insurance = new_ins

    def __str__(self):
        pass

    def __repr__(self):
        # return "{},{},{},{}".format(self.__start_date,
        # self.__end_date, self.__car, self.__insurance)
        pass
