from flask import Flask
from flask_cors import CORS
from settings import DATABASE_URI
from database.models import *

def init_db():
    db.create_all()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    CORS(app)

    db.init_app(app)
    with app.app_context():
        init_db()

    return app


app = create_app()
from handlers.registration import *