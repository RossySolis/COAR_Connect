from pydantic import BaseModel

class Padre(BaseModel):
    id: int
    usuario_id: int
    estudiante_id: int
    parentesco: str

class PadreActualizar(BaseModel):
    usuario_id: int
    estudiante_id: int
    parentesco: str