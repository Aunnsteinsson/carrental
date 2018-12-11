from models.car import Car
import csv
LICENCE_PLATE = 0
A_TYPE = 1
STATUS = 2

class CarRepo(object):
    """Sér um geymslu á bílum innan kerfis """
    def __init__(self):
        self.__price = self.price_dict()        
        self.__car = self.car_dict()

    def car_dict(self):
        car_dict = {}
        with open("./data/cars.csv", "r") as car_file:
            csv_reader = csv.reader(car_file)
            for car in csv_reader:
                if car[0] != "licence_plate":
                    car_class = Car(car[LICENCE_PLATE], car[A_TYPE], self.__price, car[STATUS])
                    licence_plate = car[LICENCE_PLATE]
                    car_dict[licence_plate] = car_class
        return car_dict

    def price_dict(self):
        price_dict = {}
        with open("./data/price_list.csv", "r") as price_file:
            csv_reader = csv.reader(price_file)
            for price in csv_reader:
                if price[0] != "gerd_bils":
                    price_dict[price[0]] = price[1]
            return price_dict    

    def add_car(self, new_car):
        """Bætir bíl inn í geymslu"""
        licence_plate = new_car.get_licence_plate()
        self.__car[licence_plate] = new_car

    def get_car(self, licence_plate):
        """Sækir upplýsingar um bíl. Kallar á __str__ fall úr class Car"""
        for licence, value in self.__car.items():
            if licence == licence_plate:
                return self.__car[licence_plate]
        return False

    def get_all_cars(self):
        """ Sækir bíla fyrir útlistun af bílum """
        return self.__car
        
        """ list_of_cars = []
        with open("./data/cars.csv", "r") as car_file:
            csv_reader = csv.reader(car_file)
            for line in csv_reader:
                if line[0] != "númeraplata":
                    list_of_cars.append(line)
        return list_of_cars """

    def remove_car(self, licence_plate):
        """Eyðir bíl úr geymslu"""
        del self.__car[licence_plate]

    def change_status(self, licence_plate, new_status):
        """Finnur __bíl sem á að breyta og sendir í service"""

        """ with open("./data/cars.csv", "r") as car_input:
            with open("./data/cars_edit.csv", "w", newline="") as car_output:
                csv_reader = csv.reader(car_input)
                csv_writer = csv.writer(car_output)
                for row in csv_reader:
                    if row:
                        if row[0] == licence_plate:
                            row[2] = (new_status)
                        csv_writer.writerow(row)

        with open("./data/cars.csv", "w", newline="") as new_car_file:
            with open("./data/cars_edit.csv", "r") as new_car_edit:
                csv_reader = csv.reader(new_car_edit)
                csv_writer = csv.writer(new_car_file)
                for row in csv_reader:
                    if row:
                        csv_writer.writerow(row) """

    def save_car_data(self):
        list_of_cars = ["licence_plate", "a_type", "status"]
        with open ("./data/cars.csv", "w", newline="") as car_file:
            csv_writer = csv.writer(car_file)
            csv_writer.writerow(list_of_cars)
            for _, info in self.__car.items():
                temp_car_string = info.__repr__()
                temp_car_list = temp_car_string.split(",")
                csv_writer.writerow(temp_car_list)

    def save_price_data(self):
        list_of_prices = ["gerd_bils", "verd"]
        with open ("./data/price_list.csv", "w", newline="") as price_file:
            csv_writer = csv.writer(price_file)
            csv_writer.writerow(list_of_prices)
            for the_type, the_price in self.__price.items():
                listi = [the_type, the_price]
                csv_writer.writerow(listi)

    def get_car_prices(self):
        return self.__price

    def change_price_of_type(self, a_type, new_price):
        self.__price[a_type] = new_price
