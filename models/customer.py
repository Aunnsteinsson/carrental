class Customer(object):
    '''Custumer klassi, tekur inn kennitölu, nafn, síma og kreditkorta
    númer'''

    def __init__(self, ssn, name, phone_number, creditcard_number):
        self.__ssn = ssn
        self.__name = name
        self.__phone_number = phone_number
        self.__creditcard_number = creditcard_number

    def change_name(self, new_name):
        self.__name = new_name

    def change_phone_number(self, new_phone_number):
        self.__phone_number = new_phone_number

    def change_credit_card(self, new_card_number):
        self.__creditcard_number = new_card_number

    # Föllin hér að neðan eru hugsuð til að sækja
    # einhverja eina sérstaka breytu
    def get__ssn(self):
        return self.__ssn

    def get_name(self):
        return self.__name

    def get_phone_number(self):
        return self.__phone_number

    def get_creditcard_number(self):
        return self.__creditcard_number

    def __str__(self):
        '''String fall sem prentar allt nema kreditkorta upplýsingar'''
        return "{:>20}{:>30}{:>20}".format(
            self.__ssn, self.__name, self.__phone_number)

    def __repr__(self):
        '''Fall tileinkað kerfisstjóra til að sækja allar
         upplýsingar notanda'''
        return "{},{},{},{}".format(
            self.__ssn, self.__name, self.__phone_number,
            self.__creditcard_number)
