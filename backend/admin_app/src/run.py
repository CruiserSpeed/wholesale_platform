from main import app
from flask_cors import CORS
from database.models import *
from globals import (
    APP_PORT,
    APP_IS_DEBUG,
)

app.run(host='0.0.0.0', port=APP_PORT, debug=APP_IS_DEBUG)
