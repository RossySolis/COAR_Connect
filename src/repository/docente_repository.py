from src.schema.docente import Docente, DocenteActualizar

class DocenteRepository:
    docentes: list[Docente] = []

    async def mostrarDocentes(self):
        return self.docentes

    async def agregarDocente(self, docente: Docente):
        for d in self.docentes:
            if d.id == docente.id:
                return {"mensaje": "Ya existe un docente con ese ID"}
            if d.usuario_id == docente.usuario_id:
                return {"mensaje": "Este usuario ya está registrado como docente"}

        self.docentes.append(docente)
        return docente

    async def actualizarDocente(self, id: int, docente: DocenteActualizar):
        for d in self.docentes:
            if d.id == id:
                d.usuario_id = docente.usuario_id
                d.especialidad = docente.especialidad
                d.experiencia = docente.experiencia
                return d
        return {"mensaje": "Docente no encontrado"}

    async def eliminarDocente(self, id: int):
        for indice, d in enumerate(self.docentes):
            if d.id == id:
                self.docentes.pop(indice)
                return {"mensaje": "Docente eliminado correctamente"}
        return {"mensaje": "Docente no encontrado"}