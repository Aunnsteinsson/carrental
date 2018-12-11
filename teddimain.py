from repositories.carrepo import CarRepo
from services.carservice import CarService
from models.car import Car
from ui.BossUi import BossUI
from ui.AdminUi import AdminUI

""" geymsla = CarRepo()
Bíll = Car("AA111","Jeppi")


geymsla.change_status("AA111","Laus")


with open("./data/cars.csv", "r") as car_input:
    for row in car_input:
        row.split(",")
        print(row)



#a_type og status """


k1 = AdminUI("User1", "Kerfisstjóri")
k1.main_menu()