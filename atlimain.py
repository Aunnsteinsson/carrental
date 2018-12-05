from datetime import date
from models.customer import Customer
from models.order import Order
from models.car import Car
from models.employee import Employee
from services.carservice import CarService
from services.customerservice import CustomerService
from services.employeeservice import EmployeeService
from services.orderservice import OrderService
HOMECOMMANDS = ["h", "H", "s", "S"]


class SalesmanUI(object):
    """Klasi sem sér um viðmót Sölumanns og ferðir þar um"""

    def __init__(self):
        self.__employee_service = EmployeeService()

    def main(self):
        a_customer = Employee("AtliSD", "abc1234",
                              "Atli Dagur")
        self.__employee_service.add_employee(a_customer)
        username = input("username: ")
        numer = input("skrifaðu 3")
        nytt_nafn = input("skrifaðu nýja nafnið: ")
        self.__employee_service.change_employee(username, numer, nytt_nafn)
        username = ("username: ")
        self.__employee_service.remove_employee(username)


k1 = SalesmanUI()
k1.main()
