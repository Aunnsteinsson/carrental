from repositories.orderrepo import OrderRepo
from repositories.customerrepo import CustomerRepo
from models.order import Order
from repositories.carrepo import CarRepo
from models.car import Car
from models.customer import Customer
from datetime import date, timedelta

STARTDATE = 0
ENDDATE = -1
VSK = 1.24


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
            if order_num > new_order_number:  # Finnur hæsta pöntunarnúmer sem var
                new_order_number = order_num  # í kerfinu fyrir
        new_order_number += 1  # Bætir einum við
        return new_order_number

    def remove_order(self, order_number):
        """Eyðir út pöntun"""
        self.remove_order_from_car(order_number)
        self.__order_repo.remove_order(order_number)
        self.__order_repo.save_new_orders()
        self.__car_repo.save_car_data()

    def remove_order_from_car(self, order_number):
        """Eyðir pöntun sem er skráð á bíl af þeim bíl"""
        the_order = self.__order_repo.get_order(order_number)
        licence_plate = the_order.get_licence_plate()
        car = self.__car_repo.get_car(licence_plate)
        car.remove_order(order_number)

    def list_of_days(self, start_date, finish_date):
        """Tekur inn upphafs og lokadagsetningu og skilar inn
        lista af dögum (datetime) sem eru á því bili"""
        list_startdate = start_date.split("-")
        list_finishdate = finish_date.split("-")
        start_year, start_month, start_day = int(list_startdate[2]), int(
            list_startdate[1]), int(list_startdate[0])
        finish_year, finish_month, finish_day = int(list_finishdate[2]), int(
            list_finishdate[1]), int(list_finishdate[0])
        start_date = date(start_day, start_month, start_year)
        finish_date = date(finish_day, finish_month, finish_year)
        step = timedelta(days=1)
        list_of_days = []
        while start_date <= finish_date:
            list_of_days.append(start_date)
            start_date += step
        return list_of_days

    def find_unavailable_cars(self, a_type, start_date, finish_date):
        """Fall sem tekur inn upphafs og lokadag leigu og lista yfir þær gerðir
        bíla sem eru í boði og skilar lista með þeim bílum sem uppfylla ekki 
        skilyrðin að vera af réttum flokki og í boði á þessu tímabili"""
        desired_days = self.list_of_days(start_date, finish_date)
        # Breytum dögum úr datetime í streng því þannig eru þau geymd í klösunum
        desired_days = [str(day) for day in desired_days]
        car_dict = self.__car_repo.get_all_cars()
        unavailable_cars = []
        for _, cars in car_dict.items():
            type_of_car = cars.get_type()
            if type_of_car in a_type:  # a_type er listi með þeim flokkum sem notandi vill
                unavailable_days = cars.get_duration()
                for _, date_list in unavailable_days.items():
                    for day in date_list:
                        if day in desired_days:
                            unavailable_cars.append(cars)
            else:
                unavailable_cars.append(cars)
        return unavailable_cars

    def find_available_cars(self, a_type, start_date, finish_date):
        """Fall sem að tekur inn lista af þeim flokkum af bílum sem eru í boði
        og upphafs og lokadagsetningu og skilar streng með þeim bílum sem 
        uppfylla það skilyrði að vera af réttri gerð og í boði á tímabilinu"""
        unavailable_cars = self.find_unavailable_cars(
            a_type, start_date, finish_date)
        available_cars_string = ""
        car_dict = self.__car_repo.get_all_cars()
        for _, cars in car_dict.items():
            if cars not in unavailable_cars:
                cars_string = cars.__str__()
                available_cars_string += cars_string + "\n"
        return available_cars_string

    def add_dates_to_car(self, start_date, finish_date,
                         licence_plate, order_number):
        """Tekur inn dagsetningar, pöntunarnúmer og bílnúmer og bætir 
        pöntuninni á bíl"""
        car_dict = self.__car_repo.get_all_cars()
        car_unavailable = self.list_of_days(start_date, finish_date)
        the_car = car_dict[licence_plate]
        the_car.add_rented_days(car_unavailable, order_number)
        self.__car_repo.save_car_data()

    def get_customer_name(self, customer):
        """Tekur inn stak af viðskiptavini og nær í nafn á viðskiptavini"""
        name = customer.get_name()
        return name

    def get_orders_of_customer_menu(self, ssn):
        """Finnur allar pantanir sem eru skráðar á viðskiptavin
        og skilar þeim sem lista"""
        order = self.__order_repo.get_orders()
        list_of_order_numbers = []
        for ordernumber, orders in order.items():
            if ssn == orders.get_ssn():
                list_of_order_numbers.append(ordernumber)
        return list_of_order_numbers

    def customer_orders(self, ssn, print_format):
        """Skilar streng þar sem allar pantanir viðskiptavins
        koma fram"""
        order_list = self.get_orders_of_customer_menu(ssn)
        string_of_orders = ""
        for order_number in order_list:
            order = self.__order_repo.get_order(order_number)
            order_string = order.__str__(print_format)
            string_of_orders += order_string + "\n"
        return string_of_orders

    def change_time(self, order_number, new_start_time, new_end_time):
        """Tekur inn pöntunarnúmer og nýjan upphafs og lokatíma og breytir
        tímunum á pöntuninni"""
        order = self.__order_repo.get_order(order_number)
        licence_plate = order.get_licence_plate()
        the_car = self.__car_repo.get_car(licence_plate)
        a_type = the_car.get_type()
        self.remove_order_from_car(order_number)
        unavailable_cars = self.find_unavailable_cars(
            a_type, new_start_time, new_end_time)
        if the_car not in unavailable_cars:  # Ef bíllin er laus þá fær hann nýjar dagsetningar
            self.add_dates_to_car(
                new_start_time, new_end_time, licence_plate, order_number)
            new_list = self.list_of_days(new_start_time, new_end_time)
            order.change_duration(new_list)
            self.__order_repo.save_new_orders()
            return "Breyting tókst!"
        else:  # Ef bíllinn er ekki laus er fundinn bíll af réttum flokki sem er laus og notandi beðinn um að velja einn af þeim
            available_cars = self.find_available_cars(
                a_type, new_start_time, new_end_time)
            return "Bíll ekki í boði. Vinsamlegast veldu einhvern af þessum bílum. \n {}".format(available_cars)

    def change_car(self, a_type, order_number):
        """Tekur inn gerð bíls og pöntunarnúmer og skilar
        streng með öllum þeim bílum sem eru í boði"""
        order = self.__order_repo.get_order(order_number)
        list_of_days = order.get_duration()
        start = list_of_days[STARTDATE]
        start = start.split("-")
        start = start[0] + "-" + start[1] + "-" + start[2]
        end = list_of_days[ENDDATE]
        end = end.split("-")
        end = end[0] + "-" + end[1] + "-" + end[2]
        price_dict = self.__car_repo.get_car_prices()
        type_list = []  # Við gerum lista með öllum gerðum bíla öðrum en þeim sem
        for car_type in price_dict:  # var áður í pöntuninni
            if car_type != a_type:
                type_list.append(car_type)
        self.remove_order_from_car(order_number)
        string_car = self.find_available_cars(type_list, start, end)
        return string_car

    def change_car_again(self, new_car, order_number):
        """Tekur inn stak af bíl og setur það inn í dict
        og skrifar það líka í csv skrána"""
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
        licence_plate = order.get_licence_plate()
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

    def get_total_rev(self, list_of_dates):
        """Tekur inn lista af dögum og skilar inn heildatekjum af öllum
        pöntunum án VSK á því tímabili og öllum pöntunum á því tímabili tengd við
        þær tekjur sem sú pöntun gefur á því tímabili"""
        list_of_dates = [str(day)for day in list_of_dates]
        dict_of_orders = self.get_orders()
        total_revenue = 0
        string_of_orders = ""
        for order_number, order in dict_of_orders.items():
            counter = 0
            list_of_days = order.get_duration()
            price_of_order = order.get_price()
            for day in list_of_days:
                if day in list_of_dates:
                    counter += 1
            ratio = counter/len(list_of_days)
            price_of_order_in_month = (ratio * float(price_of_order))/VSK
            if counter:
                new_order_string = "\t{:^15} | {:>9,.0f} ISK\n".format(
                    order_number, price_of_order_in_month)
                string_of_orders += new_order_string
            total_revenue += price_of_order_in_month
        return total_revenue, string_of_orders

    def get_orders(self):
        """Skilar dict með pöntunarnúmeri sem key og stökum af
        pöntunum sem value"""
        return self.__order_repo.get_orders()

    def get_price_of_extra_insurance(self):
        """Skilar verði á aukatryggingu"""
        price_of_insurance = self.__car_repo.get_car_prices()
        price_of_insurance = price_of_insurance["Aukatrygging"]
        return float(price_of_insurance)

    def get_price_of_mandated_insurance(self):
        """Skilar verði á skyldutryggingu"""
        price_of_insurance = self.__car_repo.get_car_prices()
        price_of_insurance = price_of_insurance["Skyldutrygging"]
        return float(price_of_insurance)

    def price_of_rent(self, licence_plate, discount, insurance, start_date, end_date):
        """Tekur inn bílnúmer, afslátt, tryggingar, og dagsetningar og
        reiknar úr heildarverð pöntunar með VSK"""
        the_car = self.__car_repo.get_car(licence_plate)
        price_of_car = the_car.price_vehicle()
        price_of_car = float(price_of_car)
        price_of_extra_insurance = self.get_price_of_extra_insurance()
        price_of_mandated_insurance = self.get_price_of_mandated_insurance()
        list_of_days = self.list_of_days(start_date, end_date)
        start = list_of_days[STARTDATE]
        end = list_of_days[ENDDATE]
        step = timedelta(days=1)
        days_of_rent = 0
        while start <= end:
            days_of_rent += 1
            start += step
        price_of_rent = days_of_rent * price_of_car
        print("Verð bíls í {} daga án skyldutrygginga og VSK: {:,.0f} ISK".format(
            days_of_rent, float(price_of_rent)))
        price_of_mandated = days_of_rent * price_of_mandated_insurance
        price_of_rent += price_of_mandated
        discount = self.change_discount_to_float(discount)
        if insurance:
            final_price = price_of_extra_insurance * days_of_rent + price_of_rent
            if discount:
                final_price = final_price * discount
            return final_price*VSK  # Það verð sem er skilað ef keyptar eru aukatryggingar
        if discount:
            # Hér er verð án aukatrygginga en með afsl
            price_of_rent = price_of_rent * discount
            return price_of_rent*VSK
        else:
            return price_of_rent*VSK  # Verð án aukatryggingar og án afsláttar

    def change_price(self, order, new_price):
        """Tekur inn stak af pöntun og nýtt verð og breytir verðinu"""
        order.change_price(new_price)

    def change_discount(self, order_number, new_discount):
        """Tekur inn pöntunarnúmer og breyttan afslátt og
        breytir afslættinum í pöntununni og uppfærir verðið"""
        order = self.__order_repo.get_order(order_number)
        order.change_discount(new_discount)
        insurance = order.get_insurance()
        duration_list = order.get_duration()
        licence_plate = order.get_licence_plate()
        start = duration_list[STARTDATE]
        end = duration_list[ENDDATE]
        price = self.price_of_rent(
            licence_plate, new_discount, insurance, start, end)
        self.change_price(order, price)
        self.__order_repo.save_new_orders()

    def change_discount_to_float(self, discount):
        """Tekur inn afslátt í prósentum og breytir honum í float hlutfall"""
        discount = float(discount)/100
        return 1-discount

    def find_order(self, order_number):
        """Tekur inn pöntunarnúmer og ef það er til pöntun á því
        númeri og skilar henni"""
        order_dict = self.__order_repo.get_orders()
        for order, _ in order_dict.items():
            if order == order_number:
                return order_dict[order_number]
        return False
