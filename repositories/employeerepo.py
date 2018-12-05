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
            employees_file.write(employee.__repr__() + "/n")

    def change_info(self, username_of_user_to_change, choice, new_value):
        employee_to_store = []
        with open("./data/employees.csv", "r") as employees_input:
            with open("./data/employees_edit.csv", "w") as employees_output:
                csv_reader = csv.reader(employees_input)
                csv_writer = csv.writer(employees_output)
                for row in csv_reader:
                    if row[0] != username_of_user_to_change:
                        csv_writer.writerow(row)
                    else:
                        employee_to_store.append(row)
                        employee_to_store[choice] = new_value
                        csv_writer.writerow(employee_to_store)

        with open("./data/employees.csv", "w") as new_employees_file:
            with open("./data/employees_edit.csv", "r") as new_employees_edit:
                csv_reader = csv.reader(new_employees_edit)
                csv_writer = csv.writer(new_employees_file)
                for row in csv_reader:
                    csv_writer.writerow(row)

    def remove_employee(self, username):
        with open("./data/employees.csv", "r") as employees_input:
            with open("./data/employees_edit.csv", "w") as employees_output:
                csv_reader = csv.reader(employees_input)
                csv_writer = csv.writer(employees_output)
                for row in csv_reader:
                    if row[0] != username:
                        csv_writer.writerow(row)

        with open("./data/employees.csv", "w") as new_employees_file:
            with open("./data/employees_edit.csv", "r") as new_employees_edit:
                csv_reader = csv.reader(new_employees_edit)
                csv_writer = csv.writer(new_employees_file)
                for row in csv_reader:
                    csv_writer.writerow(row)
