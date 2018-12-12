import csv


class Order(object):
    '''Klasi fyrir pantanir. Breytur í þessum klasa eru pöntunarnúmer, upphafsdagur,
    skiladagur, nafn viðskiptavinar, kennitala viðskiptavinar, bíltegund, bílnúmer, 
    staða bíls og hvort pöntun innihaldi aukatryggingu eður ei.
    Klasinn inniheldur föll til að hægt sé að kalla á breytur eða breyta þeim.
    Hægt er að fá __str__ á tvo mismunandi vegu.'''

    def __init__(self, order_number, list_of_dates, ssn, name, car_number, price, insurance=False, discount=0.000):
        self.__order_number = order_number
        self.__list_of_dates = self.dates_string_to_list(list_of_dates)
        self.__ssn = ssn
        self.__name = name
        self.__car_number = car_number
        self.__insurance = insurance
        self.__discount = discount
        self.__price = price

    # Föll hér að neðan er hægt að kalla í til að nálgast breyturnar

    def get_order_number(self):
        return self.__order_number

    def get_discount(self):
        return self.__discount

    def change_discount(self, new_discount):
        self.__discount = new_discount

    def get_licence_plate(self):
        return self.__car_number

    def get_price(self):
        return self.__price

    def change_price(self, new_price):
        self.__price = new_price

    def get_duration(self):
        return self.__list_of_dates

    def dates_list_to_string(self):
        list_of_dates = self.__list_of_dates
        string_of_dates = ""
        for date in list_of_dates:
            string_of_dates += str(date) + ":"
        return string_of_dates

    def dates_string_to_list(self, dates_string):
        try:
            str(dates_string)
            date_list = dates_string.strip(":").split(':')
            return date_list
        except Exception:
            return dates_string

    def get_insurance(self):
        return self.__insurance

    def get_car(self):
        return self.__car_number

    def change_duration(self, new_list):
        self.__list_of_dates = [str(day) for day in new_list]

    def get_ssn(self):
        return self.__ssn

    # Föll hér að neðan er hægt að nýta til að breyta gildi breytanna

    def change_list_of_days(self, new_list):
        self.__list_of_dates = new_list

    def change_insurance(self, new_insurance):
        self.__insurance = new_insurance

    def change_name(self, new_name):
        self.__name = new_name

    def change_car(self, new_car):
        self.__car_number = new_car

    def change_ssn(self, new_ssn):
        self.__ssn = new_ssn

    def __str__(self, info_to_print=0):
        '''Annars vegar skilar upplýsingum prentuðum með án kennitölu.
        Það er nýtt þegar pöntun er sköðuð út frá Kennitölu.
        Hins vegar skilar upplýsingum með kommu á milli, notað til skráningar
        í geymslu.'''
        start_date = self.__list_of_dates[0]
        end_date = self.__list_of_dates[-1]
        if info_to_print == 1:
            return "\t {:11}| {:14}| {:10}| {:9}| {:10}{}{}".format(
                start_date, self.__order_number, self.__name, self.__ssn, self.__car_number,
                self.__car_number, end_date)
        else:
            return "\t {:11}| {:14}| {:25}| {:11}| {:10}| {:9}| {:10}".format(
                start_date, self.__order_number, self.__name,
                self.__ssn, self.__car_number, self.__car_number, end_date)

    def __repr__(self):
        '''
        Skrifar upplýsingar um pöntun
        '''
        string_of_dates = self.dates_list_to_string()
        return "{},{},{},{},{},{},{},{}".format(self.__order_number,
                                                string_of_dates,
                                                self.__ssn, self.__name,
                                                self.__car_number, self.__price,
                                                self.__insurance, self.__discount)
