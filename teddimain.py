from repositories.carrepo import CarRepo
from services.carservice import CarService
from models.car import Car

geymsla = CarRepo()
Bíll = Car("AA111","Jeppi")

geymsla.add_car(Bíll)

geymsla.change_status("AA111","Laus")


with open("./data/cars.csv", "r") as car_input:
    for row in car_input:
        row.split(",")
        print(row)



#a_type og status