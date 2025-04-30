"""Test configuration"""

import sys
import os
import pytest
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app
from fastapi.testclient import TestClient
from app.models.user import User
from app.models.base import Base
from app.database import get_db

DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False,
    },
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    database = TestingSessionLocal()
    try:
        yield database
    finally:
        database.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="function")
def client():
    """
    Client creation
    """
    with TestClient(app) as c:
        yield c

@pytest.fixture(autouse=True)
def setup_db():
    """
    Create and destroy tables before and after test automatically
    Crea y destruye las tablas antes y después de cada test automáticamente.
    """
    Base.metadata.create_all(bind=engine)
    yield  # Aquí es donde se ejecuta el test
    Base.metadata.drop_all(bind=engine)
