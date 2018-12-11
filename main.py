from ui.loginUi import LoginUI
from ui.AdminUi import AdminUI
from ui.BossUi import BossUI
from ui.SalesmanUi import SalesmanUI

user = LoginUI()

emp_type, username = user.main_menu()

if emp_type == "admin":
    user = AdminUI(username)
elif emp_type == "yfirmadur":
    user = BossUI(username)
elif emp_type == "soludeild":
    user = SalesmanUI(username)

user.main_menu()
