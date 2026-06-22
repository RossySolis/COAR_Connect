from src.schema.seguimiento_academico import SeguimientoAcademico, SeguimientoAcademicoActualizar

class SeguimientoAcademicoRepository:
    seguimientos: list[SeguimientoAcademico] = []

    async def mostrarSeguimientos(self):
        return self.seguimientos

    async def agregarSeguimiento(self, seguimiento: SeguimientoAcademico):
        for s in self.seguimientos:
            if s.id == seguimiento.id:
                return {"mensaje": "Ya existe un seguimiento académico con ese ID"}
            if s.estudiante_id == seguimiento.estudiante_id and s.curso_id == seguimiento.curso_id:
                return {"mensaje": "Ya existe seguimiento académico para este estudiante y curso"}

        self.seguimientos.append(seguimiento)
        return seguimiento

    async def actualizarSeguimiento(self, id: int, seguimiento: SeguimientoAcademicoActualizar):
        for s in self.seguimientos:
            if s.id == id:
                s.estudiante_id = seguimiento.estudiante_id
                s.curso_id = seguimiento.curso_id
                s.avance_porcentaje = seguimiento.avance_porcentaje
                s.horas_estudio = seguimiento.horas_estudio
                s.asistencia_porcentaje = seguimiento.asistencia_porcentaje
                s.recomendacion = seguimiento.recomendacion
                s.fecha_registro = seguimiento.fecha_registro
                return s
        return {"mensaje": "Seguimiento académico no encontrado"}

    async def eliminarSeguimiento(self, id: int):
        for indice, s in enumerate(self.seguimientos):
            if s.id == id:
                self.seguimientos.pop(indice)
                return {"mensaje": "Seguimiento académico eliminado correctamente"}
        return {"mensaje": "Seguimiento académico no encontrado"}