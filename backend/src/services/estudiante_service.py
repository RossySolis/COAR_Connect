from src.repository.estudiante_repository import EstudianteRepository
from src.schema.estudiante import Estudiante, EstudianteActualizar

class EstudianteService:
    def __init__(self):
        self.estudianteRepository = EstudianteRepository()

    async def mostrarEstudiantes(self):
        return await self.estudianteRepository.mostrarEstudiantes()

    async def agregarEstudiante(self, estudiante: Estudiante):
        return await self.estudianteRepository.agregarEstudiante(estudiante)

    async def actualizarEstudiante(self, id: int, estudiante: EstudianteActualizar):
        return await self.estudianteRepository.actualizarEstudiante(id, estudiante)

    async def eliminarEstudiante(self, id: int):
        return await self.estudianteRepository.eliminarEstudiante(id)