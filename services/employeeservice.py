from models.employee import Employee


class EmployeeService(object):
    def __init__(self):
        pass

    def change_info(self, choice, new_value):
        if choice == "1":
            Employee.change_name(new_value)
        elif choice == "2":
            Employee.change_username(new_value)
        elif choice == "3":
            Employee.change_password(new_value)
        elif choice == "4":
            Employee.change_type(new_value)
        elif choice == "5":
            Employee.change_address(new_value)
        else:
            Employee.change_phone_number(new_value)
