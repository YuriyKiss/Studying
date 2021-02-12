import os
from math import sqrt
from math import ceil


class Validator:
    @staticmethod
    def input_positive_int(message):
        while True:
            try:
                num = int(input(message))
                if num < 0:
                    print("Integer should be positive")
                    continue
                return num
            except ValueError:
                print("This should be an integer type")

    @staticmethod
    def input_int_in_bounds(message, start, end):
        while True:
            try:
                num = int(input(message))
                if num < start:
                    print("Integer should be equal/bigger than " + str(start))
                    continue
                if num > end:
                    print("Integer should be equal/smaller than " + str(end))
                    continue
                return num
            except ValueError:
                print("This should be an integer type")

    @staticmethod
    def input_file(message):
        while True:
            file = input(message)
            if not file.endswith(".txt") or not os.path.isfile(file):
                print("This file doesn't exist")
                continue
            return file

    @staticmethod
    def check_file(path):
        if isinstance(path, int):
            return False
        if not path.endswith(".txt") or not os.path.isfile(path):
            return False
        else:
            return True

    @staticmethod
    def check_int(num):
        while True:
            try:
                return int(num)
            except ValueError:
                print("This number is not int. Returning 0")
                return 0

    @staticmethod
    def check_context(cont):
        if cont.get_strategy() is None:
            print("The strategy is not set yet")
            return True
        else:
            return False

    @staticmethod
    def check_op_list(func):
        def func_wrapper(name, op_list, obs):
            if op_list.is_empty():
                print("List is empty")
            else:
                func(name, op_list, obs)
        return func_wrapper

    @staticmethod
    def is_prime(num):
        if num == 1 or num == 4:
            return False

        for i in range(2, ceil(sqrt(num))):
            if num % i == 0:
                return False

        return True
