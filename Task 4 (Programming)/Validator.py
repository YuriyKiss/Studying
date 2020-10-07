import datetime


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
        if num <= 0:
            raise ValueError("This number cannot reach negative values: " + str(num))
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
            raise ValueError("Countries and companies should only contain alphabetic symbols")

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
            raise ValueError("Incorrect data format. Correct is YYYY-MM-DD HH:MM")
