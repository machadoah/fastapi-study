from typing import List

from fastapi import APIRouter, Depends, Path, HTTPException, status

from geek_conceitos_fastapi.database import fake_db, cursos
from geek_conceitos_fastapi.models import Curso, CursoBD

router = APIRouter()


@router.get("/api/v1")
async def root(db=Depends(fake_db)):
    return {"message": "Hello World"}


@router.get(
    path="/api/v1/cursos",
    response_model=List[Curso],
    description="Retorna todos os cursos ou uma lista vazia.",
    summary="Retorna todos os cursos",
)
async def get_cursos(db=Depends(fake_db)):
    return cursos


@router.get(path="/api/v1/cursos/{curso_id}")
async def get_curso(
    curso_id: int = Path(title="ID do curso", description="Deve se inteiro"),
    db=Depends(fake_db),
):
    curso = [curso for curso in cursos if curso.id == curso_id]
    if not curso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado."
        )

    return curso


@router.post(
    path="/api/v1/cursos", status_code=status.HTTP_201_CREATED, response_model=CursoBD
)
async def create_curso(curso: CursoBD, db=Depends(fake_db)):
    id = len(cursos) + 1
    cursos.append(Curso(id=id, **curso.model_dump()))

    return curso


@router.put(path="/api/v1/cursos/{curso_id}")
async def update_curso(curso_id: int, curso: CursoBD, db=Depends(fake_db)):
    curso_found = [curso for curso in cursos if curso.id == curso_id]
    if not curso_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado."
        )

    cursos[curso_id - 1] = curso
    return curso


@router.delete(path="/api/v1/cursos/{curso_id}")
async def delete_curso(curso_id: int, db=Depends(fake_db)):
    curso = [curso for curso in cursos if curso.id == curso_id]
    if not curso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado."
        )
    else:
        del cursos[curso_id - 1]
        return f"curso de id {curso_id} deletado."
