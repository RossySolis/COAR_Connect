from src.repository.curso_repository import CursoRepository
from src.schema.curso import Curso, CursoActualizar

class CursoService:

    def __init__(self):
        self.cursoRepository = CursoRepository()

    async def mostrarCursos(self):
        return await self.cursoRepository.mostrarCursos()

    async def agregarCurso(self, curso: Curso):
        return await self.cursoRepository.agregarCurso(curso)

    async def actualizarCurso(self, id: int, curso: CursoActualizar):
        return await self.cursoRepository.actualizarCurso(id, curso)

    async def eliminarCurso(self, id: int):
        return await self.cursoRepository.eliminarCurso(id)