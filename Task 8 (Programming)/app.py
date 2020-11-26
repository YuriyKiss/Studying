import os

from flask import Flask  # Importing Flask,
from flask_sqlalchemy import SQLAlchemy  # SQLAlchemy and Marshmallow
from flask_marshmallow import Marshmallow  # to work with

app = Flask(__name__)  # Init Application

basedir = os.path.abspath(os.path.dirname(__file__))  # Get DB directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:@localhost:5432/products'  # Connect app and DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # Init DB
ma = Marshmallow(app)  # Init Marshmallow
