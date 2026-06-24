from fastapi import APIRouter
from src.services.resultado_service import ResultadoService
from src.schema.resultado import Resultado, ResultadoActualizar

routerResultado = APIRouter(prefix="/resultado", tags=["Resultado"])

resultadoService = ResultadoService()

@routerResultado.get("/")
async def obtenerResultados():
    return await resultadoService.mostrarResultados()

@routerResultado.post("/agregar")
async def agregarResultado(resultado: Resultado):
    return await resultadoService.agregarResultado(resultado)

@routerResultado.put("/{id_resultado}")
async def actualizarResultado(id_resultado: int, resultado: ResultadoActualizar):
    return await resultadoService.actualizarResultado(id_resultado, resultado)

@routerResultado.delete("/{id_resultado}")
async def eliminarResultado(id_resultado: int):
    return await resultadoService.eliminarResultado(id_resultado)