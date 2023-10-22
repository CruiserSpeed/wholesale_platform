from database.models import User

def test_request_example(mocker, client):
    mock = mocker.patch('flask_sqlalchemy._QueryProperty.__get__')
    mock.return_value.filter_by.return_value.first.return_value = User(email="test@mail.ru", password="12345")

    response = client.post("/sign_in", json={
        "email": "test@mail.ru",
        "password": "12345",
    })
    assert response.json["success"] == True