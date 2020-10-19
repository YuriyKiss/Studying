from Strategy.Strategy import Strategy
from Validator import Validator


class Sequence:
    def __init__(self):
        self.a = 2
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            c = self.a + self.b
            self.a = self.b
            self.b = c

            if Validator.is_prime(self.a):
                return self.a

    def __str__(self):
        return str(self.a)


class StrategyIterator(Strategy):
    def generate(self, op_list, amount, pos):
        p = Sequence()
        for i in range(amount):
            op_list.insert(pos, Validator.check_int(next(iter(p))))
            pos += 1

    def get_name(self):
        return "Iterator"
