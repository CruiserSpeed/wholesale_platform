from database.models import *
from app_setup import create_app

app = create_app()
from handlers.registration import *

@app.route("/ping")
def ping():
    return "Success"

