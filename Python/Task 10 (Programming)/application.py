# Importing Flask, Flask-Login, SQLAlchemy and Marshmallow to work with
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager

# Importing app key and config
from validation.codes import app_key
from config import *

# Initializing Application Framework
app = Flask(__name__)
app.secret_key = app_key

# Creating link inside application to database (in this case - PostgreSQL)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{USER}:{PASSWORD}@{LINK}:{PORT}/{DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializing database, then Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Initializing login manager
login_m = LoginManager()
login_m.init_app(app)
