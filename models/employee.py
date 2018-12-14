class Employee(object):
    """
     Breytur í þessum klasa eru notendanafn, lykilorð, nafn, heimilisfang
     sími og hlutverk starfsmanns, einnig inniheldur klasin föll sem eru gerð
     til að kalla á breytur eða breyta breytum, __str__ fallið er fyrir
     yfirmann og __repr__ er fyrir kerfisstjóra, það er einnig hægt að gefa
     __repr__ fallinu einhvað annað en 0 og þú skilar öllum breytum skiptum
     með kommu
    """

    def __init__(self, username, password,
                 name, address, phonenumber, emp_type):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__address = address
        self.__phone_number = phonenumber
        self.__emp_type = emp_type

    def __str__(self):
        """
         Skilar öllum breytum nema lykilorði, þetta fall er fyrir yfirmann
        """
        return "{:<25s}| {:<10s}| {:<25s}| {:<10s}| {:<12s}\
        ".format(self.__name, self.__username, self.__address,
                 self.__phone_number, self.__emp_type)

    def __repr__(self, admin=0):
        """
         Skilar öllum breytum.
         Þetta er gert fyrir admin, einnig skilar
         fallið upplýsingum með kommu á milli
         ef það er gefið 1/eitthvað annað en 0
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

    # Hér eru nokkur get föll sett inn til að nálgast breyturnar í fallinu

    def get_name(self):
        """skilar nafni starfsmanns"""
        return self.__name

    def get_address(self):
        """Skilar heimilisfangi starfsmanns"""
        return self.__address

    def get_username(self):
        """Skilar notendanafni starfsmanns"""
        return self.__username

    def get_password(self):
        """Skilar lykilorði starfsmanns"""
        return self.__password

    def get_type(self):
        """Skilar starfsheiti starfsmanns"""
        return self.__emp_type

    def get_phone_number(self):
        """Skilar símanúmeri Starfsmanns"""
        return self.__phone_number

    # Hér eru nokkur change föll sett inn til að breyta breytum í fallinu
    def change_name(self, new_name):
        """Tekur inn nafn og breytir nafni starfsmanns í það nafn2"""
        self.__name = new_name

    def change_address(self, new_address):
        """Tekur inn heimilsifang og breytir heimilisfangi stafsmanns í það heimilisfang"""
        self.__address = new_address

    def change_password(self, new_password):
        """Tekur inn lykilorð og breytir lykilorði starfsmanns í það lykilorð"""
        self.__password = new_password

    def change_phone_number(self, new_phone_number):
        """Tekur inn símanúmer og breytir símanúmeri starfsmanns í það símanúmer"""
        self.__phone_number = new_phone_number
