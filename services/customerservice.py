from repositories import CustomerRepo


class CustomerService(object):
    def __init__(self):
        pass

    def make_customer(self, name, SSN, creditcard_number, phone_number):
        customer = CustomerRepo.add_customer(
            name, SSN, creditcard_number, phone_number)
        return customer

    def remove_customer(self, SSN):
        CustomerRepo.remove_customer(SSN)

    def change_card(self, SSN, new_credit):
        CustomerRepo.change_card_number(SSN, new_credit)

    def change_phone_number(self, SSN, new_phone_number):
        CustomerRepo.change_card_number(SSN, new_phone_number)

    def change_name(self, SSN, new_name):
        CustomerRepo.change_name(SSN, new_name)

    def show_list(self):

        pass

    def show_orders():
        pass
