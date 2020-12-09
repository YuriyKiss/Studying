import datetime

from app import db, ma
from custom_time import MyDateTime
from validation.validator import Validator


# Order Class/Model
class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    flight_id = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    date = db.Column(MyDateTime)

    def __init__(self, _id, _user_id, _flight_id, _amount):
        self.set_id(_id)
        self.set_user_id(_user_id)
        self.set_flight_id(_flight_id)
        self.set_amount(_amount)
        self.date = datetime.datetime.now()

    @Validator.check_positive
    def set_id(self, id):
        self.id = id

    @Validator.check_positive
    def set_user_id(self, user_id):
        self.user_id = user_id

    @Validator.check_positive
    def set_flight_id(self, flight_id):
        self.flight_id = flight_id

    @Validator.check_positive
    def set_amount(self, amount):
        self.amount = amount


# Order Schema
class OrderSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'flight_id', 'amount', 'date')
