from main import app
from flask import request


@app.route("/sing_in", methods=['GET'])
def sign_in():
    print(request.data)
    return "sign in response"

@app.route("/sing_up", methods=['GET'])
def sign_up():
    return "Sing up response"