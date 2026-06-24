from pydantic import BaseModel

class Inscripcion(BaseModel):
    id: int
    estudiante_id: int
    horario_id: int
    fecha_inscripcion: str
    estado: str

class InscripcionActualizar(BaseModel):
    estudiante_id: int
    horario_id: int
    fecha_inscripcion: str
    estado: str