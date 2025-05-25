from time import sleep

from geek_conceitos_fastapi.models import Curso


def fake_db():
    try:
        print("Abrindo conexão com banco de dados ...")
        sleep(1)
    finally:
        print("Fechando conexão com banco de dados ...")
        sleep(1)


cursos = [
    Curso(id=1, titulo="LlamaIndex - Introdução", aulas=1, horas=2),
    Curso(id=2, titulo="FastAPI - Introdução", aulas=1, horas=3),
    Curso(id=3, titulo="FastAPI - Avançado", aulas=1, horas=4),
]
