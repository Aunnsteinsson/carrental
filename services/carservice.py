#Teddi á að massa þennan fæl
from repositories.carrepo import CarRepo

class CarService(object):
    #Sér um aðgerðir með bíla
    def __init__(self):
        self.__car_repo = CarRepo

    def make_car(self):
        #Nýskráir bíl í kerfi
        self.__car_repo.add_car(car)
    
    def remove_car(self):
        #Fjarlægir bíl úr kerfi
        self.__car_repo.remove_car(license_plate)
    
    def change_status(self):
        #Breytir stöðu bíls
        self.__car_repo.change_status(license_plate, new_status)

    def show_cars(self):
        #Fall sem sýnir lista af bílum
        self.__car_repo.get_car()