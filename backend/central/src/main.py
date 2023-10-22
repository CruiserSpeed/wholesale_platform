from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from settings import DATABASE_URI


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
db = SQLAlchemy(app)

CORS(app)

import database.models
import handlers.registration

