from pydantic import BaseModel

class Horario(BaseModel):
    id: int
    curso_id: int
    dia: str
    hora_inicio: str
    hora_fin: str
    modalidad: str
    cupos: int
    estado: str

class HorarioActualizar(BaseModel):
    curso_id: int
    dia: str
    hora_inicio: str
    hora_fin: str
    modalidad: str
    cupos: int
    estado: str