from pydantic import BaseModel

class Rol(BaseModel):
    id: int
    nombre: str
    descripcion: str

class RolActualizar(BaseModel):
    nombre: str
    descripcion: str