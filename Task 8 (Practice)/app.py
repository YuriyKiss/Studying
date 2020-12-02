# Importing Flask, SQLAlchemy and Marshmallow to work with
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager

from nothing_to_look_at import app_key
# Initialize Application Framework
app = Flask(__name__)
app.secret_key = app_key

# Create link inside application to database (in this case - PostgreSQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:1234@localhost:5432/second'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database, then Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Initializing login manager
login_m = LoginManager()
login_m.init_app(app)
