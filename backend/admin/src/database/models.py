from sqlalchemy import Integer, String
from main import db

class User(db.Model):
    id = db.Column(Integer, primary_key=True)
    email = db.Column(String)
    password = db.Column(String)


db.create_all()