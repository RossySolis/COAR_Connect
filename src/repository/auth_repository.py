from src.schema.auth import Login
from src.repository.usuario_repository import UsuarioRepository

class AuthRepository:

    def __init__(self):
        self.usuarioRepository = UsuarioRepository()

    async def login(self, login: Login):
        usuarios = await self.usuarioRepository.mostrarUsuarios()

        for usuario in usuarios:
            if usuario.correo == login.correo and usuario.password == login.password:
                return {
                    "mensaje": "Inicio de sesión exitoso",
                    "usuario": usuario
                }

        return {"mensaje": "Correo o contraseña incorrectos"}