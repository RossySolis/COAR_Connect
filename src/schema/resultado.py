from pydantic import BaseModel

class Resultado(BaseModel):
    id: int
    estudiante_id: int
    simulacro_id: int
    puntaje: float
    fecha_realizacion: str
    observacion: str

class ResultadoActualizar(BaseModel):
    estudiante_id: int
    simulacro_id: int
    puntaje: float
    fecha_realizacion: str
    observacion: str