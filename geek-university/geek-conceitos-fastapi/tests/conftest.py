from fastapi.testclient import TestClient
from geek_conceitos_fastapi.app import app
import pytest


@pytest.fixture
def client():
    return TestClient(app)
