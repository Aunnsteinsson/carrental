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

    def remove_customer(self, ssn):
        with open("./data/customers.csv", "r") as customer_input:
            with open("./data/customers_edit.csv", "w") as customer_output:
                csv_reader = csv.reader(customer_input)
                csv_writer = csv.writer(customer_output)
                for row in csv_reader:
                    if row[0] != ssn:
                        csv_writer.writerow(row)

        with open("./data/customers.csv", "w") as new_customer_file:
            with open("./data/customers_edit.csv", "r") as new_customer_edit:
                csv_reader = csv.reader(new_customer_edit)
                csv_writer = csv.writer(new_customer_file)
                for row in csv_reader:
                    csv_writer.writerow(row)

    def get_customer(self):
        pass


"""with open("./data/customers.csv") as customer_file:
    csv_reader = csv.DictReader(customer_file)
    for line in csv_reader:
        print(line)"""
