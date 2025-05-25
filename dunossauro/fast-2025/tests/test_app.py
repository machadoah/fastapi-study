from fastapi import status
from fastapi.testclient import TestClient

from fasttodo.app import app
from fasttodo.static.htmls import ENDPOINT_HEALTH


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == status.HTTP_200_OK  # Assert
    assert response.json() == {'message': 'Hello World'}  # Assert


def test_health_deve_retornar_ok_e_html():
    client = TestClient(app)  # Arrange

    response = client.get('/health')  # Act

    assert response.status_code == status.HTTP_200_OK  # Assert
    assert (
        response.headers['content-type'] == 'text/html; charset=utf-8'
    )  # Assert

    assert (
        response.text == ENDPOINT_HEALTH  # Assert
    )
