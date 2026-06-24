from pydantic import BaseModel

class Estudiante(BaseModel):
    id: int
    usuario_id: int
    padre_id: int
    grado: str
    colegio: str
    distrito: str

class EstudianteActualizar(BaseModel):
    usuario_id: int
    padre_id: int
    grado: str
    colegio: str
    distrito: str