from fastapi import APIRouter
from src.services.horario_service import HorarioService
from src.schema.horario import Horario, HorarioActualizar

routerHorario = APIRouter(prefix="/horario", tags=["Horario"])

horarioService = HorarioService()

@routerHorario.get("/")
async def obtenerHorarios():
    return await horarioService.mostrarHorarios()

@routerHorario.post("/agregar")
async def agregarHorario(horario: Horario):
    return await horarioService.agregarHorario(horario)

@routerHorario.put("/{id_horario}")
async def actualizarHorario(id_horario: int, horario: HorarioActualizar):
    return await horarioService.actualizarHorario(id_horario, horario)

@routerHorario.delete("/{id_horario}")
async def eliminarHorario(id_horario: int):
    return await horarioService.eliminarHorario(id_horario)