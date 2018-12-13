# Teddi á að massa þennan fæl
from repositories.carrepo import CarRepo
from models.car import Car


class CarService(object):
    """ Sér um aðgerðir með bíla """

    def __init__(self):
        self.__car_repo = CarRepo()

    def make_car(self, new_car):
        """ Nýskráir bíl í kerfi """
        self.__car_repo.add_car(new_car)
        self.save_cars()

    def remove_car(self, licence_plate):
        """ Fjarlægir bíl úr kerfi """
        self.__car_repo.remove_car(licence_plate)
        self.save_cars()

    def change_status(self, licence_plate, new_status):
        """ Breytir stöðu bíls """
        car = self.__car_repo.get_car(licence_plate)
        car.change_status(new_status)
        self.save_cars()

        """ self.__car_repo.change_status(licence_plate, new_status) """

    def show_cars(self, licence_plate):
        """ Fall sem sýnir upplýsingar um bíl """
        return self.__car_repo.get_car(licence_plate)

    def change_status(self, new_status, car):
        car.change_status(new_status)
        self.__car_repo.save_car_data()

    def get_list_of_cars(self, a_type, status):
        """ Fall sem sækir lista af öllum bílum """
        dict = self.__car_repo.get_all_cars()
        string = ""
        for _, item in dict.items():
            type_of_car = item.get_type()
            wherabouts = item.get_wherabouts()
            #status_of_car = item.get_status()
            if type_of_car in a_type and wherabouts in status:  # and status_of_car in status:
                car_string = item.__str__()
                string += car_string + "\n"
        return string

    def get_all_cars(self):
        dict = self.__car_repo.get_all_cars()
        list_of_cars = []
        for _, value in dict.items():
            list_of_cars.append(value)
        return list_of_cars

    def get_car_prices(self):
        car_prices = self.__car_repo.get_car_prices()
        return car_prices

    def change_price_of_type(self, a_type, new_price):
        self.__car_repo.change_price_of_type(a_type, new_price)
        self.__car_repo.save_price_data()

    def save_cars(self):
        self.__car_repo.save_car_data()
