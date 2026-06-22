from fastapi import APIRouter
from src.services.docente_service import DocenteService
from src.schema.docente import Docente, DocenteActualizar

routerDocente = APIRouter(prefix="/docente", tags=["Docente"])

docenteService = DocenteService()

@routerDocente.get("/")
async def obtenerDocentes():
    return await docenteService.mostrarDocentes()

@routerDocente.post("/agregar")
async def agregarDocente(docente: Docente):
    return await docenteService.agregarDocente(docente)

@routerDocente.put("/{id_docente}")
async def actualizarDocente(id_docente: int, docente: DocenteActualizar):
    return await docenteService.actualizarDocente(id_docente, docente)

@routerDocente.delete("/{id_docente}")
async def eliminarDocente(id_docente: int):
    return await docenteService.eliminarDocente(id_docente)