import pytest

import pytest
from main import app as application
from database.models import db
from mock import patch

@pytest.fixture()
def app():
    application.config.update({
        "TESTING": True,
    })

    yield application


@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture(scope="function")
def sqlalchemy_declarative_base():
    return db.Model

@pytest.fixture(scope="function")
def sqlalchemy_mock_config():
    return [("users", [
        {
            "id": 1,
            "email": "test@mail.ru",
            "password": "12345"
        }
    ])]