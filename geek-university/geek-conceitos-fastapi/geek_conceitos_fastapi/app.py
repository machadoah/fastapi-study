from time import sleep

from fastapi import FastAPI, Query, Header
from geek_conceitos_fastapi.routes import curso_router, user_router

app = FastAPI(
    title="API de Cursos",
    version="0.1.0",
    description="Uma API para estudo do **FastAPI**",
)
app.include_router(curso_router.router, tags=["cursos"])
app.include_router(user_router.router, tags=["users"])


@app.get("/calc")
async def calc(
    a: int = Query(default=0),
    b: int = Query(default=0),
    c: int = Query(default=0),
    x_header: str = Header(default=None),
):
    print(f"X-HEADER = {x_header}")
    return {"result": a + b + c}
