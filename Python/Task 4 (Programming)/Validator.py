import datetime
import os
import enums


class Validator:
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
    def check_positive(num):
        if int(num) <= 0:
            print("This number cannot reach negative values: " + str(num))
        return num

    @staticmethod
    def input_name(message):
        while True:
            string = input(message)
            if not all(x.isalpha() or x.isspace() for x in string):
                print("This string should only contain alphabetic symbols: " + string)
                continue
            return string

    @staticmethod
    def check_name(string):
        if all(x.isalpha() or x.isspace() for x in string):
            return string
        else:
            print("Countries and companies should only contain alphabetic symbols")

    @staticmethod
    def input_time(message):
        while True:
            try:
                date = input(message)
                datetime.datetime.strptime(date, '%Y-%m-%d %H:%M')
                return date
            except ValueError:
                print("Incorrect data format. Correct is YYYY-MM-DD HH:MM")
                continue

    @staticmethod
    def check_time(date):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d %H:%M')
            return date
        except ValueError:
            print("Incorrect data format. Correct is YYYY-MM-DD HH:MM")

    @staticmethod
    def compare_dates(d1, d2):
        if d1 < d2:
            return
        else:
            print("Time Error: " + d1 + " Departure happened later than " + d2 + " Arrival!")

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
    def check_file_existence(path):
        if os.path.isfile(path) and path.endswith(".txt"):
            return path
        else:
            print("File does not exist")
            return Validator.input_file("Input correct file name: ")

    @staticmethod
    def check_country(info):
        if str(info).lower() not in enums.Countries.__members__:
            print("That country " + info + " is not listed in Enum")
        else:
            return

    @staticmethod
    def check_company(info):
        if str(info).lower() not in enums.Companies.__members__:
            print("That company " + info + " is not listed in Enum")
        else:
            return
