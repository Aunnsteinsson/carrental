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
        self.__employee = self.employees_dict()

    def get_employees(self):
        """Skilar dict sem er með notendanöfn sem key og staki af
         klasanum sem value"""
        return self.__employee

    def add_employee(self, username, password,
                     name, address, phonenumber,
                     emp_type):
        """Bætir við staki af starfsmanna klasanum í starfmanna dictið"""
        self.__employee[username] = Employee(
            username, password, name, address, phonenumber, emp_type)

    def remove_employee(self, username):
        """Eyðir starfsmanni úr dict"""
        del self.__employee[username]

    def change_info_of_employee(self, username_of_user_to_change):
        """tekur inn stak af starfmanni og breytir stakinu á notendanafns key
         í það stak"""
        for username, _ in self.__employee.items():
            if username == username_of_user_to_change:
                return self.__employee[username]
        return False

    def save(self):
        """Les upplýsingar úr dictinu og setur það inn í csv skjalið"""
        list_of_employees = [
            "Notendanafn,lykilord,nafn,heimilisfang,simi,hlutverk"]
        with open("./data/employees.csv", "w", newline="",
                  encoding="utf-8") as employees_file:
            csv_writer = csv.writer(employees_file)
            csv_writer.writerow(list_of_employees)
            for _, info in self.__employee.items():
                employees_string = info.__repr__(1).split(",")
                csv_writer.writerow(employees_string)

    def employees_dict(self):
        """Tekur við gögnum úr employee.csv og les það inn í dict
         þar sem notendanafn er notað sem lykill og hver starfsmaður
         er hluti af Employee klasanum og er notaður sem gildi"""
        dict_for_emp = {}
        with open("./data/employees.csv", "r",
                  encoding="utf-8") as employees_file:
            csv_reader = csv.reader(employees_file)
            next(csv_reader)
            for employee in csv_reader:
                employee_class = Employee(
                    employee[USERNAME], employee[PASSWORD], employee[NAME],
                    employee[ADDRESS], employee[PHONE], employee[EMP_TYPE])
                username = employee[USERNAME]
                dict_for_emp[username] = employee_class
        return dict_for_emp
