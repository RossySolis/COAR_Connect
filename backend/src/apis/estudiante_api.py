from fastapi import APIRouter
from src.services.estudiante_service import EstudianteService
from src.schema.estudiante import Estudiante, EstudianteActualizar

routerEstudiante = APIRouter(prefix="/estudiante", tags=["Estudiante"])

estudianteService = EstudianteService()

@routerEstudiante.get("/")
async def obtenerEstudiantes():
    return await estudianteService.mostrarEstudiantes()

@routerEstudiante.post("/agregar")
async def agregarEstudiante(estudiante: Estudiante):
    return await estudianteService.agregarEstudiante(estudiante)

@routerEstudiante.put("/{id_estudiante}")
async def actualizarEstudiante(id_estudiante: int, estudiante: EstudianteActualizar):
    return await estudianteService.actualizarEstudiante(id_estudiante, estudiante)

@routerEstudiante.delete("/{id_estudiante}")
async def eliminarEstudiante(id_estudiante: int):
    return await estudianteService.eliminarEstudiante(id_estudiante)