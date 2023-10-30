
from src.database.models import User, db

def test_ping(client):
    response = client.get("/ping")
    assert response.text == "Success"
    
def test_request_example(mocker, app, client):
    with app.app_context():
        user = User()
        user.email = "test@mail.ru"
        user.password = "12345"
        db.session.add(user)
        db.session.commit()

    response = client.post("/sign_in", json={
        "email": "test@mail.ru",
        "password": "12345",
    })
    assert response.json["success"] == True
