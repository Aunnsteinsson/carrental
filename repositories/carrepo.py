# Teddi á að sjá um þennan fæl
# Nota CSV module, setja alla bíla í dictionary. Geyma stórt dictionary og notar nokkra lykla til að sækja allar upplýsingar.
from models.car import Car
import csv

class CarRepo(object):
    # Sér um geymslu á bílum innan kerfis
    def __init__(self):
        self.__car = {}

    def add_car(self, car):
        # Bætir bíl inn í geymslu
        with open("./data/cars.csv", "a+") as car_file:
            licence_plate = car.get__licence_plate()
            a_type = car.get_type()
            status = car.get_status()
            car_file.write("\n{},{},{}".format(
                licence_plate, a_type, status))

    def get_car(self):
        # Sækir upplýsingar um bíl. Kallar á __str__ fall úr class Car
        pass

    def remove_car(self, licence_plate):
        # Eyðir bíl úr geymslu
        with open("./data/cars.csv", "r") as car_input:
            with open("./data/customers_edit.csv", "w") as car_output:
                csv_reader = csv.reader(car_input)
                csv_writer = csv.writer(car_output)
                for row in csv_reader:
                    if row[0] != licence_plate:
                        csv_writer.writerow(row)

        with open("./data/car.csv", "w") as new_car_file:
            with open("./data/cars_edit.csv", "r") as new_car_edit:
                csv_reader = csv.reader(new_car_edit)
                csv_writer = csv.writer(new_car_file)
                for row in csv_reader:
                    csv_writer.writerow(row)

    def __str__(self):
        # Prentar út upplýsingar um alla bíla
        pass
