from fastapi import APIRouter
from src.services.inscripcion_service import InscripcionService
from src.schema.inscripcion import Inscripcion, InscripcionActualizar

routerInscripcion = APIRouter(prefix="/inscripcion", tags=["Inscripcion"])

inscripcionService = InscripcionService()

@routerInscripcion.get("/")
async def obtenerInscripciones():
    return await inscripcionService.mostrarInscripciones()

@routerInscripcion.post("/agregar")
async def agregarInscripcion(inscripcion: Inscripcion):
    return await inscripcionService.agregarInscripcion(inscripcion)

@routerInscripcion.put("/{id_inscripcion}")
async def actualizarInscripcion(id_inscripcion: int, inscripcion: InscripcionActualizar):
    return await inscripcionService.actualizarInscripcion(id_inscripcion, inscripcion)

@routerInscripcion.delete("/{id_inscripcion}")
async def eliminarInscripcion(id_inscripcion: int):
    return await inscripcionService.eliminarInscripcion(id_inscripcion)