import csv
from models.customer import Customer
KENNITALA = 0
NAFN = 1
SIMI = 2
KREDIT = 3

"""def bla(x):
    with open("./data/customers.csv", "r") as customer_input:
        with open("./data/customers_edit.csv", "w") as customer_output:
            csv_reader = csv.reader(customer_input)
            csv_writer = csv.writer(customer_output)
            for row in csv_reader:
                if row[0] != x:
                    csv_writer.writerow(row)


bla("1234567890")"""


"""def bla(ssn):

    with open("./data/customers.csv", "r") as customer_file:
        csv_reader = csv.reader(customer_file)
        for row in csv_reader:
            if row[0] == ssn:
                return row


joi = bla("1234")
print(joi)
"""


def overview_customers():
    #list_of_employees = []
    customer_dict = {}
    with open("./data/customers.csv", "r") as customer_file:
        csv_reader = csv.reader(customer_file)
        for customer in csv_reader:
            if customer[0] != "kennitala":
                customer_class = Customer(
                    customer[KENNITALA], customer[NAFN], customer[SIMI], customer[KREDIT])
                kennitala = customer[0]
                customer_dict[kennitala] = customer_class

    print(customer_dict["siggi"])
    # return list_of_employees


overview_customers()
#list_of_customers = overview_customers()


"""def customer_dict(list_of_customers):
    customer_list = list_of_customers
    customer_dict = {}
    for customer in customer_list:
        customer_class = Customer(
            customer[KENNITALA], customer[NAFN], customer[SIMI], customer[KREDIT])
        kennitala = customer[0]
        customer_dict[kennitala] = customer_class
    return customer_dict"""


"""bla = customer_dict(list_of_customers)
print(bla)"""


"""def get_indicators(risk_factor_list):
    ''' Extracts and returns the individual indicators from the given list '''
    kennitala = [lst[KENNITALA] for lst in list_of_employees]
    nafn = [lst[NAFN] for lst in list_of_employees]
    simi = [lst[SIMI] for lst in list_of_employees]
    kreditkort = [lst[KREDIT] for lst in list_of_employees]
    return kennitala, nafn, simi, kreditkort


blabla = get_indicators(list_of_employees)
print(blabla)
"""
