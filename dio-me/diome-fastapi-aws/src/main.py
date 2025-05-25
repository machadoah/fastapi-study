from fastapi import FastAPI
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import BaseModel
import os


class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    msg: str
    done: Optional[bool] = Field(default=False)


api = FastAPI()

engine = create_engine(
    # "postgresql://user:password@host:port/database"
    "postgresql://postgres:postgres@{database_host}:5432/postgres".format(
        database_host=os.getenv("DATABASE_HOST"))
)


@api.on_event("startup")
def run_migrations():
    SQLModel.metadata.create_all(engine)


@api.get("/")
def list() -> list[Task]:
    with Session(engine) as session:
        return session.exec(select(Task)).all()


@api.post("/")
def create(task: Task) -> Task:
    with Session(engine) as session:
        session.add(task)
        session.commit()
        session.refresh(task)
        return task


class TaskUpdatePayload(BaseModel):
    done: bool
    msg: str


@api.patch("/{task_id}")
def update(task_id: int, body: TaskUpdatePayload) -> Task:
    with Session(engine) as session:
        task = session.exec(select(Task).where(Task.id == task_id)).one()

        task.done = body.done
        task.msg = body.msg
        session.add(task)
        session.commit()
        session.refresh(task)
        return task
