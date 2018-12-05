from repositories.carrepo import CarRepo
from models.car import Car

geymsla = CarRepo()
Bíll = Car("AA111","Jeppi")

geymsla.add_car(Bíll)

with open("./data/cars.csv", "r") as car_input:
    for row in car_input:
        row.split(",")
        print(row)
