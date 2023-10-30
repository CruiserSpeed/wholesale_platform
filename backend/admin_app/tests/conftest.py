import pytest
from flask import Flask
from src.database.models import db

@pytest.fixture(autouse=True)
def mock_application(mocker):
    print("WAS HERE")
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    app.config["TESTING"] = True
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    mock = mocker.patch("src.app_setup.create_app")
    mock.return_value = app

@pytest.fixture()
def app():
    from src.main import app
    return app

@pytest.fixture()
def client(app):
    return app.test_client()