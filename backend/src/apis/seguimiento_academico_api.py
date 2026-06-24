from fastapi import APIRouter
from src.services.seguimiento_academico_service import SeguimientoAcademicoService
from src.schema.seguimiento_academico import SeguimientoAcademico, SeguimientoAcademicoActualizar

routerSeguimientoAcademico = APIRouter(
    prefix="/seguimiento-academico",
    tags=["Seguimiento Academico"]
)

seguimientoService = SeguimientoAcademicoService()

@routerSeguimientoAcademico.get("/")
async def obtenerSeguimientos():
    return await seguimientoService.mostrarSeguimientos()

@routerSeguimientoAcademico.post("/agregar")
async def agregarSeguimiento(seguimiento: SeguimientoAcademico):
    return await seguimientoService.agregarSeguimiento(seguimiento)

@routerSeguimientoAcademico.put("/{id_seguimiento}")
async def actualizarSeguimiento(id_seguimiento: int, seguimiento: SeguimientoAcademicoActualizar):
    return await seguimientoService.actualizarSeguimiento(id_seguimiento, seguimiento)

@routerSeguimientoAcademico.delete("/{id_seguimiento}")
async def eliminarSeguimiento(id_seguimiento: int):
    return await seguimientoService.eliminarSeguimiento(id_seguimiento)