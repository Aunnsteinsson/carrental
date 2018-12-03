class Car(object):
    def __init__(self, licence_plate, a_type):
        self.__licence_plate = licence_plate
        self.__a_type = a_type

    def __str__(self):
        pass

    def get_licence_plate(self):
        return self.__licence_plate

    def get_type(self):
        return self.__a_type

    def __repr__(self):
        pass
