from fastapi.testclient import TestClient
import pytest
from app.main import app
from app import schemas
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import get_db, Base
from alembic import command

# SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:P0stgres26@localhost:5432/fastapi_test"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()
# def override_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
        
# app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="function")
def session():
    print("the session fixture is running")
    # command.upgrade("head")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    # command.downgrade("base")
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
@pytest.fixture(scope="function")
def client(session):
    def override_get_db():
    # db = TestingSessionLocal()
        try:
            yield session
        finally:
            session.close() 
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)