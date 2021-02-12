import abc


class Strategy(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def generate(self, *args):
        pass

    @abc.abstractmethod
    def get_name(self):
        pass
