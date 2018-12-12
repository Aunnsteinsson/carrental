# DENNI


class Car(object):
    """Þessi klasi býr til bíl, með númeraplötu og hvernig týpa
    af bíl hann er"""

    def __init__(self, licence_plate, a_type, price_dict, rented_days=[]):
        self.__licence_plate = licence_plate
        self.__a_type = a_type
        self.__price = price_dict
        rented_days = rented_days.strip("[]")
        rented_days = rented_days.split(",")
        self.__rented_days = []
        self.__price_of_car = self.price_vehicle()

    def __str__(self):
        return "{:<20} | {:<20} | {:<20} | {:<20}".format(self.__a_type, self.__licence_plate, self.__price_of_car, str(self.__rented_days))

    def get_licence_plate(self):
        """Skilar númeraplötu"""
        return self.__licence_plate

    def price_vehicle(self):
        """Ef flokkur bíls er jeppi, þá er verðið á honum 10.000"""
        vehicle_price = self.__price[self.__a_type]
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

    def get_status(self):
        """Skilar stöðu bíls"""
        return self.__rented_days

    def remove_order(self, list_of_days):
        for list_of_rented_days in self.__rented_days:
            for day in list_of_rented_days:
                for order_day in list_of_days:
                    if order_day == day:
                        list_of_rented_days.pop(day)

    def add_rented_days(self, list_of_days):
        self.__rented_days.append(list_of_days)

    def __repr__(self):
        return "{},{},{}".format(self.__licence_plate,
                                 self.__a_type, self.__rented_days)


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
