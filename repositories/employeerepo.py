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
        """tekur global employee_dict og gefur self.__employee dictionaryið"""
        global employee_dict
        self.__employee = employee_dict

    def get_employees(self):
        '''skilar öllum starfmönnum'''
        return self.__employee

    def add_employee(self, username, password,
                     name, address, phonenumber,
                     emp_type):
        '''bætir við staki af employee í __employee'''
        self.__employee[username] = Employee(
            username, password, name, address, phonenumber, emp_type)

    def remove_employee(self, username):
        '''tekur stak úr __employee'''
        del self.__employee[username]

    def change_info_of_employee(self, username_of_user_to_change):
        '''sendir __employee sem á að breyta til'''
        for username, _ in self.__employee.items():
            if username == username_of_user_to_change:
                del self.__employee[username]
                return self.__employee
        return False

    def save(self):
        '''afritar stak af hlutum í __employee og skráir það í employees.csv'''
        list_of_employees = [
            "Notendanafn,lykilord,nafn,heimilisfang,simi,hlutverk"]
        with open("./data/employees.csv", "w", newline="") as employees_file:
            csv_writer = csv.writer(employees_file)
            csv_writer.writerow(list_of_employees)
            for _, info in self.__employee.items():
                employees_string = info.__repr__(1).split(",")
                csv_writer.writerow(employees_string)


def employees_dict():
    """Tekur við data úr employee og les það inn í dictionary
        þar sem notendanafn er notað sem key og hver starfsmaður
        er hluti af Employee klasanum og notað sem value"""
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


employee_dict = employees_dict()
