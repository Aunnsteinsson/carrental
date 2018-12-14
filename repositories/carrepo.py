from models.car import Car
import csv
LICENCE_PLATE = 0
A_TYPE = 1
STATUS = 2
DAYS = 3


class CarRepo(object):
    """Sér um geymslu á bílum innan kerfis """

    def __init__(self):
        self.__price = self.price_dict()
        self.__car = self.car_dict()

    def car_dict(self):
        """Fall sem les upp úr cars.csv og skilar dict með bílnúmeri
        sem key og instance af car klasanum sem value"""
        car_dict = {}
        with open("./data/cars.csv", "r", encoding="utf-8") as car_file:
            csv_reader = csv.reader(car_file)
            for car in csv_reader:
                if car[0] != "licence_plate":
                    car_class = Car(
                        car[LICENCE_PLATE],
                        car[A_TYPE],
                        self.__price,
                        car[STATUS],
                        car[DAYS])
                    licence_plate = car[LICENCE_PLATE]
                    car_dict[licence_plate] = car_class
        return car_dict

    def price_dict(self):
        """Fall sem les upp úr price.csv og skilar dict með verðandlagi
        sem key og verði sem value"""
        price_dict = {}
        with open("./data/price_list.csv", "r",
                  encoding="utf-8") as price_file:
            csv_reader = csv.reader(price_file)
            for price in csv_reader:
                if price[0] != "gerd_bils":
                    price_dict[price[0]] = price[1]
            return price_dict

    def add_car(self, new_car):
        """Bætir bíl inn í dictið"""
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

    def remove_car(self, licence_plate):
        """Eyðir bíl úr geymslu"""
        del self.__car[licence_plate]

    def save_car_data(self):
        """Tekur upplýsingar úr dict og skrifar það í car_dict"""
        list_of_cars = ["licence_plate", "a_type", "status", "days"]
        with open("./data/cars.csv", "w", newline="",
                  encoding="utf-8") as car_file:
            csv_writer = csv.writer(car_file)
            csv_writer.writerow(list_of_cars)
            for _, info in self.__car.items():
                temp_car_string = info.__repr__()
                temp_car_list = temp_car_string.split(",")
                csv_writer.writerow(temp_car_list)

    def save_price_data(self):
        """Tekur upplýsingar úr dict og skrifar það í price_dict"""
        list_of_prices = ["gerd_bils", "verd"]
        with open("./data/price_list.csv", "w", newline="",
                  encoding="utf-8") as price_file:
            csv_writer = csv.writer(price_file)
            csv_writer.writerow(list_of_prices)
            for the_type, the_price in self.__price.items():
                listi = [the_type, the_price]
                csv_writer.writerow(listi)

    def get_car_prices(self):
        """skilar dict með verðandlgi sem key og verði á
         bílum eða tryggingum sem key"""
        return self.__price

    def change_price_of_type(self, a_type, new_price):
        """Tekur inn nýtt verð og verðandlag og breytir verðinu
         á verðandlaginu"""
        self.__price[a_type] = new_price
