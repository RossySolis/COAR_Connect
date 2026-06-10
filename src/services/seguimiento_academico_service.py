from src.repository.seguimiento_academico_repository import SeguimientoAcademicoRepository
from src.schema.seguimiento_academico import SeguimientoAcademico, SeguimientoAcademicoActualizar

class SeguimientoAcademicoService:
    def __init__(self):
        self.seguimientoRepository = SeguimientoAcademicoRepository()

    async def mostrarSeguimientos(self):
        return await self.seguimientoRepository.mostrarSeguimientos()

    async def agregarSeguimiento(self, seguimiento: SeguimientoAcademico):
        return await self.seguimientoRepository.agregarSeguimiento(seguimiento)

    async def actualizarSeguimiento(self, id: int, seguimiento: SeguimientoAcademicoActualizar):
        return await self.seguimientoRepository.actualizarSeguimiento(id, seguimiento)

    async def eliminarSeguimiento(self, id: int):
        return await self.seguimientoRepository.eliminarSeguimiento(id)