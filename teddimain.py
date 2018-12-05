from repositories.carrepo import CarRepo
from models.car import Car

geymsla = CarRepo()
Bíll = Car("AA111","Jeppi")

geymsla.remove_car(Bíll)

with open("./data/cars_edit.csv", "r") as car_input:
    for row in car_input:
        row.split(",")
        print(row)
