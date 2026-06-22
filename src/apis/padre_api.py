from fastapi import APIRouter
from src.services.padre_service import PadreService
from src.schema.padre import Padre, PadreActualizar

routerPadre = APIRouter(prefix="/padre", tags=["Padre"])

padreService = PadreService()

@routerPadre.get("/")
async def obtenerPadres():
    return await padreService.mostrarPadres()

@routerPadre.post("/agregar")
async def agregarPadre(padre: Padre):
    return await padreService.agregarPadre(padre)

@routerPadre.put("/{id_padre}")
async def actualizarPadre(id_padre: int, padre: PadreActualizar):
    return await padreService.actualizarPadre(id_padre, padre)

@routerPadre.delete("/{id_padre}")
async def eliminarPadre(id_padre: int):
    return await padreService.eliminarPadre(id_padre)