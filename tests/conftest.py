import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from db.database import Base, get_db
import os
from dotenv import load_dotenv

DATABASE_URL_TEST = os.getenv("DATABASE_URL_TEST")

engine_test = create_engine(DATABASE_URL_TEST)
SessionLocalTest = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)


def override_get_db():
    db = SessionLocalTest()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="function")
def client():
    Base.metadata.create_all(bind=engine_test)
    yield TestClient(app)
    Base.metadata.drop_all(bind=engine_test)