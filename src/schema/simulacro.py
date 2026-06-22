from pydantic import BaseModel

class Simulacro(BaseModel):
    id: int
    curso_id: int
    titulo: str
    descripcion: str
    fecha_publicacion: str
    tiempo_minutos: int
    estado: str

class SimulacroActualizar(BaseModel):
    curso_id: int
    titulo: str
    descripcion: str
    fecha_publicacion: str
    tiempo_minutos: int
    estado: str