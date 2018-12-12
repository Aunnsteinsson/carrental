# DENNI


class Car(object):
    """Þessi klasi býr til bíl, með númeraplötu og hvernig týpa
    af bíl hann er"""

    def __init__(self, licence_plate, a_type, price_dict, rented_days="None"):
        self.__licence_plate = licence_plate
        self.__a_type = a_type
        self.__price = price_dict
        self.__rented_days = self.string_to_dict(rented_days)
        self.__price_of_car = self.price_vehicle()

    def __str__(self):
        if self.__rented_days:
            for order_number, date_list in self.__rented_days.items():
                date = str(date_list[0])
                
        else:
            date = "Engar pantanir"
        return "{:<8} | {:<12} | {:>11,.2f} {} | {:<10} | {:<20}".format(self.__licence_plate, self.print_a_type(self.__a_type), self.__price_of_car, ("kr."), ("Í stæði"), date)

    def dict_to_string(self, date_dict):
        string = ""
        for key, value in date_dict.items():
            string += ":" + str(key) + "&"
            for day in value:
                string += str(day) + "$"
        return string

    def print_a_type(self, a_type):
        if a_type == "folksbill":
            return "Fólksbíll"
        elif a_type == "jeppi":
            return "Jeppi"
        elif a_type == "sendibill":
            return "Sendibíll"
        elif a_type == "trygging":
            return "Aukatrygging"

    def string_to_dict(self, order_string):
        dictionary = {}
        if order_string == "None":
            return dictionary
        string = order_string.split(":")
        for value in string:
            if value != "":
                new_list = value.split("&")
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

    # def price_small_car(self, a_type):
      #  """Ef flokkur bíls er fólksbíll, þá er verðið á honum 5000"""
       # self.__price = 5000
        # return self.__price

#    def price_van(self, a_type):
 #       """Ef flokkur bíls er sendibíll, þá er verðið á honum 15.000"""
  #      if a_type.lower() == "sendibíll":
   #         self.__price = 15000
    #    return self.__price"""

    def get_type(self):
        """Skilar flokki bíls"""
        return self.__a_type

    def get_duration(self):
        """Skilar stöðu bíls"""
        return self.__rented_days

    def remove_order(self, order_number):
        k = self.__rented_days.pop(order_number)

    def add_rented_days(self, list_of_days, order_number):
        list_of_days = [str(day) for day in list_of_days]
        self.__rented_days[order_number] = list_of_days

    def __repr__(self):
        days_string = self.dict_to_string(self.__rented_days)
        return "{},{},{}".format(self.__licence_plate,
                                 self.__a_type, days_string)


"""class Jeep(Car):
    def __init__(self, price, licence_plate, a_type):
        Car.__init__(self, licence_plate, a_type)
        self.__price = price

    def get_price(self):
        return self.__price


class SmallCar(Car):
    def __init__(self, price, licence_plate, a_type):
        Car.__init__(self, licence_plate, a_type)
        self.__price = price

    def get_price(self):
        return self.__price


class Van(Car):
    def __init__(self, price, licence_plate, a_type):
        Car.__init__(self, licence_plate, a_type)
        self.__price = price

    def get_price(self):
        return self.__price"""
