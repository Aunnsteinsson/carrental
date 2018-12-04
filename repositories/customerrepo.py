from models.customer import Customer
import csv


class CustomerRepo(object):
    def __init__(self):
        self.__customer = {}

    def add_customer(self):
        pass

    def remove_customer(self):
        pass

    def get_car(self):
        pass


with open("./data/customers.csv") as customer_file:
    csv_reader = csv.reader(customer_file)
    for line in csv_reader:
        print(line)
