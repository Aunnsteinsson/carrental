import csv

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
    list_of_employees = []
    with open("./data/customers.csv", "r") as customer_file:
        csv_reader = csv.reader(customer_file)
        for line in csv_reader:
            if line[0] != "kennitala":
                list_of_employees.append(line)
    return list_of_employees


list_of_employees = overview_customers()


def get_indicators(risk_factor_list):
    ''' Extracts and returns the individual indicators from the given list '''
    kennitala = [lst[KENNITALA] for lst in list_of_employees]
    nafn = [lst[NAFN] for lst in list_of_employees]
    simi = [lst[SIMI] for lst in list_of_employees]
    kreditkort = [lst[KREDIT] for lst in list_of_employees]
    return kennitala, nafn, simi, kreditkort


blabla = get_indicators(list_of_employees)
print(blabla)
