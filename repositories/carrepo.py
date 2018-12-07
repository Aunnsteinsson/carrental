from models.car import Car
import csv


class CarRepo(object):
    """Sér um geymslu á bílum innan kerfis """
    def __init__(self):
        self.__car = {}

    def add_car(self, car):
        """Bætir bíl inn í geymslu"""
        with open("./data/cars.csv", "a+") as car_file:
            licence_plate = car.get_licence_plate()
            a_type = car.get_type()
            status = car.get_status()
            car_file.write("{},{},{}\n".format(
                licence_plate, a_type, status))

    def get_car(self, licence_plate):
        """Sækir upplýsingar um bíl. Kallar á __str__ fall úr class Car"""
        with open("./data/cars.csv", "r") as car_file:
            csv_reader = csv.reader(car_file)
            for row in csv_reader:
                if row:
                    if row[0] == licence_plate:
                        return row
        return None

    def get_all_cars(self):
        """Sækir lista af öllum bílum"""
        list_of_cars = []
        with open("./data/cars.csv", "r") as car_file:
            csv_reader = csv.reader(car_file)
            for line in csv_reader:
                if line[0] != "númeraplata":
                    list_of_cars.append(line)
        return list_of_cars

    def remove_car(self, licence_plate):
        """Eyðir bíl úr geymslu"""
        with open("./data/cars.csv", "r") as car_input:
            with open("./data/cars_edit.csv", "w", newline="") as car_output:
                csv_reader = csv.reader(car_input)
                csv_writer = csv.writer(car_output)
                for row in csv_reader:
                    if row:
                        if row[0] != licence_plate:
                            csv_writer.writerow(row)

        with open("./data/cars.csv", "w", newline="") as new_car_file:
            with open("./data/cars_edit.csv", "r") as new_car_edit:
                csv_reader = csv.reader(new_car_edit)
                csv_writer = csv.writer(new_car_file)
                for row in csv_reader:
                    if row:
                        csv_writer.writerow(row)

    def change_status(self, licence_plate, new_status):
<<<<<<< Updated upstream
        """Breytir stöðu bíls"""
=======
        # Breytir stöðu bíls
>>>>>>> Stashed changes
        with open("./data/cars.csv", "r") as car_input:
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
                        csv_writer.writerow(row)
