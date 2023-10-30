from src.database.models import *
from src.app_setup import create_app

app = create_app()
from src.handlers.registration import *

@app.route("/ping")
def ping():
    return "Success"

