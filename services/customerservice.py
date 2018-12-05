from repositories.customerrepo import CustomerRepo


class CustomerService(object):
    def __init__(self):
        self.__customer_repo = CustomerRepo

    def make_customer(self, customer):
        self.__customer_repo.add_customer(customer)

    def remove_customer(self, ssn):
        self.__customer_repo.remove_customer(ssn)

    def change_card(self, ssn, new_credit):
        self.__customer_repo.change_card_number(ssn, new_credit)

    def change_phone_number(self, ssn, new_phone_number):
        self.__customer_repo.change_card_number(ssn, new_phone_number)

    def change_name(self, ssn, new_name):
        self.__customer_repo.change_name(ssn, new_name)

    def show_list(self):
        self.__customer_repo.get_customers()

    def show_orders():
        pass


k = CustomerService()
