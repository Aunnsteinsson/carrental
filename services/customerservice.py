from repositories.customerrepo import CustomerRepo
from models.customer import Customer


class CustomerService(object):
    def __init__(self):
        self.__customer_repo = CustomerRepo()

    def test_values(self, ssn, name, phone_number, credit_card_number):
        new_ssn = ssn.replace(" ", "")
        new_ssn = new_ssn.replace("-", "")
        try:
            int(new_ssn)
        except ValueError:
            return "Kennitalan {} er ekki samþykkt".format(ssn)
        if len(new_ssn) < 9:
            return "Kennitalan {} er ekki samþykkt".format(ssn)
        if len(name) < 2:
            return "Nafnið {} er ekki samþykkt".format(name)
        new_phone_number = phone_number.replace(" ", "")
        new_phone_number = new_phone_number.replace("-", "")
        new_phone_number = new_phone_number.replace("+", "")
        try:
            int(new_phone_number)
        except ValueError:
            return "Simanúmerið {} er ekki samþykkt".format(phone_number)
        new_credit_card_number = credit_card_number.replace(" ", "")
        new_credit_card_number = new_credit_card_number.replace("-", "")
        try:
            int(new_credit_card_number)
        except ValueError:
            return "Kortanúmerið {} er ekki samþykkt".format(
                credit_card_number)
        if len(new_credit_card_number) != 16:
            return "Kortanúmerið {} er ekki samþykkt".format(
                credit_card_number)
        return ""

    def make_customer(self, customer):
        self.__customer_repo.add_customer(customer)
        self.save_program()

    def find_customer(self, ssn):
        customer = self.__customer_repo.get_customer(ssn)
        if customer == None:
            return False
        return customer

    def remove_customer(self, ssn):
        self.__customer_repo.remove_customer(ssn)
        self.save_program()

    def change_card(self, ssn, new_credit):
        customer = self.__customer_repo.get_customer(ssn)
        customer.change_credit_card(new_credit)
        self.save_program()

    def change_phone_number(self, ssn, new_phone_number):
        customer = self.__customer_repo.get_customer(ssn)
        customer.change_phone_number(new_phone_number)
        self.save_program()

    def change_name(self, ssn, new_name):
        customer = self.__customer_repo.get_customer(ssn)
        customer.change_name(new_name)
        self.save_program()

    def get_list(self):
        dict = self.__customer_repo.overview_customers()
        string = ""
        for kennitala, value in dict.items():
            customer_string = value.__str__()
            string += customer_string + "\n"
        return string

    def show_orders(self):
        pass

    def save_program(self):
        self.__customer_repo.overwrite_customer_data()
