# Importing Flask, SQLAlchemy and Marshmallow to work with
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize Application Framework
app = Flask(__name__)

# Create link inside application to database (in this case - PostgreSQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:1234@localhost:5432/homework'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database, then Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)
