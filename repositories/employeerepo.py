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
        '''skilar öllum starfmönnum'''
        return self.__employee

    def add_employee(self, username, password,
                     name, address="N/A", phonenumber="N/A",
                     emp_type="soludeild"):
        Employee(username, password, name, address, phonenumber, emp_type)

    def change_info_of_employee(self, username_of_user_to_change, choice,
                                new_value):
        for username, _ in self.__employee.items():
            if username == username_of_user_to_change:
                return self.__employee[username]

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
