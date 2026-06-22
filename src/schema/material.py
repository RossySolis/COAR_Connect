from pydantic import BaseModel

class Material(BaseModel):
    id: int
    curso_id: int
    titulo: str
    descripcion: str
    tipo: str
    archivo_url: str
    fecha_subida: str

class MaterialActualizar(BaseModel):
    curso_id: int
    titulo: str
    descripcion: str
    tipo: str
    archivo_url: str
    fecha_subida: str