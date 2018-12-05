#Teddi á að massa þennan fæl
from repositories.carrepo import CarRepo

class CarService(object):
    #Sér um aðgerðir með bíla
    def __init__(self):
        self.__car_repo = CarRepo()

    def make_car(self, car):
        #Nýskráir bíl í kerfi
        self.__car_repo.add_car(car)
    
    def remove_car(self, licence_plate):
        #Fjarlægir bíl úr kerfi
        self.__car_repo.remove_car(licence_plate)
    
    def change_status(self, licence_plate, new_status):
        #Breytir stöðu bíls
        self.__car_repo.change_status(licence_plate, new_status)

    def show_cars(self):
        #Fall sem sýnir lista af bílum
        self.__car_repo.get_car()