import time
import os
from ui.LoginUi import LoginUI
from ui.AdminUi import AdminUI
from ui.BossUi import BossUI
from ui.SalesmanUi import SalesmanUI


system_is_on = True
user = LoginUI()

while system_is_on:
    os.system("cls" if os.name == "nt" else "clear")
    try:
        emp_type, username = user.main_menu()
        if emp_type == "admin":
            user = AdminUI(username, "Kerfisstjóri")
        elif emp_type == "yfirmadur":
            user = BossUI(username, "Yfirmaður")
        elif emp_type == "soludeild":
            user = SalesmanUI(username, "Söludeild")

        user.main_menu()

    except TypeError:
        print("Notendanafn eða lykilorð rangt, vinsamlegast \
hafðu samband við kerfisstjóra")
        time.sleep(2)
