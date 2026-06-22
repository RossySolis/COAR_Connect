from src.repository.inscripcion_repository import InscripcionRepository
from src.schema.inscripcion import Inscripcion, InscripcionActualizar

class InscripcionService:

    def __init__(self):
        self.inscripcionRepository = InscripcionRepository()

    async def mostrarInscripciones(self):
        return await self.inscripcionRepository.mostrarInscripciones()

    async def agregarInscripcion(self, inscripcion: Inscripcion):
        return await self.inscripcionRepository.agregarInscripcion(inscripcion)

    async def actualizarInscripcion(self, id: int, inscripcion: InscripcionActualizar):
        return await self.inscripcionRepository.actualizarInscripcion(id, inscripcion)

    async def eliminarInscripcion(self, id: int):
        return await self.inscripcionRepository.eliminarInscripcion(id)