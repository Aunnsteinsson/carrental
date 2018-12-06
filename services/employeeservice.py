from repositories.employeerepo import EmployeeRepo


class EmployeeService(object):
    def __init__(self):
        self.__employee_repo = EmployeeRepo()

    def add_employee(self, employee):
        self.__employee_repo.add_employee(employee)

    def get_employees(self, boss_or_admin=0):
        list_with_data_in_string = []
        employee_list = self.__employee_repo.get_employees()
        for value in employee_list:
            username = value[0]
            password = value[1]
            name = value[2]
            address = value[3]
            phone = value[4]
            position = value[5]

            if boss_or_admin == 0:
                list_with_data_in_string.append("\
{:<25s}| {:<10s}| {:<25s}| {:<10s}| {:<12s}".format(
                    name, username, address, phone, position))
            else:
                list_with_data_in_string.append("\
{:<10s}| {:<10s}| {:<25s}| {:<25s}| {:<10s}| {:<12s}".format(
                    username, password, name, address, phone, position))
        return list_with_data_in_string

    def remove_employee(self, username):
        self.__employee_repo.remove_employee(username)

    def change_employee(self, username, choice, new_value):
        self.__employee_repo.change_info_of_employee(
            username, choice, new_value)
