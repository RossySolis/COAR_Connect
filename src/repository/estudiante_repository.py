from src.schema.estudiante import Estudiante, EstudianteActualizar

class EstudianteRepository:
    estudiantes: list[Estudiante] = []

    async def mostrarEstudiantes(self):
        return self.estudiantes

    async def agregarEstudiante(self, estudiante: Estudiante):
        for e in self.estudiantes:
            if e.id == estudiante.id:
                return {"mensaje": "Ya existe un estudiante con ese ID"}
            if e.usuario_id == estudiante.usuario_id:
                return {"mensaje": "Este usuario ya está registrado como estudiante"}

        self.estudiantes.append(estudiante)
        return estudiante

    async def actualizarEstudiante(self, id: int, estudiante: EstudianteActualizar):
        for e in self.estudiantes:
            if e.id == id:
                e.usuario_id = estudiante.usuario_id
                e.grado = estudiante.grado
                e.colegio = estudiante.colegio
                e.distrito = estudiante.distrito
                return e
        return {"mensaje": "Estudiante no encontrado"}

    async def eliminarEstudiante(self, id: int):
        for indice, e in enumerate(self.estudiantes):
            if e.id == id:
                self.estudiantes.pop(indice)
                return {"mensaje": "Estudiante eliminado correctamente"}
        return {"mensaje": "Estudiante no encontrado"}