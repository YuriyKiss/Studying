from math import sqrt
from math import ceil


class Validator:
    @staticmethod
    def input_int(message):
        while True:
            try:
                quantity = int(input(message))
                if quantity <= 0:
                    print('\nInteger should be bigger than 0')
                    continue
                return quantity
            except ValueError:
                print('\nPlease enter an integer')

    @staticmethod
    def is_prime(num):
        if num == 1 or num == 4:
            return False

        for i in range(2, ceil(sqrt(num))):
            if num % i == 0:
                return False

        return True
