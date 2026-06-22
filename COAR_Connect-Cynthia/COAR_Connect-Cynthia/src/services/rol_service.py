from src.repository.rol_repository import RolRepository
from src.schema.rol import Rol, RolActualizar

class RolService:
    def __init__(self):
        self.rolRepository = RolRepository()

    async def mostrarRoles(self):
        return await self.rolRepository.mostrarRoles()

    async def agregarRol(self, rol: Rol):
        return await self.rolRepository.agregarRol(rol)

    async def actualizarRol(self, id: int, rol: RolActualizar):
        return await self.rolRepository.actualizarRol(id, rol)

    async def eliminarRol(self, id: int):
        return await self.rolRepository.eliminarRol(id)