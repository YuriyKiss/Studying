# Importing database to create class model and Marshmallow to create Flight Schema
from app import db, ma

from validation.validator import Validator
import datetime


class MyDateTime(db.TypeDecorator):
    impl = db.DateTime

    def process_bind_param(self, value, dialect):
        if type(value) is str:
            return datetime.datetime.strptime(value, '%Y-%m-%d %H:%M')
        return value


# Flight Class/Model
class Flight(db.Model):
    __tablename__ = "flights"

    id = db.Column(db.Integer, primary_key=True)
    departure_country = db.Column(db.String(50))
    arrival_country = db.Column(db.String(50))
    departure_time = db.Column(MyDateTime)
    arrival_time = db.Column(MyDateTime)
    ticket_price = db.Column(db.Float)
    company = db.Column(db.String(25))
    user_id = db.Column(db.Integer)

    def __init__(self,
                 _id, _departure_country, _arrival_country, _departure_time, _arrival_time, _ticket_price, _company,
                 _user_id):
        self.set_id(_id)
        self.set_departure_country(_departure_country)
        self.set_arrival_country(_arrival_country)
        self.set_departure_time(_departure_time)
        self.set_arrival_time(_arrival_time)
        self.set_ticket_price(_ticket_price)
        self.set_company(_company)
        self.user_id = _user_id

        self._compare_dates(self.departure_time, self.arrival_time)

    def get_data_integrity(self):
        respond = []
        for a in self.get_attributes():
            if getattr(self, a) is None:
                respond.append(a)
        return respond

    @staticmethod
    def get_attributes():
        attributes = []
        for attr, values in vars(Flight).items():
            if not attr.startswith("_") and not attr.startswith("set") and not attr.startswith("get"):
                attributes.append(attr)
        return attributes

    @Validator.check_positive
    def set_id(self, id_num):
        self.id = id_num

    @Validator.check_country
    def set_departure_country(self, info):
        self.departure_country = info

    @Validator.check_country
    def set_arrival_country(self, info):
        self.arrival_country = info

    @Validator.check_time
    def set_departure_time(self, date):
        self.departure_time = date

    @Validator.check_time
    def set_arrival_time(self, date):
        self.arrival_time = date

    @Validator.check_float
    @Validator.check_positive
    def set_ticket_price(self, num):
        self.ticket_price = num

    @Validator.check_company
    def set_company(self, info):
        self.company = info

    @Validator.compare_dates
    def _compare_dates(self, d1, d2):
        if d1 is None or d2 is None:
            self.departure_time = None
            self.arrival_time = None

        return self


# Product Schema
class FlightSchema(ma.Schema):
    class Meta:
        fields = ('id', 'departure_country', 'arrival_country', 'departure_time', 'arrival_time', 'ticket_price',
                  'company')
