from http import HTTPStatus


def test_get_all_courser(client):
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello World"}


def test_get_courses(client):
    response = client.get("/cursos/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "1": {"aulas": 20, "horas": 10, "titulo": "LlamaIndex - Introdução"},
        "2": {"aulas": 15, "horas": 8, "titulo": "FastAPI - Introdução"},
    }
