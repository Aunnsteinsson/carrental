class Customer(object):
    '''custumer klassi, tekur inn kennitölu, nafn, síma og kreditkorta
    númer'''

    def __init__(self, ssn, name, phone_number, creditcard_number):
        self.__ssn = ssn
        self.__name = name
        self.__phone_number = phone_number
        self.__creditcard_number = creditcard_number

    # föllin hér að neðan eru hugsuð til að sækja
    # einhverja eina sérstaka breytu
    def get__ssn(self):
        return self.get__ssn

    def get_name(self):
        return self.__name

    def get_phone_number(self):
        return self.__phone_number

    def get_creditcard_number(self):
        return self.__creditcard_number

    def __str__(self):
        # sting fall sem prentar allt nema kreditkorta upplýsingar
        return "Kennitala: {} Nafn: {} Sími: {}".format(
            self.__ssn, self.__name, self.__phone_number)

    def __repr__(self):
        # fall tileinkað kerfisstjóra til að sækja allar
        # upplýsingar notanda
        return "{},{},{},{},{}".format(
            self.__ssn, self.__name, self.__phone_number,
            self.__creditcard_number)
