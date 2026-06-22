from src.repository.padre_repository import PadreRepository
from src.schema.padre import Padre, PadreActualizar

class PadreService:
    def __init__(self):
        self.padreRepository = PadreRepository()

    async def mostrarPadres(self):
        return await self.padreRepository.mostrarPadres()

    async def agregarPadre(self, padre: Padre):
        return await self.padreRepository.agregarPadre(padre)

    async def actualizarPadre(self, id: int, padre: PadreActualizar):
        return await self.padreRepository.actualizarPadre(id, padre)

    async def eliminarPadre(self, id: int):
        return await self.padreRepository.eliminarPadre(id)