from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from settings import DATABASE_URI


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
db = SQLAlchemy(app)

CORS(app)

from database.models import *

with app.app_context():
    db.create_all()

import handlers.registration

