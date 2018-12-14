# DENNI
from datetime import date
from datetime import datetime
from datetime import timedelta


class Car(object):
    """Þessi klasi býr til bíl, með númeraplötu og hvernig týpa
    af bíl hann er"""

    def __init__(self, licence_plate, a_type, price_dict, status="j",
                 rented_days="None"):
        self.__licence_plate = licence_plate
        self.__a_type = a_type
        self.__price = price_dict
        self.__rented_days = self.string_to_dict(rented_days)
        self.__price_of_car = self.price_vehicle()
        self.__status = status
        self.__wherabouts = self.see_if_returned()

    def __str__(self):
        the_date = self.get_the_next_order()
        return "{:<8} | {:<12} | {:<11,.0f} {:<} | {:<30} | {:<20}".format(
            self.__licence_plate,
            self.__a_type,
            self.__price_of_car,
            ("ISK"),
            (self.__wherabouts),
            the_date)

    def __repr__(self):
        days_string = self.dict_to_string(self.__rented_days)
        return "{},{},{},{}".format(self.__licence_plate,
                                    self.__a_type,
                                    self.__status,
                                    days_string)

    def string_to_dict(self, order_string):
        """Fall sem les úr dagsetningar csv skránni og setur upplýsingarnar
         í dictionary"""
        dictionary = {}
        # Ef að það voru engir dagar skráðir á bílinn þá skilar þetta tómu dict
        if order_string == "None":
            return dictionary
        # splittum á : til að skilja að einstakar pantanir
        string = order_string.split(":")
        for value in string:
            # Til að forðast villur þar sem við splittum tómum streng
            if value != "":
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

    def dict_to_string(self, date_dict):
        """Fall sem að breytid dagsetningadict í streng til að hægt sé að
         setja í csv skrá"""
        string = ""
        for key, value in date_dict.items():
            # Hér bætum við inn breytum sem eru aldrei annars í strengnum
            # til að splitta á þegar lesið er úr skránni
            string += ":" + str(key) + "&"
            for day in value:
                string += str(day) + "$"
        return string

    def see_if_returned(self):
        """Fall sem sér hvort að bíll eigi að vera í útleigu eða ekki í dag
         og hvort hann sé í stæði eða ekki"""
        if self.__rented_days:
            for order_number, list_of_days in self.__rented_days.items():
                # athugar hvort að dagurinn í dag sé einn af þeim dögum
                #  sem að bíllinn er leigður
                if str(date.today()) in list_of_days:
                    # "j" stendur fyrir í stæði og "n" fyrir að hann sé
                    #  ekki í stæði
                    if self.__status == "j":
                        return "Leigður en ekki sóttur"
                    if self.__status == "n":
                        return "Í útleigu"
        if self.__status == "j":
            return "Tilbúinn til útleigu"
        if self.__status == "n":
            return "Hefur ekki enn verið skilað"

    def get_the_next_order(self):
        """Fall sem að gefur þér dagsetningu næsta dags sem
         bíllinn er frátekinn"""
        if self.__rented_days:
            # Býr til gærdaginn til að bera saman við
            yesterday = datetime.now() - timedelta(days=1)
            # dagur sem er svo langt í burtu að enginn(með viti)
            #  mun leigja hann
            highest_date = datetime(4500, 12, 30)
            for order_number, date_list in self.__rented_days.items():
                for a_date in date_list:
                    date_list = a_date.split("-")
                    day = datetime(int(date_list[0]), int(
                        date_list[1]), int(date_list[2]))
                    # ef dagurinn er ekki í fortíð og ekki það sem nú er
                    #  skráð sem highest day
                    if day > yesterday and day < highest_date:
                        # þá er dagurinn skráður sem highest day því við
                        #  viljum lægstu dagsetningu sem er ekki í dag
                        highest_date = day
            # Ef einhver dagur var í framtíðinni
            if highest_date != datetime(4500, 12, 30):
                # þá skilar fallið þeim degi
                the_date = str(highest_date.date())
            else:
                the_date = "Engar pantanir"  # annars engar pantanir
        else:
            # Ef engin pöntun var skráð á bíl þá skilar fallið setningu um það
            the_date = "Engar pantanir"
        return(the_date)

    # Hér koma nokkur föll sem að sækja breytur í klasann
    def get_status(self):
        """sendir streng sem er "j" ef bíll er í stæði en annars "n" """
        return self.__status

    def get_wherabouts(self):
        """Fall sem að sendir streng með því ástandi sem bíll er í """
        return self.__wherabouts

    def get_licence_plate(self):
        """Skilar númeraplötu"""
        return self.__licence_plate

    def price_vehicle(self):
        """Finnur verð bílategundar í verðflokki og skilar verði bíls"""
        vehicle_price = self.__price[self.__a_type]
        vehicle_price = float(vehicle_price)
        return vehicle_price

    def get_type(self):
        """Skilar flokki bíls"""
        return self.__a_type

    def get_duration(self):
        """Skilar dictionary af öllum þeim pöntunum og dögum sem
         bíll er frátekinn"""
        return self.__rented_days

    # Hér eru nokkur föll sem breyta breytum í klasanum
    def change_status(self, new_status):
        """Fall sem breytir því hvort bill sé í stæði eða ekki"""
        self.__status = new_status
        # ástand bíls breytist með stæðinu og því þarf að kalla á þetta
        self.__wherabouts = self.see_if_returned()

    def remove_order(self, order_number):
        """Eyðir pöntun af bíl"""
        self.__rented_days.pop(order_number, None)

    def add_rented_days(self, list_of_days, order_number):
        """Bætir pöntun á bíl, þar eða setur inn lista af dögum sem
         hann er frátekinn"""
        list_of_days = [str(day) for day in list_of_days]
        self.__rented_days[order_number] = list_of_days
