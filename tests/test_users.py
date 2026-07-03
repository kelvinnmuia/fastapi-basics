from fastapi.testclient import TestClient
from app.main import app
from app import schemas
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import get_db, Base

# SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:P0stgres26@localhost:5432/fastapi_test"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# Base = declarative_base()
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_root():
    
    res = client.get("/")
    print(res.json())
    assert res.json().get("message") == "Welcome to my first api in python"
    assert res.status_code == 200
    
def test_create_user():
    res = client.post("/users/", json={"email": "hall3@mail.com", "password": "hall3pwd123"})
    # print(res.json())
    new_user = schemas.UserOut(**res.json())
    # assert res.json().get("email") == "hall3@mail.com"
    assert new_user.email == "hall3@mail.com"
    assert res.status_code == 201