from ui.loginUi import LoginUI
from ui.AdminUi import AdminUI

user = LoginUI()

emp_type, username = user.main_menu()

if emp_type == 'admin':
    user = AdminUI(username)
    user.main_menu()
