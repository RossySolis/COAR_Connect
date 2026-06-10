from src.repository.horario_repository import HorarioRepository
from src.schema.horario import Horario, HorarioActualizar

class HorarioService:

    def __init__(self):
        self.horarioRepository = HorarioRepository()

    async def mostrarHorarios(self):
        return await self.horarioRepository.mostrarHorarios()

    async def agregarHorario(self, horario: Horario):
        return await self.horarioRepository.agregarHorario(horario)

    async def actualizarHorario(self, id: int, horario: HorarioActualizar):
        return await self.horarioRepository.actualizarHorario(id, horario)

    async def eliminarHorario(self, id: int):
        return await self.horarioRepository.eliminarHorario(id)