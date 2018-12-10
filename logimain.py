from ui.AdminUi import AdminUI
from models.order import Order
from repositories.orderrepo import OrderRepo

start = "2112"
end = "2323"
car = "Jeppi"
insur = "no"

repo = OrderRepo()

# print(repo.order_dict())

order_number = "001"

order = Order(order_number, start, end, car, insur)
print(order)

repo.add_order(order_number, order)

# print("repr: {}".format(order_info))

# print("new: {}".format(repo.add_order(order_number, order_info)))

new_orders = repo.get_orders()
print(new_orders)

save = input("Save")
if save == "1":
    repo.save_new_orders()
# # pontun = Order("001", "upphf", "endir", "jepps", "no")


# # k1 = AdminUI("logigeir")

# # k1.main_menu()
