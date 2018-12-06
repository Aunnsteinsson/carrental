from repositories.employeerepo import EmployeeRepo


class EmployeeService(object):
    def __init__(self):
        self.__employee_repo = EmployeeRepo()

    def add_employee(self, employee):
        self.__employee_repo.add_employee(employee)

    def get_employees(self, boss_or_admin=0):
        # employee_list =
        return self.__employee_repo.get_employees()

        # if boss_or_admin == 0:
        #     pass
        # else:
        #     return"{:<10s}| {:<10s}| {:<10s}| {:<10s}|\
        #      {:<10s}| {:<20s}".format(
        #         username, password, name, position, phone, address)

    def remove_employee(self, username):
        self.__employee_repo.remove_employee(username)

    def change_employee(self, username, choice, new_value):
        self.__employee_repo.change_info_of_employee(
            username, choice, new_value)
