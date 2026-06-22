from pydantic import BaseModel

class Docente(BaseModel):
    id: int
    usuario_id: int
    especialidad: str
    experiencia: str

class DocenteActualizar(BaseModel):
    usuario_id: int
    especialidad: str
    experiencia: str