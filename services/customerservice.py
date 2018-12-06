from repositories.customerrepo import CustomerRepo
from models.customer import Customer


class CustomerService(object):
    def __init__(self):
        self.__customer_repo = CustomerRepo()

    def make_customer(self, customer):
        self.__customer_repo.add_customer(customer)

    def find_customer(self, ssn):
        customer_list = self.__customer_repo.get_customer(ssn)
        if customer_list == None:
            return None
        customer = Customer(
            customer_list[0], customer_list[1], customer_list[2],
            customer_list[3])
        return customer

    def remove_customer(self, ssn):
        self.__customer_repo.remove_customer(ssn)

    def change_card(self, ssn, new_credit):
        customer_list = self.__customer_repo.get_customer(ssn)
        customer_class = Customer(
            customer_list[0], customer_list[1], customer_list[2], new_credit)
        self.remove_customer(ssn)
        self.make_customer(customer_class)

    def change_phone_number(self, ssn, new_phone_number):
        customer_list = self.__customer_repo.get_customer(ssn)
        customer_class = Customer(
            customer_list[0], customer_list[1], new_phone_number, customer_list[3])
        self.remove_customer(ssn)
        self.make_customer(customer_class)

    def change_name(self, ssn, new_name):
        customer_list = self.__customer_repo.get_customer(ssn)
        customer_class = Customer(
            customer_list[0], new_name, customer_list[2], customer_list[3])
        self.remove_customer(ssn)
        self.make_customer(customer_class)

    def get_list(self):
        dict = self.__customer_repo.overview_customers()
        string = ""
        for kennitala, value in dict.items():
            customer_string = value.__str__()
            string += customer_string + "\n"
        return string

    def show_orders():
        pass
