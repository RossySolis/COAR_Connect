from src.repository.resultado_repository import ResultadoRepository
from src.schema.resultado import Resultado, ResultadoActualizar

class ResultadoService:
    def __init__(self):
        self.resultadoRepository = ResultadoRepository()

    async def mostrarResultados(self):
        return await self.resultadoRepository.mostrarResultados()

    async def agregarResultado(self, resultado: Resultado):
        return await self.resultadoRepository.agregarResultado(resultado)

    async def actualizarResultado(self, id: int, resultado: ResultadoActualizar):
        return await self.resultadoRepository.actualizarResultado(id, resultado)

    async def eliminarResultado(self, id: int):
        return await self.resultadoRepository.eliminarResultado(id)