import csv


class Order(object):
    '''Klasi fyrir pantanir. Breytur í þessum klasa eru pöntunarnúmer,
    upphafsdagur,skiladagur, nafn viðskiptavinar, kennitala viðskiptavinar,
    bíltegund, bílnúmer, staða bíls og hvort pöntun innihaldi aukatryggingu
    eður ei. Klasinn inniheldur föll til að hægt sé að kalla á breytur eða
    breyta þeim. Hægt er að fá __str__ á tvo mismunandi vegu.'''

    def __init__(self, order_number, list_of_dates, ssn, name, car_number,
                 price, insurance=False, discount=0.000):
        self.__order_number = order_number
        self.__list_of_dates = self.dates_string_to_list(list_of_dates)
        self.__ssn = ssn
        self.__name = name
        self.__car_number = car_number
        self.__insurance = insurance
        self.__discount = discount
        self.__price = price

    # Föll hér að neðan er hægt að kalla í til að nálgast breyturnar

    def __str__(self, info_to_print=0):
        '''Annars vegar skilar upplýsingum prentuðum með án kennitölu.
        Það er nýtt þegar pöntun er sköðuð út frá Kennitölu.
        Hins vegar skilar upplýsingum með kommu á milli, notað til skráningar
        í geymslu.'''
        start_date = self.__list_of_dates[0]
        end_date = self.__list_of_dates[-1]

        if info_to_print == 1:
            return "\t{:11}| {:9}| {:11}| {:7} | ".format(
                start_date,
                self.__order_number,
                self.__ssn,
                self.__car_number)

        elif info_to_print == 2:  # Hvernig pantanir prentast í sögu viðsk.v.
            return "\t{:13}| {:9}| {:7}| {:10,.0f} ISK".format(
                start_date,
                self.__order_number,
                self.__car_number,
                float(self.__price))

        else:
            # Skilar öllum upplýsingum um pöntun.
            if self.__insurance == "True":
                insurance = "Já"   
            else:
                insurance = "Nei"
            return "{:11}| {:11}| {:9}| {:30}| {:11}| {:7}| {:12,.0f} ISK| {:>9}| {:5.0f}%".format(
                start_date,
                end_date,
                self.__order_number,
                self.__name,
                self.__ssn,
                self.__car_number,
                float(self.__price),
                insurance,
                float(self.__discount))

    def __repr__(self):
        '''
        Skrifar upplýsingar um pöntun
        '''
        string_of_dates = self.dates_list_to_string()
        return "{},{},{},{},{},{},{},{}".format(self.__order_number,
                                                string_of_dates,
                                                self.__ssn,
                                                self.__name,
                                                self.__car_number,
                                                float(self.__price),
                                                self.__insurance,
                                                self.__discount)

    def dates_list_to_string(self):
        """Tekur listann af dögum og breytir honum í 
        streng svo hægt sé að skrifa hann í csv skrána"""
        list_of_dates = self.__list_of_dates
        string_of_dates = ""
        for date in list_of_dates:
            # Sett inn til að hægt sé að splitt strengnum í dagsetningar þegar lesið er úr skránni
            string_of_dates += str(date) + ":"
        return string_of_dates

    def dates_string_to_list(self, dates_string):
        """Tekur streng úr csv skránni og býr til lista úr honum"""
        if type(dates_string) == list:  # Stundum í kerfinu er inputið nú þegar listi en sá listi getur verið
            # fullur af datetime eða dagsetningum sem eru strengur.
            # Þá breytum við listanum í streng þannig að formattið sé alltaf það sama
            self.__list_of_dates = dates_string
            dates_string = self.dates_list_to_string()
        try:
            str(dates_string)  # ER ÞETTA TRY AND EXCEPT ENNÞÁ NAUÐSUNLEGT???
            date_list = dates_string.strip(":").split(':')
            return date_list
        except Exception:
            return dates_string

    # Hér koma nokkur föll sem að sækja breytur í klasann

    def get_order_number(self):
        """SKilar pöntunarnúmeri pöntunar"""
        return self.__order_number

    def get_discount(self):
        """Skilar afslætti pöntunar"""
        return self.__discount

    def get_licence_plate(self):  # Endurtekinn kóði
        """Skilar bílnúmeri þess bíls sem er skráður á pöntunina"""
        return self.__car_number

    def get_price(self):
        """Skilar verði pöntunar"""
        return self.__price

    def get_duration(self):
        """Sækir lista af þeim dögum sem pöntunin er"""
        return self.__list_of_dates

    def get_insurance(self):
        """Sækir upplýsingar um hvort pöntun er með aukatryggingu eða ekki"""
        return self.__insurance

    def get_car(self):
        """Sækir bílnúmer þess bíls sem er skráður á pöntunina"""  # Endurtekinn kóði
        return self.__car_number

    def get_ssn(self):
        """Sækir kennitölu þess sem viðskiptavinar sem er skráður á pöntunina"""
        return self.__ssn

    # Föll hér að neðan er hægt að nýta til að breyta gildi breytanna

    def change_duration(self, new_list):  # Endurtekinn kóði
        """Tekur inn lista af dögum og skráir pöntunina á þá daga"""
        self.__list_of_dates = [str(day) for day in new_list]

    def change_price(self, new_price):
        """Tekur inn verð og breytir verði pöntunar í það verð"""
        self.__price = new_price

    def change_list_of_days(self, new_list):  # Endurtekinn kóði
        """Tekur inn lista af dögum og skráir pöntunina á þá daga"""
        self.__list_of_dates = new_list

    def change_insurance(self, new_insurance):
        """Tekur inn upplýsingar um hvort það sé aukatrygging og breytir pöntun eftir því"""
        self.__insurance = new_insurance

    def change_name(self, new_name):
        """Tekur inn nýtt nafn viðskiptavinar og breytir því í pöntuninni"""
        self.__name = new_name

    def change_car(self, new_car):
        """Tekur inn nýtt bílnúmer og breytir bílnúmeri pöntunar í það"""
        self.__car_number = new_car

    def change_ssn(self, new_ssn):
        """Tekur inn kennitölu og breytir kennitölu pöntunar í þá kennitölu"""
        self.__ssn = new_ssn

    def change_discount(self, new_discount):
        """Tekur inn afslátt og breytir afslætti pöntunar í þann afslátt"""
        self.__discount = new_discount
