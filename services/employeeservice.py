from repositories.employeerepo import EmployeeRepo


class EmployeeService(object):
    def __init__(self):
        self.__employee_repo = EmployeeRepo()

    def add_employee(self, employee):
        self.__employee_repo.add_employee(employee)

    def get_employees(self, boss_or_admin=0):
        # komið
        employees_dict = self.__employee_repo.get_employees()
        employees = ""
        for _, value in employees_dict.items():
            if boss_or_admin == 0:
                employee_string = value.__str__()
            else:
                employee_string = value.__repr__()
            employees += employee_string + "\n"
        return employees

    def remove_employee(self, username):
        self.__employee_repo.remove_employee(username)

    def change_employee(self, username, choice, new_value):
        self.__employee_repo.change_info_of_employee(
            username, choice, new_value)
