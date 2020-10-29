import os


class Validator:
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
    def check_name(func):
        def func_wrapper(self, string):
            if not all(x.isalpha() or x.isspace() for x in string):
                print("This field should only contain alphabetic symbols")
            func(self, string)

        return func_wrapper

    @staticmethod
    def check_people(func):
        def func_wrapper(self, people):
            try:
                people = int(people)
                if people < 0:
                    print("Can't be less than 1 people. Changing to 1")
                    func(self, 1)
                elif people > 4:
                    print("Can't be more than 4 people. Changing to 4")
                    func(self, 4)
                else:
                    func(self, people)
            except ValueError:
                print("Amount of people should be INT type")

        return func_wrapper

    @staticmethod
    def check_minute(func):
        def func_wrapper(self, minute):
            try:
                minute = int(minute)
                if minute < 0:
                    print("Can't be less than 0 minutes. Changing to 0")
                    func(self, 0)
                elif minute > 59:
                    print("Can't be more than 59 minutes. Changing to 59")
                    func(self, 59)
                else:
                    func(self, int(minute))
            except ValueError:
                print("Minutes must be INT type")

        return func_wrapper

    @staticmethod
    def check_hour(func):
        def func_wrapper(self, hour):
            try:
                hour = int(hour)
                if hour < 0:
                    print("Can't be less than 0 hours. Changing to 0")
                    func(self, 0)
                elif hour > 23:
                    print("Can't be more than 23 hours. Changing to 23")
                    func(self, 23)
                else:
                    func(self, int(hour))
            except ValueError:
                print("Hours must be INT type")

        return func_wrapper

    @staticmethod
    def check_end_time(func):
        def func_wrapper(self, start_time, end_time):
            if end_time.get_minute() < start_time.get_minute() or \
                    end_time.get_hour() <= start_time.get_hour():
                print("Warning: End time is earlier than start time!")
            func(self, start_time, end_time)
        return func_wrapper

    @staticmethod
    def check_file_existence(func):
        def func_wrapper(self, path):
            if not (os.path.isfile(path) and path.endswith(".txt")):
                print("File does not exist")
                path = Validator.input_file("Input correct file name: ")

            func(self, path)

        return func_wrapper
