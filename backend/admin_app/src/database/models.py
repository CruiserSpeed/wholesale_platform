from sqlalchemy import Integer, String, Boolean
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Admin(db.Model):
    __tablename__ = "admin"

    id = db.Column(Integer, primary_key=True)
    email = db.Column(String)
    password = db.Column(String)
    admin_confirmation_status = db.Column(String)    # "approved", "disapproved", None
    email_confirmation_status = db.Column(String)    # "confirmed", None
    confirmations = db.relationship("Confirmation", back_populates="admin")


class Confirmation(db.Model):
    __tablename__ = "confirmation"

    hash = db.Column(String, primary_key=True)
    value = db.Column(String)
    admin_id = db.Column(db.ForeignKey("admin.id"))
    admin = db.relationship("Admin", back_populates="confirmations")

