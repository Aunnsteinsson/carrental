# Teddi á að massa þennan fæl
from repositories.carrepo import CarRepo
from models.car import Car


class CarService(object):
    # Sér um aðgerðir með bíla
    def __init__(self):
        self.__car_repo = CarRepo()

    def make_car(self, car):
        # Nýskráir bíl í kerfi
        self.__car_repo.add_car(car)

    def remove_car(self, licence_plate):
        # Fjarlægir bíl úr kerfi
        self.__car_repo.remove_car(licence_plate)

    def change_status(self, licence_plate, new_status):
        # Breytir stöðu bíls
        self.__car_repo.change_status(licence_plate, new_status)

    def show_cars(self, licence_plate):
        # Fall sem sýnir lista af bílum
        self.__car_repo.get_car(licence_plate)

    def get_list_of_cars(self, a_type, status):
        # Heavy copyright Denni
        list = self.__car_repo.get_all_cars()
        car_list = []
        for car in list:
            if len(car) == 3:
                if car[1] in a_type and car[2] in status:
                    car_class = Car(
                        car[0], car[1], car[2])
                    car_list.append(car_class)
        string = ""
        for car in car_list:
            car_string = car.__str__()
            string += car_string + "\n"
        return string
