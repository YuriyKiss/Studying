from Validator import Validator
import json


class Flight:
    def __init__(self,
                 _id, _departure_country, _arrival_country, _departure_time, _arrival_time, _ticket_price, _company):
        self.set_id(_id)
        self.set_departure_country(_departure_country)
        self.set_arrival_country(_arrival_country)
        self.set_departure_time(_departure_time)
        self.set_arrival_time(_arrival_time)
        self.set_ticket_price(_ticket_price)
        self.set_company(_company)

        self.compare_dates(_departure_time, _arrival_time)

    def __str__(self):
        string = ""
        for attr, values in vars(self).items():
            string += str(attr) + ": " + str(values) + "\n"

        return string

    def __eq__(self, other):
        return self.get_id() == other.get_id() and \
               self.get_departure_country() == other.get_departure_country() and \
               self.get_arrival_country() == other.get_arrival_country() and \
               self.get_departure_time() == other.get_departure_time() and \
               self.get_arrival_time() == other.get_arrival_time() and \
               self.get_ticket_price() == other.get_ticket_price() and \
               self.get_company() == other.get_company()

    def get_attributes(self):
        return [attr for attr in vars(self)]

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

    @Validator.compare_dates
    def compare_dates(self, d1, d2):
        self._departure_time = d1
        self._arrival_time = d2

        return self

    @Validator.check_positive
    def set_id(self, id_num):
        self._id = id_num

    @Validator.check_country
    def set_departure_country(self, text):
        self._departure_country = text

    @Validator.check_country
    def set_arrival_country(self, text):
        self._arrival_country = text

    @Validator.check_time
    def set_departure_time(self, date):
        self._departure_time = date

    @Validator.check_time
    def set_arrival_time(self, date):
        self._arrival_time = date

    @Validator.check_float
    @Validator.check_positive
    def set_ticket_price(self, num):
        self._ticket_price = num

    @Validator.check_company
    def set_company(self, text):
        self._company = text
