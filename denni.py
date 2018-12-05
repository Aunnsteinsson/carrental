import csv


def bla(x):
    with open("./data/customers.csv", "r") as customer_input:
        with open("./data/customers_edit.csv", "w") as customer_output:
            csv_reader = csv.reader(customer_input)
            csv_writer = csv.writer(customer_output)
            for row in csv_reader:
                if row[0] != x:
                    csv_writer.writerow(row)


bla("1234567890")
