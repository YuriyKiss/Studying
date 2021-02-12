import datetime
import os
import enums


class Validator:
    # ---------------------------------------------------------------------------------------------------------------- #
    # Validations that are used in Main Menu
    @staticmethod
    def input_positive(message):
        while True:
            try:
                num = int(input(message))
                if num <= 0:
                    print("This number cannot reach negative values: " + str(num))
                    continue
                return num
            except ValueError:
                print("It is not an integer")

    @staticmethod
    def input_file(message):
        while True:
            path = input(message)
            if os.path.isfile(path) and path.endswith(".txt"):
                return path
            else:
                print("File name is incorrect")
                continue

    @staticmethod
    def input_name(message):
        while True:
            string = input(message)
            if not all(x.isalpha() or x.isspace() for x in string):
                print("This should only contain alphabetic symbols")
                continue
            else:
                return string

    # ---------------------------------------------------------------------------------------------------------------- #
    # Class validations
    @staticmethod
    def check_positive(func):
        def func_wrapper(self, num):
            if int(num) <= 0:
                print("This number cannot reach negative values: " + str(num))
                func(self, -1)
            else:
                func(self, num)

        return func_wrapper

    @staticmethod
    def check_float(func):
        def func_wrapper(self, num):
            try:
                num = round(float(num), 2)
            except ValueError:
                print('This number can be float type')
            func(self, num)

        return func_wrapper

    @staticmethod
    def check_name(func):
        def func_wrapper(self, string):
            if not all(x.isalpha() or x.isspace() for x in string):
                print("Countries and companies should only contain alphabetic symbols")
                func(self, "a")
            else:
                func(self, string)

        return func_wrapper

    @staticmethod
    def check_time(func):
        def func_wrapper(self, date):
            try:
                if isinstance(date, int):
                    raise ValueError
                datetime.datetime.strptime(date, '%Y-%m-%d %H:%M')
                func(self, date)
            except ValueError:
                print("Incorrect data format. Correct is YYYY-MM-DD HH:MM")
                func(self, -1)

        return func_wrapper

    @staticmethod
    def check_file_existence(func):
        def func_wrapper(self, path):
            if not (os.path.isfile(path) and path.endswith(".txt")):
                print("File does not exist")
                path = Validator.input_file("Input correct file name: ")

            func(self, path)

        return func_wrapper

    @staticmethod
    def check_country(func):
        def func_wrapper(self, info):
            if str(info).lower() not in enums.Countries.__members__:
                print("That country " + info + " is not listed in Enum")
                func(self, "a")
            else:
                func(self, info)

        return func_wrapper

    @staticmethod
    def check_company(func):
        def func_wrapper(self, info):
            if str(info).lower() not in enums.Companies.__members__:
                print("That company " + info + " is not listed in Enum")
                func(self, "a")
            else:
                func(self, info)

        return func_wrapper

    @staticmethod
    def compare_dates(func):
        def func_wrapper(self, d1, d2):
            if isinstance(d1, int) or isinstance(d2, int):
                print("Time Error: One of the dates is not correct. Can't compare dates!")
                func(self, -1, -1)
            elif not d1 < d2:
                print("Time Error: " + d1 + " Departure happened later than " + d2 + " Arrival!")
                func(self, -1, -1)
            else:
                func(self, d1, d2)

        return func_wrapper

    @staticmethod
    def check_object(func):
        def func_wrapper(self, flight, x):
            if isinstance(x, int):
                if x > len(self.get_array()):
                    print("Exceeding array limit. Such ID doesn't exist")
                    return
            func(self, flight, x)
            if x is None:
                flight.set_id(self.get_array()[len(self.get_array()) - 1].get_id())
                flight.set_departure_country(self.get_array()[len(self.get_array()) - 1].get_departure_country())
                flight.set_arrival_country(self.get_array()[len(self.get_array()) - 1].get_arrival_country())
                flight.set_departure_time(self.get_array()[len(self.get_array()) - 1].get_departure_time())
                flight.set_arrival_time(self.get_array()[len(self.get_array()) - 1].get_arrival_time())
                flight.set_ticket_price(self.get_array()[len(self.get_array()) - 1].get_ticket_price())
                flight.set_company(self.get_array()[len(self.get_array()) - 1].get_company())

                flight.compare_dates(self.get_array()[len(self.get_array()) - 1].get_departure_time(),
                                    self.get_array()[len(self.get_array()) - 1].get_arrival_time())

        return func_wrapper
