from models.employee import Employee
import csv
USERNAME = 0
PASSWORD = 1
NAME = 2
ADDRESS = 3
PHONE = 4
EMP_TYPE = 5


class EmployeeRepo(object):
    def __init__(self):
        """Employee er hér sama og employers_dict sem var notað til að
        lesa gögn um starfsmenn og færa þau í dictionary"""
        self.__employee = self.employee_dict()
        self.__employee_changes_and_additions = self.__employee

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
                    employee[USERNAME], employee[PASSWORD], employee[NAME],
                    employee[ADDRESS], employee[PHONE], employee[EMP_TYPE])
                username = employee[USERNAME]
                employee_dict[username] = employee_class
        return employee_dict

    def get_employees(self):
        '''skilar öllum starfmönnum'''
        return self.__employee

    def add_employee(self, username, password,
                     name, address="N/A", phonenumber="N/A",
                     emp_type="soludeild"):
        self.__employee_changes_and_additions[username] = username, password, name, address, phonenumber, emp_type

    def change_info_of_employee(self, username_of_user_to_change, choice,
                                new_value):
        for username, _ in self.__employee.items():
            if username == username_of_user_to_change:
                return self.__employee[username]

    def remove_employee(self, username):
        pass
