from src.repository.usuario_repository import UsuarioRepository
from src.schema.usuario import Usuario, UsuarioActualizar

class UsuarioService:

    def __init__(self):
        self.usuarioRepository = UsuarioRepository()

    async def mostrarUsuarios(self):
        return await self.usuarioRepository.mostrarUsuarios()

    async def agregarUsuario(self, usuario: Usuario):
        return await self.usuarioRepository.agregarUsuario(usuario)

    async def actualizarUsuario(self, id: int, usuario: UsuarioActualizar):
        return await self.usuarioRepository.actualizarUsuario(id, usuario)

    async def eliminarUsuario(self, id: int):
        return await self.usuarioRepository.eliminarUsuario(id)