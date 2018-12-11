from repositories.carrepo import CarRepo
from services.carservice import CarService
from models.car import Car
from ui.BossUi import BossUI
from ui.AdminUi import AdminUI
""" ordabok = {}
ordabok["Jeppi"] = 4444444
geymsla = CarRepo()
Bíll = Car("AA111","Jeppi", ordabok )
verd = Bíll.price_vehicle()

print(verd)
 """
""" geymsla.change_status("AA111","Laus") """


""" with open("./data/cars.csv", "r") as car_input:
    for row in car_input:
        row.split(",")
        print(row)
 """


#a_type og status """


k1 = BossUI("User1", "Yfirmaður")
k1.main_menu() 