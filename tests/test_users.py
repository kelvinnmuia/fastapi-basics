from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    res = client.get("/")
    print(res.json())
    assert res.json().get("message") == "Welcome to my first api in python"