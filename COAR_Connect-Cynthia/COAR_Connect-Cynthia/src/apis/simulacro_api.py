from fastapi import APIRouter
from src.services.simulacro_service import SimulacroService
from src.schema.simulacro import Simulacro, SimulacroActualizar

routerSimulacro = APIRouter(prefix="/simulacro", tags=["Simulacro"])

simulacroService = SimulacroService()

@routerSimulacro.get("/")
async def obtenerSimulacros():
    return await simulacroService.mostrarSimulacros()

@routerSimulacro.post("/agregar")
async def agregarSimulacro(simulacro: Simulacro):
    return await simulacroService.agregarSimulacro(simulacro)

@routerSimulacro.put("/{id_simulacro}")
async def actualizarSimulacro(id_simulacro: int, simulacro: SimulacroActualizar):
    return await simulacroService.actualizarSimulacro(id_simulacro, simulacro)

@routerSimulacro.delete("/{id_simulacro}")
async def eliminarSimulacro(id_simulacro: int):
    return await simulacroService.eliminarSimulacro(id_simulacro)