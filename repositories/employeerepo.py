from models.employee import Employee
import csv


class EmployeeRepo(object):
    def __init__(self):
        self.__employee = {}

    def get_employees(self):
        employees = []
        with open("./data/employees.csv", "r") as employees_file:
            csv_reader = csv.reader(employees_file)
            for line in csv_reader:
                employees.append(line)
        return employees

    def add_employee(self, employee):
        with open("./data/employees.csv", "a+") as employees_file:
            employees_file.write(employee.__repr__() + "\n")

    def change_info(self, choice, new_value):
        pass

    def remove_employee(self):
        pass
