import datetime
import validation.enums


class Validator:
    @staticmethod
    def check_id(id_, data):
        if id_ <= str(0):
            return {"status": 404, "message": "Flight not found"}, {"info": "ID cannot be <= 0"}
        if data is None:
            return {"status": 404, "message": "Flight not found"}, {"info": "Such ID doesn't exist"}
        else:
            return None

    @staticmethod
    def check_positive(func):
        def func_wrapper(self, num):
            if int(num) <= 0:
                print("This number cannot reach negative values: " + str(num))
                func(self, None)
            else:
                func(self, num)

        return func_wrapper

    @staticmethod
    def check_float(func):
        def func_wrapper(self, num):
            try:
                num = round(float(num), 2)
            except ValueError:
                print('This number should be float type')
            func(self, num)

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
                func(self, None)

        return func_wrapper

    @staticmethod
    def check_country(func):
        def func_wrapper(self, info):
            if str(info).lower() not in validation.enums.Countries.__members__:
                print("That country " + info + " is not listed in Enum")
                func(self, None)
            else:
                func(self, info)

        return func_wrapper

    @staticmethod
    def check_company(func):
        def func_wrapper(self, info):
            if str(info).lower() not in validation.enums.Companies.__members__:
                print("That company " + info + " is not listed in Enum")
                func(self, None)
            else:
                func(self, info)

        return func_wrapper

    @staticmethod
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
