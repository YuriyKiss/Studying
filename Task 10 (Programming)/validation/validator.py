import re
import datetime
import validation.enums


class Validator:
    # ----------------------------------------- Flight class validations ------------------------------------------ #
    @staticmethod              # ID, Price, and Places validation
    def check_positive(func):
        def func_wrapper(self, num):
            if int(num) <= 0:
                print("This number cannot reach negative values: " + str(num))
                func(self, None)
            else:
                func(self, num)

        return func_wrapper

    @staticmethod              # Departure/Arrival Country validation
    def check_country(func):
        def func_wrapper(self, info):
            if str(info).lower() not in validation.enums.Countries.__members__:
                print("That country " + info + " is not listed in Enum")
                func(self, None)
            else:
                func(self, info)

        return func_wrapper

    @staticmethod               # Departure/Arrival Time validation
    def check_time(func):
        def func_wrapper(self, date):
            try:
                if isinstance(date, int):
                    raise ValueError
                datetime.datetime.strptime(date, '%Y-%m-%d %H:%M')
                func(self, date)
            except ValueError:
                print("Incorrect data format. Correct is YYYY-MM-DD HH:MM")
                func(self, None)

        return func_wrapper

    @staticmethod              # Ticket Price validation
    def check_float(func):
        def func_wrapper(self, num):
            try:
                num = round(float(num), 2)
            except ValueError:
                print('This number should be float type')
            func(self, num)

        return func_wrapper

    @staticmethod              # Company Name validation
    def check_company(func):
        def func_wrapper(self, info):
            if str(info).lower() not in validation.enums.Companies.__members__:
                print("That company " + info + " is not listed in Enum")
                func(self, None)
            else:
                func(self, info)

        return func_wrapper

    @staticmethod              # Comparing Arrival and Departure time
    def compare_dates(func):
        def func_wrapper(self, d1, d2):
            if d1 is None or d2 is None:
                func(self, d1, d2)
            elif isinstance(d1, int) or isinstance(d2, int):
                print("Time Error: One of the dates is not correct. Can't compare dates!")
                func(self, None, None)
            elif not d1 < d2:
                print("Time Error: " + d1 + " Departure happened later than " + d2 + " Arrival!")
                func(self, None, None)
            else:
                func(self, d1, d2)

        return func_wrapper

    # ----------------------------------------- User class validations ------------------------------------------ #
    @staticmethod              # User Name validation
    def check_name(func):
        def func_wrapper(self, string):
            if not all(x.isalpha() for x in string):
                func(self, None)
            else:
                func(self, string)

        return func_wrapper

    @staticmethod              # User Email validation
    def check_email(func):
        def func_wrapper(self, string):
            if re.match('[a-zA-Z0-9._]{3,16}[@][a-zA-Z]{3,6}[.][a-z]{2,3}([.]((ua)|(uk)))?', string):
                func(self, string)
            else:
                func(self, None)

        return func_wrapper

    @staticmethod             # User Password validation
    def check_pass(func):
        def func_wrapper(self, string):
            if re.match("\S{6,16}", str(string)):
                func(self, str(string).lower())
            else:
                func(self, None)

        return func_wrapper

    @staticmethod             # User Role validation
    def check_role(func):
        def func_wrapper(self, string):
            if str(string).lower() not in validation.enums.Roles.__members__:
                print("That role: " + string + " does not exist in Enum")
                func(self, None)
            else:
                func(self, string)

        return func_wrapper
