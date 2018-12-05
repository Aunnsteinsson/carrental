from models.customer import Customer
import csv


class CustomerRepo(object):
    def __init__(self):
        self.__customer = {}

    def add_customer(self, customer):
        with open("./data/customers.csv", "a+") as customer_file:
            ssn = customer.get__ssn()
            name = customer.get_name()
            phone_number = customer.get_phone_number()
            creditcard_number = customer.get_creditcard_number()
            customer_file.write("\n{},{},{},{}".format(
                ssn, name, phone_number, creditcard_number))

    def remove_customer(self):
        pass

    def get_customer(self):
        pass


"""with open("./data/customers.csv") as customer_file:
    csv_reader = csv.DictReader(customer_file)
    for line in csv_reader:
        print(line)"""
