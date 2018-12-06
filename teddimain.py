from repositories.carrepo import CarRepo
from services.carservice import CarService
from models.car import Car

geymsla = CarRepo()
Bíll = Car("AA111","Jeppi")

service = CarService()

listi = service.get_list()

print(listi)

with open("./data/cars_edit.csv", "r") as car_input:
    for row in car_input:
        row.split(",")
        print(row)


