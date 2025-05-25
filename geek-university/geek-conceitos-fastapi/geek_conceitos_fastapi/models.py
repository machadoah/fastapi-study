from pydantic import BaseModel, field_validator
from typing import Optional


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @field_validator('titulo')
    def titulo_validator(cls, value):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('Titulo deve ter mais do que 2 palavras!')


class CursoBD(BaseModel):
    titulo: str
    aulas: int
    horas: int
