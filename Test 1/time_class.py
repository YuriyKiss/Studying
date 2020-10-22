from validator import Validator


class Time:
    def __init__(self, minute, hour):
        self.set_minute(minute)
        self.set_hour(hour)

    def __str__(self):
        return str(self._hour) + ":" + str(self._minute)

    @Validator.check_minute
    def set_minute(self, minute):
        self._minute = minute

    @Validator.check_hour
    def set_hour(self, hour):
        self._hour = hour

    def get_minute(self):
        return self._minute

    def get_hour(self):
        return self._hour
