from fastapi import APIRouter
from src.services.curso_service import CursoService
from src.schema.curso import Curso, CursoActualizar

routerCurso = APIRouter(prefix="/curso", tags=["Curso"])

cursoService = CursoService()

@routerCurso.get("/")
async def obtenerCursos():
    return await cursoService.mostrarCursos()

@routerCurso.post("/agregar")
async def agregarCurso(curso: Curso):
    return await cursoService.agregarCurso(curso)

@routerCurso.put("/{id_curso}")
async def actualizarCurso(id_curso: int, curso: CursoActualizar):
    return await cursoService.actualizarCurso(id_curso, curso)

@routerCurso.delete("/{id_curso}")
async def eliminarCurso(id_curso: int):
    return await cursoService.eliminarCurso(id_curso)