from models.employee import Employee
import csv


class EmployeeRepo(object):
    def __init__(self):
        self.__employee = {}

    def get_employee(self):
        pass

    def add_employee(self, employee):
        with open("./data/employees.csv", "a+") as employees_file:
            username = employee.get__username()
            password = employee.get__password()
            position = employee.get__type()
            name = employee.get__name()
            phone = employee.get__phone_number()
            address = employee.get_address()
            employees_file.write("\n{},{},{},{},{},{}".format(
                username, password, position, name, phone, address))

    def change_info(self, choice, new_value):
        pass

    def remove_employee(self):
        pass
