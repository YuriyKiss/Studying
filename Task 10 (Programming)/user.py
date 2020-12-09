from app import db, ma
from nothing_to_look_at import encode
from validation.validator import Validator
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    email = db.Column(db.String(50))
    password = db.Column(db.String)
    role = db.Column(db.String(10))

    def __init__(self, id_, first_name, last_name, email, password, role):
        self.set_id(id_)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_password(password)
        self.set_role(role)

    def get_data_integrity(self):
        respond = []
        for a in self.get_attributes():
            if getattr(self, a) is None:
                respond.append(a)
        return respond

    @staticmethod
    def get_attributes():
        attributes = []
        for attr, values in vars(User).items():
            if not attr.startswith("_") and not attr.startswith("set") and not attr.startswith("get"):
                attributes.append(attr)
        return attributes

    def get_pass(self):
        return self.password

    def get_id(self):
        return self.id

    def get_mail(self):
        return self.email

    def get_role(self):
        return self.role

    @Validator.check_positive
    def set_id(self, id_num):
        self.id = id_num

    @Validator.check_name
    def set_first_name(self, first_name):
        self.first_name = first_name

    @Validator.check_name
    def set_last_name(self, last_name):
        self.last_name = last_name

    @Validator.check_email
    def set_email(self, mail):
        self.email = mail

    @Validator.check_role
    def set_role(self, role):
        self.role = role

    @Validator.check_pass
    def set_password(self, _password):
        if _password is None:
            self.password = None
            return
        self.password = encode(_password)


# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'role')
