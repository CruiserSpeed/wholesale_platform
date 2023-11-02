from main import app
from flask import request
import json
from database.models import db, User
from api_walker.api_walker import send_request_to_api_walker


@app.route("/api_walker", methods=["GET"])
def send_api_walker():
    print("HERE")
    return send_request_to_api_walker()


@app.route("/sign_in", methods=["POST"])
def sign_in():
    data = json.loads(request.data)

    email = data["email"]
    password = data["password"]
    user = User.query.filter_by(email=email).first()
    if user is None or user.password != password:
        return {"success": False}
    return {"success": True}


@app.route("/sign_up", methods=["POST"])
def sign_up():
    data = json.loads(request.data)
    print(data)
    user = User()
    user.email = data["email"]
    user.password = data["password"]

    db.session.add(user)
    db.session.commit()
    return "Sing up response"
