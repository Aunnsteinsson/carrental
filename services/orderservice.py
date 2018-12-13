from repositories.orderrepo import OrderRepo
from repositories.customerrepo import CustomerRepo
from models.order import Order
from repositories.carrepo import CarRepo
from models.car import Car
from models.customer import Customer
from datetime import date, timedelta

STARTDATE = 0
ENDDATE = -1


class OrderService(object):
    def __init__(self):
        self.__order_repo = OrderRepo()
        self.__car_repo = CarRepo()
        self.__customer_repo = CustomerRepo()

    def make_order(self, order_number, order):
        """Bætir við pöntun í kerfið"""
        self.__order_repo.add_order(order_number, order)
        self.__order_repo.save_new_orders()

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
        self.remove_order_from_car(order_number)
        self.__order_repo.remove_order(order_number)
        self.__order_repo.save_new_orders()
        self.__car_repo.save_car_data()

    def remove_order_from_car(self, order_number):
        the_order = self.__order_repo.get_order(order_number)
        licence_plate = the_order.get_licence_plate()
        car = self.__car_repo.get_car(licence_plate)
        car.remove_order(order_number)

    def list_of_days(self, start_date, finish_date):
        """Tekur við upphafsdagsetningu, lokadagsetningu,
        setur það í sitthvorn lista sem síðan breytir því í dagsetningu
        býr síðan til lista á milli beggja dagsetninganna og bætir við
        þeim dögum inn í lista sem sýnir þá daga sem bílar eru uppteknir"""
        list_startdate = start_date.split("-")
        list_finishdate = finish_date.split("-")
        start_year, start_month, start_day = int(list_startdate[2]), int(
            list_startdate[1]), int(list_startdate[0])
        finish_year, finish_month, finish_day = int(list_finishdate[2]), int(
            list_finishdate[1]), int(list_finishdate[0])
        start_date = date(start_day, start_month, start_year)
        finish_date = date(finish_day, finish_month, finish_year)
        step = timedelta(days=1)
        unavailable_list = []
        while start_date <= finish_date:
            unavailable_list.append(start_date)
            start_date += step
        return unavailable_list

    def find_unavailable_cars(self, a_type, start_date, finish_date):
        desired_days = self.list_of_days(start_date, finish_date)
        desired_days = [str(day) for day in desired_days]
        car_dict = self.__car_repo.get_all_cars()
        unavailable_cars = []
        for licence_plate, cars in car_dict.items():
            type_of_car = cars.get_type()
            if type_of_car in a_type:
                not_available = cars.get_duration()
                for order_number, date_list in not_available.items():
                    for day in date_list:
                        if day in desired_days:
                            unavailable_cars.append(cars)
            else:
                unavailable_cars.append(cars)
        return unavailable_cars

    def find_available_cars(self, a_type, start_date, finish_date):
        unavailable_cars = self.find_unavailable_cars(
            a_type, start_date, finish_date)
        available_cars_string = ""
        car_dict = self.__car_repo.get_all_cars()
        for licence_plate, cars in car_dict.items():
            if cars not in unavailable_cars:
                cars_string = cars.__str__()
                available_cars_string += cars_string + "\n"
        return available_cars_string

    def add_dates_to_car(self, start_date, finish_date,
                         licence_plate, order_number):
        car_dict = self.__car_repo.get_all_cars()
        car_unavailable = self.list_of_days(start_date, finish_date)
        the_car = car_dict[licence_plate]
        the_car.add_rented_days(car_unavailable, order_number)
        self.__car_repo.save_car_data()

    def get_customer_name(self, customer):
        """Nær í nafn á viðskiptavini"""
        name = customer.get_name()
        return name

    def customer_orders(self, ssn, print_format):
        """Skilar streng þar sem allar pantanir viðskiptavins
        koma fram"""
        order = self.__order_repo.get_orders()
        string_of_orders = ""
        for _, orders in order.items():
            if ssn == orders.get_ssn():
                licence_plate = orders.get_car()
                the_car = self.__car_repo.get_car(licence_plate)
                status = the_car.get_wherabouts()
                order_string = orders.__str__(print_format)
                string_of_orders += order_string + status + "\n"
        return string_of_orders

    def change_time(self, order_number, new_start_time, new_end_time):
        """Breytir tíma á pöntun"""
        order = self.__order_repo.get_order(order_number)
        licence_plate = order.get_licence_plate()
        the_car = self.__car_repo.get_car(licence_plate)
        a_type = the_car.get_type()
        self.remove_order_from_car(order_number)
        unavailable_cars = self.find_unavailable_cars(
            a_type, new_start_time, new_end_time)
        if the_car not in unavailable_cars:
            self.add_dates_to_car(
                new_start_time, new_end_time, licence_plate, order_number)
            new_list = self.list_of_days(new_start_time, new_end_time)
            order.change_duration(new_list)
            self.__order_repo.save_new_orders()
            return "Breyting tókst!"
        else:
            available_cars = self.find_available_cars(
                a_type, new_start_time, new_end_time)
            return "Bíll ekki í boði. Vinsamlegast veldu einhvern af þessum bílum. \n {}".format(available_cars)

    def change_car(self, a_type, order_number):
        order = self.__order_repo.get_order(order_number)
        list_of_days = order.get_duration()
        start = list_of_days[STARTDATE]
        start = start.split("-")
        start = start[0] + "-" + start[1] + "-" + start[2]
        end = list_of_days[ENDDATE]
        end = end.split("-")
        end = end[0] + "-" + end[1] + "-" + end[2]
        self.remove_order_from_car(order_number)
        string_car = self.find_available_cars(a_type, start, end)
        return string_car

    def change_car_again(self, new_car, order_number):
        order = self.__order_repo.get_order(order_number)
        order.change_car(new_car)
        self.__order_repo.save_new_orders()
        self.__car_repo.save_car_data()

    def change_customer(self, order_number, new_ssn):
        """Breytir hver viðskiptavinur er á pöntun"""
        order = self.__order_repo.get_order(order_number)
        order.change_ssn(new_ssn)
        customer = self.__customer_repo.get_customer(new_ssn)
        name = customer.get_name()
        order.change_name(name)
        self.__order_repo.save_new_orders()

    def change_insurance(self, order_number, new_insurance):
        """Breytir stöðu á tryggingu"""
        order = self.__order_repo.get_order(order_number)
        order.change_insurance(new_insurance)
        discount = order.get_discount()
        duration_list = order.get_duration()
        licence_plate = order.get_car()
        start = duration_list[STARTDATE]
        end = duration_list[ENDDATE]
        price = self.price_of_rent(
            licence_plate, discount, new_insurance, start, end)
        self.change_price(order, price)
        self.__order_repo.save_new_orders()

    def show_orders(self):
        """Sýnir allar pantanir og skilar þeim sem streng"""
        order_dict = self.__order_repo.get_orders()
        string_of_orders = ""
        for order, value in order_dict.items():
            order_string = value.__str__()
            string_of_orders += order_string + "\n"
        return string_of_orders

    def get_orders(self):
        return self.__order_repo.get_orders()

    def get_price_of_extra_insurance(self):
        price_of_insurance = self.__car_repo.get_car_prices()
        price_of_insurance = price_of_insurance["aukatrygging"]
        return float(price_of_insurance)

    def get_price_of_mandated_insurance(self):
        price_of_insurance = self.__car_repo.get_car_prices()
        price_of_insurance = price_of_insurance["skyldutrygging"]
        return float(price_of_insurance)

    def price_of_rent(self, licence_plate, discount, insurance, start_date, end_date):
        """Reiknar út verð á pöntun"""
        the_car = self.__car_repo.get_car(licence_plate)
        price_of_car = the_car.price_vehicle()
        price_of_car = float(price_of_car)
        price_of_extra_insurance = self.get_price_of_extra_insurance()
        price_of_mandated_insurance = self.get_price_of_mandated_insurance()
        list_of_days = self.list_of_days(start_date, end_date)
        start = list_of_days[STARTDATE]
        end = list_of_days[ENDDATE]
        days_of_rent = end.day - start.day
        days_of_rent = int(days_of_rent)
        price_of_rent = days_of_rent * price_of_car
        price_of_mandated = days_of_rent * price_of_mandated_insurance
        price_of_rent += price_of_mandated
        discount = self.change_discount_to_float(discount)
        if insurance:
            final_price = price_of_extra_insurance * days_of_rent + price_of_rent
            if discount:
                final_price = final_price * discount
            return final_price
        if discount:
            price_of_rent = price_of_rent * discount
            return price_of_rent
        else:
            return price_of_rent

    def change_price(self, order, new_price):
        order.change_price(new_price)

    def change_discount(self, order_number, new_discount):
        order = self.__order_repo.get_order(order_number)
        order.change_discount(new_discount)
        insurance = order.get_insurance()
        duration_list = order.get_duration()
        licence_plate = order.get_car()
        start = duration_list[STARTDATE]
        end = duration_list[ENDDATE]
        price = self.price_of_rent(
            licence_plate, new_discount, insurance, start, end)
        self.change_price(order, price)
        self.__order_repo.save_new_orders()

    def change_discount_to_float(self, discount):
        discount = float(discount)/100
        return 1-discount

    def find_order(self, order_number):
        order_dict = self.__order_repo.get_orders()
        for order, _ in order_dict.items():
            if order == order_number:
                return order_dict[order_number]
        return False
