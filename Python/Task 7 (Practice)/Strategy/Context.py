class Context:
    def __init__(self):
        self._strategy = None

    def set_strategy(self, strategy):
        self._strategy = strategy
        print("Strategy set to " + self._strategy.get_name())

    def get_strategy(self):
        if self._strategy is None:
            return None
        return self._strategy.get_name()

    def use_strategy(self, op_list, amount, pos):
        if self._strategy is not None:
            self._strategy.generate(op_list, amount, pos)
        else:
            print("StrategyError: Strategy is not set yet")
