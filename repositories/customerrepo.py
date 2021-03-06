from models.customer import Customer
import csv
SSN = 0
NAME = 1
PHONE = 2
CREDIT = 3


class CustomerRepo(object):
    def __init__(self):
        """Customer er hér sama og customer dict sem var notað til að
         lesa gögn um viðskiptavini og færa þau í dictionary"""
        self.__customer = self.customer_dict()

    def customer_dict(self):
        """Tekur við data úr customer.py og les það inn í dictionary
         þar sem kennitalan er notuð sem key og hver customer er hluti af
         customer klasanum er notað sem value"""
        customer_dict = {}
        with open("./data/customers.csv", "r",
                  encoding="utf-8") as customer_file:
            csv_reader = csv.reader(customer_file)
            next(csv_reader)
            for customer in csv_reader:
                customer_class = Customer(
                    customer[SSN], customer[NAME], customer[PHONE],
                    customer[CREDIT])
                ssn_number = customer[SSN]
                customer_dict[ssn_number] = customer_class
        return customer_dict

    def add_customer(self, new_customer):
        """Tekur við kennitölu nýs viðskiptavinar og bætir honum við í
         customer dictionary"""
        ssn = new_customer.get_ssn()
        self.__customer[ssn] = new_customer

    def remove_customer(self, ssn):
        """Finnur key sem er kennitala viðskiptavinar, ef key passar við
         kennitöluna sem við starfsmaður leitar að þá eyðum við þeim
         viðskiptavini út úr dictionary"""
        for kennitala, _ in self.__customer.items():
            if kennitala == ssn:
                del self.__customer[ssn]
                return self.__customer
        return False

    def get_customer(self, ssn):
        """Ef að kennitalan sem starfsmaður leitar að passar við
         kennitölu í dictionary, þá skilum við þeim viðskiptavini. Annars
         skilum við False"""
        for kennitala, _ in self.__customer.items():
            if kennitala == ssn:
                return self.__customer[ssn]
        return False

    def overview_customers(self):
        """Skilar viðskiptavinayfirliti"""
        return self.__customer

    def overwrite_customer_data(self):
        """Þegar keyrslu er hætt, þá skrifum við inn allar upplýsingar aftur inn
         í datafile sem heldur utan um viðskiptavini og
         þannig breytum við skránni"""
        list_of_customers = ["kennitala", "nafn",
                             "simanumer", "kreditkortanumer"]
        with open("./data/customers.csv", "w", newline="",
                  encoding="utf-8") as customer_file:
            csv_writer = csv.writer(customer_file)
            csv_writer.writerow(list_of_customers)
            for _, customer in self.__customer.items():
                temp_list = customer.__repr__().split(",")
                csv_writer.writerow(temp_list)
