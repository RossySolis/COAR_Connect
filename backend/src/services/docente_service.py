from src.repository.docente_repository import DocenteRepository
from src.schema.docente import Docente, DocenteActualizar

class DocenteService:
    def __init__(self):
        self.docenteRepository = DocenteRepository()

    async def mostrarDocentes(self):
        return await self.docenteRepository.mostrarDocentes()

    async def agregarDocente(self, docente: Docente):
        return await self.docenteRepository.agregarDocente(docente)

    async def actualizarDocente(self, id: int, docente: DocenteActualizar):
        return await self.docenteRepository.actualizarDocente(id, docente)

    async def eliminarDocente(self, id: int):
        return await self.docenteRepository.eliminarDocente(id)