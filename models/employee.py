class Employee(object):
    def __init__(self, username, name, password, type="Sölumaður"):
        self.__username = username
        self.__name = name
        self.__password = password
        self.__type = type
    
    def get_name(self):
        return self.__name
    
    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def get_type(self):
        return self.__type

    def change_name(self, new_name):
        self.__name = new_name
    
    def change_username(self, new_username):
        self.__username = new_username

    def change_password(self, new_password):
        self.__password = password
    
    def change_type(self, new_type):
        self.__type = new_type
    
    def __str__(self):
        return "Nafn: {}, Notendanafn: {}, Staða: {}".format(self.__name, self.__username, self.__type)
    
    def __repr__(self):
        return "{},{},{},{}".format(self.__name, self.__username, self.__password, self.__type)