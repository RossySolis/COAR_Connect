from pydantic import BaseModel

class Padre(BaseModel):
    id: int
    usuario_id: int
    parentesco: str
    codigo_vinculacion: str

class PadreActualizar(BaseModel):
    usuario_id: int
    parentesco: str
    codigo_vinculacion: str