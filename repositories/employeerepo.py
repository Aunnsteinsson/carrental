from models.employee import Employee
import csv
NOTENDANAFN = 0
NAFN = 1
LYKILORD = 2
HLUTVERK = 3
SIMI = 4
HEIMILISFANG = 5


class EmployeeRepo(object):
    def __init__(self):
        """Employee er hér sama og employers_dict sem var notað til að
        lesa gögn um starfsmenn og færa þau í dictionary"""
        self.__employee = self.employee_dict()

    def employee_dict(self):
        """Tekur við data úr employee og les það inn í dictionary
         þar sem notendanafn er notað sem key og hver starfsmaður
         er hluti af Employee klasanum og notað sem value"""
        employee_dict = {}
        with open("./data/employees.csv", "r") as employees_file:
            csv_reader = csv.reader(employees_file)
            next(csv_reader)
            for employee in csv_reader:
                employee_class = Employee(
                    employee[NOTENDANAFN], employee[NAFN], employee[LYKILORD],
                    employee[HLUTVERK], employee[SIMI], employee[HEIMILISFANG])
                username = employee[NOTENDANAFN]
                employee_dict[username] = employee_class
        return employee_dict

    def get_employees(self):
        return self.__employee

    def add_employee(self, employee):
        with open("./data/employees.csv", "a+") as employees_file:
            employees_file.write(employee.__repr__() + "\n")

    def change_info_of_employee(self, username_of_user_to_change, choice,
                                new_value):
        employee_to_store = []
        with open("./data/employees.csv", "r") as employees_input:
            with open("./data/employees_edit.csv", "w",
                      newline="")as employees_output:
                csv_reader = csv.reader(employees_input)
                csv_writer = csv.writer(employees_output)
                for row in csv_reader:
                    if row[1] != username_of_user_to_change:
                        csv_writer.writerow(row)
                    else:
                        employee_to_store.append(row)
                        employee_to_store[choice-1] = new_value
                        csv_writer.writerow(employee_to_store)

        with open("./data/employees.csv", "w",
                  newline="") as new_employees_file:
            with open("./data/employees_edit.csv", "r") as new_employees_edit:
                csv_reader = csv.reader(new_employees_edit)
                csv_writer = csv.writer(new_employees_file)
                for row in csv_reader:
                    csv_writer.writerow(row)

    def remove_employee(self, username):
        with open("./data/employees.csv", "r") as employees_input:
            with open("./data/employees_edit.csv", "w",
                      newline="") as employees_output:
                csv_reader = csv.reader(employees_input)
                csv_writer = csv.writer(employees_output)
                for row in csv_reader:
                    if row:
                        if row[0] != username:
                            csv_writer.writerow(row)

        with open("./data/employees.csv", "w",
                  newline="") as new_employees_file:
            with open("./data/employees_edit.csv", "r") as new_employees_edit:
                csv_reader = csv.reader(new_employees_edit)
                csv_writer = csv.writer(new_employees_file)
                for row in csv_reader:
                    if row:
                        csv_writer.writerow(row)
