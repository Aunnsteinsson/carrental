from repositories.customerrepo import CustomerRepo


class CustomerService(object):
    def __init__(self):
        pass

    def make_customer(self, name, ssn, creditcard_number, phone_number):
        customer = CustomerRepo.add_customer(
            name, ssn, creditcard_number, phone_number)
        return customer

    def remove_customer(self, ssn):
        CustomerRepo.remove_customer(ssn)

    def change_card(self, ssn, new_credit):
        CustomerRepo.change_card_number(ssn, new_credit)

    def change_phone_number(self, ssn, new_phone_number):
        CustomerRepo.change_card_number(ssn, new_phone_number)

    def change_name(self, ssn, new_name):
        CustomerRepo.change_name(ssn, new_name)

    def show_list(self):
        CustomerRepo.get_customers()

    def show_orders():
        pass


k = CustomerService()
