from flask import Flask
from flask_cors import CORS
from globals import (
    DATABASE_URI,
)
from database.models import *
import os


def create_app():
    print(f"db uri: {DATABASE_URI}")
    print(os.listdir("./src/api_walker"))
    app = Flask(__name__, template_folder="assets")
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    CORS(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
