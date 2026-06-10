from src.repository.auth_repository import AuthRepository
from src.schema.auth import Login

class AuthService:
    def __init__(self):
        self.authRepository = AuthRepository()

    async def login(self, login: Login):
        return await self.authRepository.login(login)