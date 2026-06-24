from pydantic import BaseModel

class Curso(BaseModel):
    id: int
    nombre: str
    descripcion: str
    area: str
    nivel: str
    docente_id: int
    estado: str

class CursoActualizar(BaseModel):
    nombre: str
    descripcion: str
    area: str
    nivel: str
    docente_id: int
    estado: str