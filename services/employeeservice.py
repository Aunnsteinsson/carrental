from repositories.employeerepo import EmployeeRepo


class EmployeeService(object):
    def __init__(self):
        self.__employee_repo = EmployeeRepo()

    def add_employee(self, username, password, name,
                     address, phonenumber, emp_type):
        self.__employee_repo.add_employee(
            username, password, name, address, phonenumber, emp_type)

    def get_employees(self, boss_or_admin=0):
        '''kallar á employee klasann og sækir
         __str__ fyrir BossUI eða __repr fyrir AdminUi'''
        employees_dict = self.__employee_repo.get_employees()
        employees = ""
        for _, value in employees_dict.items():
            if boss_or_admin == 0:
                employee_string = value.__str__()
            else:
                employee_string = value.__repr__()
            employees += employee_string + "\n"
        return employees

    def check_if_valid(self, usern_to_check):
        employees_dict = self.__employee_repo.get_employees()
        for username, _ in employees_dict.items():
            if username == usern_to_check:
                return True
        return False

    def remove_employee(self, username):
        self.__employee_repo.remove_employee(username)

    def change_employee(self, username, choice, new_value):
        employee = self.__employee_repo.change_info_of_employee(username)
        if choice == "1":
            employee.change_password(new_value)
        elif choice == "2":
            employee.change_name(new_value)
        elif choice == "3":
            employee.change_address(new_value)
        else:
            employee.change_phone_number(new_value)

    def save_employees(self):
        self.__employee_repo.save()
