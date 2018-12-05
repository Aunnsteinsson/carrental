import csv


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
    list_of_employees = []
    with open("./data/customers.csv", "r") as customer_file:
        csv_reader = csv.reader(customer_file)
        for line in csv_reader:
            list_of_employees.append(line)
    return list_of_employees


bla = overview_customers()
print(bla)
