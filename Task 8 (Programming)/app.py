import os

from flask import Flask  # Importing Flask, SQLAlchemy and Marshmallow to work with
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import psycopg2

app = Flask(__name__)  # Init Application

basedir = os.path.abspath(os.path.dirname(__file__))  # Get DB directory
# Connect app and DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:1234@localhost:5432/homework'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # Init DB
ma = Marshmallow(app)  # Init Marshmallow
