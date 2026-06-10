from pydantic import BaseModel

class SeguimientoAcademico(BaseModel):
    id: int
    estudiante_id: int
    curso_id: int
    avance_porcentaje: float
    horas_estudio: int
    asistencia_porcentaje: float
    recomendacion: str
    fecha_registro: str

class SeguimientoAcademicoActualizar(BaseModel):
    estudiante_id: int
    curso_id: int
    avance_porcentaje: float
    horas_estudio: int
    asistencia_porcentaje: float
    recomendacion: str
    fecha_registro: str