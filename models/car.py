# DENNI
from datetime import date


class Car(object):
    """Þessi klasi býr til bíl, með númeraplötu og hvernig týpa
    af bíl hann er"""

    def __init__(self, licence_plate, a_type, price_dict, status="j", rented_days="None"):
        self.__licence_plate = licence_plate
        self.__a_type = a_type
        self.__price = price_dict
        self.__rented_days = self.string_to_dict(rented_days)
        self.__price_of_car = self.price_vehicle()
        self.__status = status
        self.__wherabouts = self.see_if_returned()

    def __str__(self):
        if self.__rented_days:
            for order_number, date_list in self.__rented_days.items():
                date = str(date_list[0])
        else:
            date = "Engar pantanir"
        return "{:<8} | {:<12} | {:<11,.0f} {:<} | {:<30} | {:<20}".format(self.__licence_plate, self.print_a_type(self.__a_type), self.__price_of_car, ("ISK"), (self.__wherabouts), date)

    def see_if_returned(self):
        """Fall sem sér hvort að bíll eigi að vera í útleigu eða ekki í dag og hvort hann sé í stæði eða ekki"""
        if self.__rented_days:
            for order_number, list_of_days in self.__rented_days.items():
                # athugar hvort að dagurinn í dag sé einn af þeim dögum sem að bíllinn er leigður
                if str(date.today()) in list_of_days:
                    if self.__status == "j":  # "j" stendur fyrir í stæði og "n" fyrir að hann sé ekki í stæði
                        return "Leigður en ekki sóttur"
                    if self.__status == "n":
                        return "Í útleigu"
        if self.__status == "j":
            return "Tilbúinn til útleigu"
        if self.__status == "n":
            return "Hefur ekki enn verið skilað"

    def get_status(self):
        """sendir streng sem er "j" ef bíll er í stæði en annars "n" """
        return self.__status

    def get_wherabouts(self):
        """Fall sem að sendir streng með því ástandi sem bíll er í """
        return self.__wherabouts

    def change_status(self, new_status):
        """Fall sem breytir því hvort bill sé í stæði eða ekki"""
        self.__status = new_status
        # ástand bíls breytist með stæðinu og því þarf að kalla á þetta
        self.__wherabouts = self.see_if_returned()

    def dict_to_string(self, date_dict):
        """Fall sem að breytid dagsetningadict í streng til að hægt sé að setja í csv skrá"""
        string = ""
        for key, value in date_dict.items():
            # Hér bætum við inn breytum sem eru aldrei annars í strengnum til að splitta á þegar lesið er úr skránni
            string += ":" + str(key) + "&"
            for day in value:
                string += str(day) + "$"  # sama hér
        return string

    def print_a_type(self, a_type):  # Er þetta fall nauðsynlegt????
        if a_type == "folksbill":
            return "Fólksbíll"
        elif a_type == "jeppi":
            return "Jeppi"
        elif a_type == "sendibill":
            return "Sendibíll"
        elif a_type == "trygging":
            return "Aukatrygging"

    def string_to_dict(self, order_string):
        """Fall sem les úr dagsetningar csv skránni og setur upplýsingarnar í dictionary"""
        dictionary = {}
        if order_string == "None":  # Ef að það voru engir dagar skráðir á bílinn þá skilar þetta tómu dict
            return dictionary
        # splittum á : til að skilja að einstakar pantanir
        string = order_string.split(":")
        for value in string:
            if value != "":  # TIl að forðast villur þar sem við splittum tómum streng
                # Skiljum að pöntunarnúmer og dagsetningar
                new_list = value.split("&")
                # Skiljum að dagsetningar í pöntun
                the_list = new_list[1].split("$")
                last_list = []
                for day in the_list:
                    if day != "":
                        last_list.append(day)
                dictionary[new_list[0]] = last_list
        return dictionary

    def get_licence_plate(self):
        """Skilar númeraplötu"""
        return self.__licence_plate

    def price_vehicle(self):
        """Ef flokkur bíls er jeppi, þá er verðið á honum 10.000"""
        vehicle_price = self.__price[self.__a_type]
        vehicle_price = float(vehicle_price)
        return vehicle_price

    def get_type(self):
        """Skilar flokki bíls"""
        return self.__a_type

    def get_duration(self):
        """Skilar stöðu bíls"""
        return self.__rented_days

    def remove_order(self, order_number):
        """Eyðir pöntun af bíl"""
        self.__rented_days.pop(order_number, None)

    def add_rented_days(self, list_of_days, order_number):
        """Bætir pöntun á bíl"""
        list_of_days = [str(day) for day in list_of_days]
        self.__rented_days[order_number] = list_of_days

    def __repr__(self):
        days_string = self.dict_to_string(self.__rented_days)
        return "{},{},{},{}".format(self.__licence_plate,
                                    self.__a_type, self.__status, days_string)
