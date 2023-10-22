from main import app, db
from flask import request
import json
from database.models import User


@app.route("/sign_in", methods=['POST'])
def sign_in():
    data = json.loads(request.data)
    print(data)
    
    email = data["email"]
    password = data["password"]
    user = db.session.execute(db.select(User).filter_by(email=email)).scalar()
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
