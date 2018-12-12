import csv


class Order(object):
    '''Klasi fyrir pantanir. Breytur í þessum klasa eru pöntunarnúmer, upphafsdagur,
    skiladagur, nafn viðskiptavinar, kennitala viðskiptavinar, bíltegund, bílnúmer, 
    staða bíls og hvort pöntun innihaldi aukatryggingu eður ei.
    Klasinn inniheldur föll til að hægt sé að kalla á breytur eða breyta þeim.
    Hægt er að fá __str__ á tvo mismunandi vegu.'''

    def __init__(self, order_number, list_of_dates, name, ssn, car,
                 car_number, status_of_car, insurance=False, discount=0.000):
        self.__order_number = order_number
        self.__list_of_dates = list_of_dates
        self.__name = name
        self.__ssn = ssn
        self.__car = car
        self.__car_number = car_number
        self.__status = status_of_car
        self.__insurance = insurance
        self.__discount = discount

    # Föll hér að neðan er hægt að kalla í til að nálgast breyturnar

    def get_order_number(self):
        return self.__order_number

    def get_discount(self):
        return self.__discount

    def change_discount(self, new_discount):
        self.__discount = new_discount

    def get_licence_plate(self):
        return self.__car_number

    def get_duration(self):
        return self.__list_of_dates

    def dates_list_to_string(self, list_of_dates):
        string_of_dates = ""
        for date in list_of_dates:
            string_of_dates += date + ","
        return string_of_dates

    def dates_string_to_list(self, dates_string):
        date_list = dates_string.strip(',').split(',')
        return date_list

    def get_insurance(self):
        return self.__insurance

    def get_car(self):
        return self.__car

    def get_ssn(self):
        return self.__ssn

    # Föll hér að neðan er hægt að nýta til að breyta gildi breytanna

    def change_start(self, new_start):
        self.__start_date = new_start

    def change_end(self, new_end):
        self.__end_date = new_end

    def change_insurance(self, new_insurance):
        self.__insurance = new_insurance

    def change_car(self, new_car):
        self.__car = new_car

    def change_ssn(self, new_ssn):
        self.__ssn = new_ssn

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

    def __repr__(self):
        '''
        Skrifar upplýsingar um pöntun
        '''
        return "{},{},{},{},{},{},{}".format(self.__start_date,
                                             self.__order_number,
                                             self.__name,
                                             self.__ssn, self.__car,
                                             self.__car_number, self.__status)
