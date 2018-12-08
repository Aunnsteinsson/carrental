from repositories.employeerepo import EmployeeRepo


class EmployeeService(object):
    def __init__(self):
        self.__employee_repo = EmployeeRepo()

    def add_employee(self, username, password, name, address, phonenumber, emp_type):
        self.__employee_repo.add_employee(
            username, password, name, address, phonenumber, emp_type)

    def get_employees(self, boss_or_admin=0):
        '''kallar á Employee klasann og sækir 
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

    def remove_employee(self, username):
        self.__employee_repo.remove_employee(username)

    def change_employee(self, username, choice, new_value):
        pass
    #     object_of_user = self.__employee_repo.change_info_of_employee(
    #         username, choice, new_value)
    #     userdata = object_of_user.__repr__(1)
    #     #gera remove hér og síðan setja inn nýjan með nýju uppl.
