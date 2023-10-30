from main import app
from flask import request
import json
from database.models import db, User


@app.route("/sign_in", methods=['POST'])
def sign_in():
    data = json.loads(request.data)
    
    email = data["email"]
    password = data["password"]
    user = User.query.filter_by(email=email).first()
    if user is None or user.password != password:
        return {"success": False}
    return {"success": True}

@app.route("/sign_up", methods=['POST'])
def sign_up():
    data = json.loads(request.data)
    print(data)
    user = User()
    user.email = data["email"]
    user.password = data["password"]

    db.session.add(user)
    db.session.commit()
    return "Sing up response"
