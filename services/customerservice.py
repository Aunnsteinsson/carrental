from repositories.customerrepo import CustomerRepo


class CustomerService(object):
    def __init__(self):
        self.__customer_repo = CustomerRepo()

    def make_customer(self, customer):
        self.__customer_repo.add_customer(customer)

    def find_customer(self, ssn):
        # self.__customer_repo.  # Eitthvað fall
        pass

    def remove_customer(self, ssn):
        self.__customer_repo.remove_customer(ssn)

    def change_card(self, ssn, new_credit):
        self.__customer_repo.change_card_number(ssn, new_credit)

    def change_phone_number(self, ssn, new_phone_number):
        self.__customer_repo.change_card_number(ssn, new_phone_number)

    def change_name(self, ssn, new_name):
        self.__customer_repo.change_name(ssn, new_name)

    def get_list(self):
        list = self.__customer_repo.get_customers()
        string = ""
        for customer in listi:
            string += customer + "\n"
        return string

    def show_orders():
        pass


k = CustomerService()
