from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    nombre: str
    apellido: str
    correo: str
    password: str
    rol_id: int
    telefono: str
    estado: str

class UsuarioActualizar(BaseModel):
    nombre: str
    apellido: str
    correo: str
    rol_id: int
    telefono: str
    estado: str