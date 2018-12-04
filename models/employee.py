class Employee(object):
    """Þessi klasi er með nokkrar breytur, (phonenumber og address eru default því það er ekki bráðnauðsynlegar upplýsingar) og heimilar það að þær breytur
    séu sóttar og þeim breytt með föllum"""

    def __init__(self, username, password, type, name, phonenumber="N/A", address="N/A"):
        self.__username = username
        self.__name = name
        self.__password = password
        self.__type = type
        self.__phone_number = phonenumber
        self.__address = address
    # Hér eru nokkur get föll sett inn til að nálgast breyturnar í fallinu

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_type(self):
        return self.__type

    def get_phone_number(self):
        return self.__phone_number
    # Hér eru nokkur change föll til að breyta breytunum.

    def change_name(self, new_name):
        self.__name = new_name

    def change_username(self, new_username):
        self.__username = new_username

    def change_password(self, new_password):
        self.__password = new_password

    def change_type(self, new_type):
        self.__type = new_type

    def change_address(self, new_address):
        self.__address = new_address

    def change_phone_number(self, new_phone_number):
        self.__phone_number = new_phone_number

    def __str__(self):
        """Her ery prentaðar allar upplýsingar nema password því það eiga ekki allir að hafa aðgang að passwordi"""
        return "Nafn: {}, Notendanafn: {}, Staða: {}, Símanúmer: {}, Heimilisfang: {}".format(self.__name, self.__username, self.__type, self.__phone_number, self.__address)

    def __repr__(self):
        """Hér eru allar upplýsingar prentaðar með kommu á milli. Þetta er gert fyrir admin"""
        return "{},{},{},{},{},{}".format(self.__name, self.__username, self.__password, self.__type, self.__phone_number, self.__address)
