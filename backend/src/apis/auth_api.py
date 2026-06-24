from fastapi import APIRouter
from src.services.auth_service import AuthService
from src.schema.auth import Login

routerAuth = APIRouter(prefix="/auth", tags=["Auth"])

authService = AuthService()

@routerAuth.post("/login")
async def login(login: Login):
    return await authService.login(login)