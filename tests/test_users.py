import pytest
from jose import jwt
from app.config import settings
from app import schemas
# from tests.database import client, session

@pytest.fixture
def test_user(client):
    user_data = {"email": "hall3@mail.com", "password": "hall3pwd123"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    # print(res.json())
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user

# def test_root(client):
    
#     res = client.get("/")
#     print(res.json())
#     assert res.json().get("message") == "Welcome to my first api in python"
#     assert res.status_code == 200


    
def test_create_user(client):
    res = client.post("/users/", json={"email": "hall3@mail.com", "password": "hall3pwd123"})
    # print(res.json())
    new_user = schemas.UserOut(**res.json())
    # assert res.json().get("email") == "hall3@mail.com"
    assert new_user.email == "hall3@mail.com"
    assert res.status_code == 201
    
def test_login_user(client, test_user):
    res = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, settings.algorithm)
    id: str = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200
    