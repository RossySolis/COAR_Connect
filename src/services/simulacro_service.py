from src.repository.simulacro_repository import SimulacroRepository
from src.schema.simulacro import Simulacro, SimulacroActualizar

class SimulacroService:
    def __init__(self):
        self.simulacroRepository = SimulacroRepository()

    async def mostrarSimulacros(self):
        return await self.simulacroRepository.mostrarSimulacros()

    async def agregarSimulacro(self, simulacro: Simulacro):
        return await self.simulacroRepository.agregarSimulacro(simulacro)

    async def actualizarSimulacro(self, id: int, simulacro: SimulacroActualizar):
        return await self.simulacroRepository.actualizarSimulacro(id, simulacro)

    async def eliminarSimulacro(self, id: int):
        return await self.simulacroRepository.eliminarSimulacro(id)