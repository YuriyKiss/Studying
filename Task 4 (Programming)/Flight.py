from Validator import Validator
import json


class Flight:
    def __init__(self,
                 _id, _departure_country, _arrival_country, _departure_time, _arrival_time, _ticket_price, _company):
        self._id = Validator.check_positive(_id)
        self._departure_country = Validator.check_name(_departure_country)
        self._arrival_country = Validator.check_name(_arrival_country)
        self._departure_time = Validator.check_time(_departure_time)
        self._arrival_time = Validator.check_time(_arrival_time)
        self._ticket_price = Validator.check_positive(_ticket_price)
        self._company = Validator.check_name(_company)

    def __str__(self):
        string = ""
        for attr, values in vars(self).items():
            string += str(attr) + ": " + str(values) + "\n"

        return string

    def edit(self):
        for attr, values in vars(self).items():
            setattr(self, attr, input(attr + " = "))

        self.object_validation()

    def object_validation(self):
        Validator.check_positive(self._id)
        Validator.check_name(self._departure_country)
        Validator.check_name(self._arrival_country)
        Validator.check_time(self._departure_time)
        Validator.check_time(self._arrival_time)
        Validator.check_positive(self._ticket_price)
        Validator.check_name(self._company)
        Validator.compare_dates(self._departure_time, self._arrival_time)
        Validator.check_country(self._arrival_country)
        Validator.check_country(self._departure_country)
        Validator.check_company(self._company)

    @classmethod
    def read_json(cls, line):
        flight_object = Flight(**json.loads(line))
        return flight_object

    def data_to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def get_id(self):
        return self._id

    def get_departure_country(self):
        return self._departure_country

    def get_arrival_country(self):
        return self._arrival_country

    def get_departure_time(self):
        return self._departure_time

    def get_arrival_time(self):
        return self._arrival_time

    def get_ticket_price(self):
        return self._ticket_price

    def get_company(self):
        return self._company

    def set_departure_country(self, text):
        self._departure_country = text

    def set_arrival_country(self, text):
        self._arrival_country = text

    def set_departure_time(self, text):
        self._departure_time = text

    def set_arrival_time(self, text):
        self._arrival_time = text

    def set_ticket_price(self, text):
        self._ticket_price = text

    def set_company(self, text):
        self._company = text
