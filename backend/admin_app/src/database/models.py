from sqlalchemy import Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(Integer, primary_key=True)
    email = db.Column(String)
    password = db.Column(String)
