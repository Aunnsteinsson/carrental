from repositories.orderrepo import OrderRepo
from models.order import Order
from repositories.carrepo import CarRepo
from models.car import Car
from models.customer import Customer
from datetime import date, timedelta


class OrderService(object):
    def __init__(self):
        self.__order_repo = OrderRepo()
        self.__car_repo = CarRepo()

    def make_order(self, order, order_number):
        """Bætir við pöntun í kerfið"""
        self.__order_repo.add_order(order, order_number)

    def make_order_number(self):
        """Býr til pöntunarnúmer fyrir nýja pöntun"""
        new_order_number = 0
        for order_number in self.__order_repo.get_orders():
            order_num = int(order_number)
            if order_num > new_order_number:
                new_order_number = order_num
        new_order_number += 1
        return new_order_number

    def remove_order(self, order_number):
        """Eyðir út pöntun"""
        self.__order_repo.remove_order(order_number)

    def list_of_days(self, start_date, finish_date):
        """Tekur við upphafsdagsetningu, lokadagsetningu,
        setur það í sitthvorn lista sem síðan breytir því í dagsetningu
        býr síðan til lista á milli beggja dagsetninganna og bætir við
        þeim dögum inn í lista sem sýnir þá daga sem bílar eru uppteknir"""
        list_startdate = start_date.split("/")
        list_finishdate = finish_date.split("/")
        start_year, start_month, start_day = int(list_startdate[2]), int(
            list_startdate[1]), int(list_startdate[0])
        finish_year, finish_month, finish_day = int(list_finishdate[2]), int(
            list_finishdate[1]), int(list_finishdate[0])
        start_date = date(start_year, start_month, start_day)
        finish_date = date(finish_year, finish_month, finish_day)
        step = timedelta(days=1)
        unavailable_list = []
        while start_date <= finish_date:
            unavailable_list.append(start_date)
            start_date += step
        return unavailable_list

    def find_available_cars(self, a_type, start_date, finish_date):
        desired_days = self.list_of_days(start_date, finish_date)
        car_dict = self.__car_repo.get_all_cars()
        unavailable_cars = []
        available_cars_string = ""
        for licence_plate, cars in car_dict.items():
            type_of_car = cars.get_type()
            if type_of_car in a_type:
                not_available = cars.get_status()
                for order_number, date_list in not_available.items():
                    for day in date_list:
                        if day in desired_days:
                            unavailable_cars.append(cars)
                if cars not in unavailable_cars:
                    cars_string = cars.__str__()
                    available_cars_string += cars_string + "\n"
        return available_cars_string

    def add_dates_to_car(self, start_date, finish_date, licence_plate, order_number):
        car_dict = self.__car_repo.get_all_cars()
        car_unavailable = self.list_of_days(start_date, finish_date)
        the_car = car_dict[licence_plate]
        the_car.add_rented_days(car_unavailable, order_number)
        status = the_car.get_status()
        return status

    def get_customer_name(self, customer):
        """Nær í nafn á viðskiptavini"""
        name = customer.get_name()
        return name

    def customer_orders(self, ssn):
        """Skilar streng þar sem allar pantanir viðskiptavins
        koma fram"""
        order = self.__order_repo.get_orders()
        string_of_orders = ""
        for key, orders in order.items():
            if ssn == orders.get_ssn():
                order_string = orders.__str__()
                string_of_orders += order_string + "\n"
        return string_of_orders

    def change_time(self, order_number, new_time):
        """Breytir tíma á pöntun"""
        order = self.__order_repo.get_orders(order_number)
        order.change_time(new_time)

    def change_insurance(self, order_number, new_insurance):
        """Breytir stöðu á tryggingu"""
        order = self.__order_repo.get_orders(order_number)
        order.change_insurance(new_insurance)

    def show_orders(self):
        """Sýnir allar pantanir og skilar þeim sem streng"""
        order_dict = self.__order_repo.get_orders()
        string_of_orders = ""
        for order, value in order_dict.items():
            order_string = value.__str__()
            string_of_orders += order_string + "\n"
        return string_of_orders

    def price_of_rent(self, order):
        """Reiknar út verð á pöntun"""
        licence_plate = order.get_licence_plate()
        the_car = self.__car_repo.get_car(licence_plate)
        price_of_car = the_car.price_vehicle()
        insurance = order.get_insurance()
        price_of_insurance = self.__car_repo.get_car_prices()
        price_of_insurance = price_of_insurance["trygging"]
        start = order.get_start()
        end = order.get_end()
        days_of_rent = date(end).day - date(start).day
        days_of_rent = int(days_of_rent)
        price_of_rent = days_of_rent * price_of_car
        if insurance:
            final_price = price_of_insurance * days_of_rent + price_of_car
            return final_price
        else:
            return price_of_rent

    def find_order(self, order_number):
        order_dict = self.__order_repo.get_orders()
        for order, value in order_dict.items():
            if order == order_number:
                return order_dict[order_number]
