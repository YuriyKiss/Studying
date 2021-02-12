from validator import Validator


class BlaBlaCar:
    def __init__(self, name, amount, start_time, end_time, start_place, end_place):
        self.set_driver_name(name)
        self.set_people(amount)
        self.set_start_time(start_time)
        self.set_end_time(self._start_time, end_time)
        self.set_start_place(start_place)
        self.set_end_place(end_place)

    def __str__(self):
        string = ""
        for attr, values in vars(self).items():
            string += str(attr) + ": " + str(values) + "\n"

        return string

    @Validator.check_name
    def set_driver_name(self, name):
        self._name = name

    @Validator.check_people
    def set_people(self, amount):
        self._people = amount

    def set_start_time(self, time):
        self._start_time = time

    @Validator.check_end_time
    def set_end_time(self, start_time, end_time):
        self._end_time = end_time

    @Validator.check_name
    def set_start_place(self, place):
        self._start_place = place

    @Validator.check_name
    def set_end_place(self, place):
        self._end_place = place
