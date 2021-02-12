from Strategy.Strategy import Strategy
from Validator import Validator as Valid


class StrategyFile(Strategy):
    def generate(self, op_list, file, pos):
        info = open(file).read().splitlines()

        for x in info:
            data = Valid.check_int(x)
            op_list.insert(pos, data)
            pos += 1

    def get_name(self):
        return "File"
