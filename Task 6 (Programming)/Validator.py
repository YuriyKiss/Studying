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
            func(self, string)

        return func_wrapper

    @staticmethod
    def check_time(func):
        def func_wrapper(self, date):
            try:
                datetime.datetime.strptime(date, '%Y-%m-%d %H:%M')
            except ValueError:
                print("Incorrect data format. Correct is YYYY-MM-DD HH:MM")
            func(self, date)

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
            func(self, info)

        return func_wrapper

    @staticmethod
    def check_company(func):
        def func_wrapper(self, info):
            if str(info).lower() not in enums.Companies.__members__:
                print("That company " + info + " is not listed in Enum")
            func(self, info)

        return func_wrapper

    @staticmethod
    def compare_dates(func):
        def func_wrapper(self, d1, d2):
            if not d1 < d2:
                print("Time Error: " + d1 + " Departure happened later than " + d2 + " Arrival!")
            func(self, d1, d2)

        return func_wrapper

    @staticmethod
    def check_obj(func):
        def func_wrapper(self):
            func(self)

            self.set_id(self.get_id())
            self.set_departure_country(self.get_departure_country())
            self.set_arrival_country(self.get_arrival_country())
            self.set_departure_time(self.get_departure_time())
            self.set_arrival_time(self.get_arrival_time())
            self.set_ticket_price(self.get_ticket_price())
            self.set_company(self.get_company())

            self.compare_dates(self.get_departure_time(), self.get_arrival_time())

        return func_wrapper
