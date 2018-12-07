from models.customer import Customer
import csv
KENNITALA = 0
NAFN = 1
SIMI = 2
KREDIT = 3


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
        with open("./data/customers.csv", "r") as customer_file:
            csv_reader = csv.reader(customer_file)
            for customer in csv_reader:
                if customer[KENNITALA] != "kennitala":
                    customer_class = Customer(
                        customer[KENNITALA], customer[NAFN], customer[SIMI], customer[KREDIT])
                    kennitala = customer[KENNITALA]
                    customer_dict[kennitala] = customer_class
        return customer_dict

    def add_customer(self, new_customer):
        """Tekur við kennitölu nýs viðskiptavinar og bætir honum við í 
        customer dictionary"""
        ssn = new_customer.get__ssn()
        self.__customer[ssn] = new_customer

    def remove_customer(self, ssn):
        """Finnur key sem er kennitala viðskiptavinar, ef key passar við 
        kennitöluna sem við starfsmaður leitar að þá eyðum við þeim
        viðskiptavini út úr dictionary"""
        for kennitala, value in self.__customer.items():
            if kennitala == ssn:
                del self.__customer[ssn]
                return self.__customer
        return False

    def get_customer(self, ssn):
        """Ef að kennitalan sem starfsmaður leitar að passar við
        kennitölu í dictionary, þá skilum við þeim viðskiptavini. Annars
        skilum við False"""
        for kennitala, value in self.__customer.items():
            if kennitala == ssn:
                return self.__customer[ssn]
        return False

    def overview_customers(self):
        """Skilar viðskiptavinayfirliti"""
        return self.__customer

    def overwrite_customer_data(self):
        """Þegar keyrslu er hætt, þá skrifum við inn allar upplýsingar aftur inn
        i datafile sem heldur utan um viðskiptavini og þannig breytum við skránni"""
        with open("./data/customers.csv", "w", newline="") as customer_file:
            csv_writer = csv.writer(customer_file)
            for customer in self.__customer:
                csv_writer.writerow(Customer.__repr__(customer))


#####################################GEYMSLA####################################################

    """def get_indicators(list_of_employees):
    Tekur við lista og flokkar eftir kennitölu, nafni, símanr og kreditkorti
    kennitala = [lst[KENNITALA] for lst in list_of_employees]
    nafn = [lst[NAFN] for lst in list_of_employees]
    simi = [lst[SIMI] for lst in list_of_employees]
    kreditkort = [lst[KREDIT] for lst in list_of_employees]
    return kennitala, nafn, simi, kreditkort"""

    """def add_customer(self, customer):
            with open("./data/customers.csv", "a+") as customer_file:
                ssn = customer.get__ssn()
                name = customer.get_name()
                phone_number = customer.get_phone_number()
                creditcard_number = customer.get_creditcard_number()
                customer_file.write("{},{},{},{}\n".format(
                    ssn, name, phone_number, creditcard_number))"""

    """def get_customer(self, ssn):
            with open("./data/customers.csv", "r") as customer_file:
                csv_reader = csv.reader(customer_file)
                for row in csv_reader:
                    if row:
                        if row[0] == ssn:
                            return row
            return None"""

    """def remove_customer(self, ssn):
        with open("./data/customers.csv", "r") as customer_input:
            with open("./data/customers_edit.csv", "w", newline="") as customer_output:
                csv_reader = csv.reader(customer_input)
                csv_writer = csv.writer(customer_output)
                for row in csv_reader:
                    if row:
                        if row[0] != ssn:
                            csv_writer.writerow(row)"""

    """with open("./data/customers.csv", "w", newline="") as new_customer_file:
            with open("./data/customers_edit.csv", "r") as new_customer_edit:
                csv_reader = csv.reader(new_customer_edit)
                csv_writer = csv.writer(new_customer_file)
                for row in csv_reader:
                    if row:
                        csv_writer.writerow(row)"""
