class Employee(object):
    """Þessi klasi er með nokkrar breytur, (phonenumber og address eru default
     því það er ekki bráðnauðsynlegar upplýsingar) og heimilar það að þær
     breytur séu sóttar og þeim breytt með föllum"""

    def __init__(self, username, password,
                 name, address, phonenumber, emp_type):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__address = address
        self.__phone_number = phonenumber
        self.__emp_type = emp_type

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
        return self.__emp_type

    def get_phone_number(self):
        return self.__phone_number

    def __str__(self):
        """Her ery prentaðar allar upplýsingar nema password
         því það eiga ekki allir að hafa aðgang að passwordi"""
        return "{:<25s}| {:<10s}| {:<25s}| {:<10s}| {:<12s}\
        ".format(self.__name, self.__username, self.__address,
                 self.__phone_number, self.__emp_type)

    def __repr__(self, admin=0):
        """Hér eru allar upplýsingar prentaðar.
         Þetta er gert fyrir admin, einnig skilar
         fallið upplýsingum með kommu á milli
         ef það er gefið 1
         """
        if admin == 0:
            return "{:<10s}| {:<10s}| {:<25s}| "\
                "{:<25s}| {:<10s}| {:<12s}".format(self.__username,
                                                   self.__password,
                                                   self.__name,
                                                   self.__address,
                                                   self.__phone_number,
                                                   self.__emp_type)
        else:
            return "{},{},{},{},{},{}".format(self.__username,
                                              self.__password,
                                              self.__name,
                                              self.__address,
                                              self.__phone_number,
                                              self.__emp_type)
