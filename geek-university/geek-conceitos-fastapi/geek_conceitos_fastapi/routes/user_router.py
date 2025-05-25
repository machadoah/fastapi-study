from fastapi import APIRouter

router = APIRouter()


@router.get("/api/v1/usuarios")
async def get_all_users():
    return {"message": "todos os usuários"}
