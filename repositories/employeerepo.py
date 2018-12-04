from models.employee import Employee


class EmployeeRepo(object):
    def __init__(self):
        pass

    def get_employee(self):
        pass

    def add_employee(self):
        username = input("Notendanafn: ")
        password = input("Lykilorð: ")
        name = input("Nafn: ")
        address = input("Heimilisfang: ")
        phonenumber = input("Sími: ")
        emp_type = input("(S)öludeil, (y)firmaður eða (k)erfisstjóri: ")
        Employee(username, password, name,
                 address, phonenumber, emp_type)
