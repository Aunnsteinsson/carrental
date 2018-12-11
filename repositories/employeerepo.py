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
        """
         Kallar í employee_dict fallið og gefur self.__employee dictionaryið
        """
        self.__employee = self.employees_dict()

    def get_employees(self):
        '''
         skilar öllum starfmönnum
        '''
        return self.__employee

    def add_employee(self, username, password,
                     name, address, phonenumber,
                     emp_type):
        '''
         Bætir við staki af employee í __employee
        '''
        self.__employee[username] = Employee(
            username, password, name, address, phonenumber, emp_type)

    def remove_employee(self, username):
        '''
         Tekur stak úr __employee
        '''
        del self.__employee[username]

    def change_info_of_employee(self, username_of_user_to_change):
        '''
         Sendir __employee sem á að breyta til
        '''
        for username, _ in self.__employee.items():
            if username == username_of_user_to_change:
                return self.__employee[username]
        return False

    def save(self):
        '''
         Afritar stak af hlutum í __employee og skráir það í employees.csv
        '''
        list_of_employees = [
            "Notendanafn,lykilord,nafn,heimilisfang,simi,hlutverk"]
        with open("./data/employees.csv", "w", newline="") as employees_file:
            csv_writer = csv.writer(employees_file)
            csv_writer.writerow(list_of_employees)
            for _, info in self.__employee.items():
                employees_string = info.__repr__(1).split(",")
                csv_writer.writerow(employees_string)

    def employees_dict(self):
        """
         Tekur við data úr employee.csv og les það inn í dictionary
         þar sem notendanafn er notað sem key og hver starfsmaður
         er hluti af Employee klasanum og er notaður sem value
        """
        dict_for_emp = {}
        with open("./data/employees.csv", "r") as employees_file:
            csv_reader = csv.reader(employees_file)
            next(csv_reader)
            for employee in csv_reader:
                employee_class = Employee(
                    employee[USERNAME], employee[PASSWORD], employee[NAME],
                    employee[ADDRESS], employee[PHONE], employee[EMP_TYPE])
                username = employee[USERNAME]
                dict_for_emp[username] = employee_class
        return dict_for_emp
