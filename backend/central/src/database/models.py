from sqlalchemy import Integer, String
from main import db

class User(db.Model):
    id = db.Column(Integer, primary_key=True)
    username = db.Column(String, unique=True, nullable=False)
    email = db.Column(String)
