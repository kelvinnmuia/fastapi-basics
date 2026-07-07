import pytest
from jose import jwt
from app.config import settings
from app import schemas
# from tests.database import client, session

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

@pytest.mark.parametrize("email, password, status_code", [
    ("wrongemail@mail.com", "hall3pwd123", 403),
    ("hall3@mail.com", "wrongpassword", 403),
    ("wrongemail@mail.com", "wrongpassword", 403),
    (None, "hall3pwd123", 422),
    ("hall3@mail.com", None, 422)
])

def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})
    
    assert res.status_code == status_code
    # assert res.json().get("detail") == "Invalid Credentials"
    