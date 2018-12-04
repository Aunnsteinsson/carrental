from models.customer import Customer
import csv


class CustomerRepo(object):
    def __init__(self):
        self.__customer = {}

    def add_customer(self, customer):
        with open("./data/customers.csv", "a+") as customer_file:
            ssn = Customer.get__ssn()
            name = Customer.get_name()
            phone_number = Customer.get_phone_number()
            creditcard_number = Customer.get_creditcard_number()
            customer_file.write("{},{},{},{}".format(
                ssn, name, phone_number, creditcard_number))

    def remove_customer(self):
        pass

    def get_car(self):
        pass


with open("./data/customers.csv") as customer_file:
    csv_reader = csv.DictReader(customer_file)
    for line in csv_reader:
        print(line)
