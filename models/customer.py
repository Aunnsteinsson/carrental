class Customer(object):
    '''
     Breytur í þessum klasa eru kennitala, nafn, sími, og kreditkorta númer
     einnig inniheldur klasin föll sem eru gerð til að kalla á breytur eða 
     breyta breytum, __str__ fallið inniheldur ekki kreditkorta númerið en
      __repr__ gerir það
    '''

    def __init__(self, ssn, name, phone_number, creditcard_number):
        self.__ssn = ssn
        self.__name = name
        self.__phone_number = phone_number
        self.__creditcard_number = creditcard_number

    # Hér eru nokkur get föll sett inn til að nálgast breyturnar í fallinu
    def get_ssn(self):
        return self.__ssn

    def get_name(self):
        return self.__name

    def get_phone_number(self):
        return self.__phone_number

    def get_creditcard_number(self):
        return self.__creditcard_number

    # Hér eru nokkur get föll sett inn til að breyta breytunum í fallinu
    def change_name(self, new_name):
        self.__name = new_name

    def change_phone_number(self, new_phone_number):
        self.__phone_number = new_phone_number

    def change_credit_card(self, new_card_number):
        self.__creditcard_number = new_card_number

    def __str__(self):
        '''
         String fall sem prentar allar breytur nema
         kreditkorta upplýsingar
        '''
        return "{:11}| {:30}| {:9}".format(
            self.__ssn, self.__name, self.__phone_number)

    def __repr__(self):
        '''
         String fall sem prentar allar breytur
        '''
        return "{},{},{},{}".format(
            self.__ssn, self.__name, self.__phone_number,
            self.__creditcard_number)
