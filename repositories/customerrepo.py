from models.customer import Customer
import csv
KENNITALA = 0
NAFN = 1
SIMI = 2
KREDIT = 3


class CustomerRepo(object):
    def __init__(self):
        self.__customer = customer_dict

    def add_customer(self, customer):
        with open("./data/customers.csv", "a+") as customer_file:
            ssn = customer.get__ssn()
            name = customer.get_name()
            phone_number = customer.get_phone_number()
            creditcard_number = customer.get_creditcard_number()
            customer_file.write("{},{},{},{}\n".format(
                ssn, name, phone_number, creditcard_number))

    def remove_customer(self, ssn):
        with open("./data/customers.csv", "r") as customer_input:
            with open("./data/customers_edit.csv", "w", newline="") as customer_output:
                csv_reader = csv.reader(customer_input)
                csv_writer = csv.writer(customer_output)
                for row in csv_reader:
                    if row:
                        if row[0] != ssn:
                            csv_writer.writerow(row)

        with open("./data/customers.csv", "w", newline="") as new_customer_file:
            with open("./data/customers_edit.csv", "r") as new_customer_edit:
                csv_reader = csv.reader(new_customer_edit)
                csv_writer = csv.writer(new_customer_file)
                for row in csv_reader:
                    if row:
                        csv_writer.writerow(row)

    def get_customer(self, ssn):
        with open("./data/customers.csv", "r") as customer_file:
            csv_reader = csv.reader(customer_file)
            for row in csv_reader:
                if row:
                    if row[0] == ssn:
                        return row
        return None

    def overview_customers(self):
        return self.__customer

    def customer_dict(self):
        customer_dict = {}
        with open("./data/customers.csv", "r") as customer_file:
            csv_reader = csv.reader(customer_file)
            for customer in csv_reader:
                if customer[KENNITALA] != "kennitala":
                    customer_class = Customer(
                        customer[KENNITALA], customer[NAFN], customer[SIMI], customer[KREDIT])
                    kennitala = customer[KENNITALA]
                    customer_dict[kennitala] = customer_class
        return customer_dict

    """def get_indicators(list_of_employees):
    Tekur við lista og flokkar eftir kennitölu, nafni, símanr og kreditkorti
    kennitala = [lst[KENNITALA] for lst in list_of_employees]
    nafn = [lst[NAFN] for lst in list_of_employees]
    simi = [lst[SIMI] for lst in list_of_employees]
    kreditkort = [lst[KREDIT] for lst in list_of_employees]
    return kennitala, nafn, simi, kreditkort"""


"""with open("./data/customers.csv") as customer_file:
    csv_reader = csv.DictReader(customer_file)
    for line in csv_reader:
        print(line)"""
