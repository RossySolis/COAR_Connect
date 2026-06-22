from src.schema.inscripcion import Inscripcion, InscripcionActualizar

class InscripcionRepository:

    def __init__(self):
        self.inscripciones: list[Inscripcion] = []

    async def mostrarInscripciones(self):
        return self.inscripciones

    async def agregarInscripcion(self, inscripcion: Inscripcion):
        for i in self.inscripciones:
            if i.id == inscripcion.id:
                return {"mensaje": "Ya existe una inscripción con ese ID"}
            if i.estudiante_id == inscripcion.estudiante_id and i.horario_id == inscripcion.horario_id:
                return {"mensaje": "El estudiante ya está inscrito en este horario"}

        self.inscripciones.append(inscripcion)
        return inscripcion

    async def actualizarInscripcion(self, id: int, inscripcion: InscripcionActualizar):
        for i in self.inscripciones:
            if i.id == id:
                i.estudiante_id = inscripcion.estudiante_id
                i.horario_id = inscripcion.horario_id
                i.fecha_inscripcion = inscripcion.fecha_inscripcion
                i.estado = inscripcion.estado
                return i
        return {"mensaje": "Inscripción no encontrada"}

    async def eliminarInscripcion(self, id: int):
        for indice, i in enumerate(self.inscripciones):
            if i.id == id:
                self.inscripciones.pop(indice)
                return {"mensaje": "Inscripción eliminada correctamente"}
        return {"mensaje": "Inscripción no encontrada"}