from repositories.employeerepo import EmployeeRepo


class EmployeeService(object):
    def __init__(self):
        """Kallar á EmployeRepo klasan í employeerepo.py"""
        self.__employee_repo = EmployeeRepo()

    def check_phone(self, phone_number):
        new_phone_number = phone_number.replace(" ", "")
        new_phone_number = new_phone_number.replace("-", "")
        new_phone_number = new_phone_number.replace("+", "")
        try:
            int(new_phone_number)
            return new_phone_number
        except ValueError:
            return "Simanúmerið {} er ekki samþykkt".format(phone_number)

    def add_employee(self, username, password, name,
                     address, phonenumber, emp_type):
        """Bætir við nýjum starfsmanni inn í orðabókina í employee_repo"""
        self.__employee_repo.add_employee(
            username, password, name, address, phonenumber, emp_type)

    def get_employees(self, boss_or_admin=0):
        """Kallar á get_employees í EmployeRepo klasann og sækir
         __str__ fyrir BossUI eða __repr__ fyrir AdminUi ef fallið
         er gefið eitthvað annað en núll"""
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
        """Tekur við notendanafni og skilar True ef change_info_of_employee
          skilar staki af notandanum"""
        employees_dict = self.__employee_repo.change_info_of_employee(
            usern_to_check)
        if not employees_dict:
            return False
        else:
            return True

    def remove_employee(self, username):
        """Kallar á remove_employee í EmployeeRepo klasanum
         og tekur stakið úr orðabókinni"""
        self.__employee_repo.remove_employee(username)

    def change_employee(self, username, choice, new_value):
        """Tekur við staki af starfsmanni og kallar á fall sem hentar í
         employee líkaninu"""
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
        """Kallar á save í EmployeeRepo sem afritar orðabókina í
         employees.csv"""
        self.__employee_repo.save()
