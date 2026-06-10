from src.schema.curso import Curso, CursoActualizar

class CursoRepository:

    def __init__(self):
        self.cursos: list[Curso] = []

    async def mostrarCursos(self):
        return self.cursos

    async def agregarCurso(self, curso: Curso):
        for c in self.cursos:
            if c.id == curso.id:
                return {"mensaje": "Ya existe un curso con ese ID"}

        self.cursos.append(curso)
        return curso

    async def actualizarCurso(self, id: int, curso: CursoActualizar):
        for c in self.cursos:
            if c.id == id:
                c.nombre = curso.nombre
                c.descripcion = curso.descripcion
                c.area = curso.area
                c.nivel = curso.nivel
                c.docente_id = curso.docente_id
                c.estado = curso.estado
                return c
        return {"mensaje": "Curso no encontrado"}

    async def eliminarCurso(self, id: int):
        for indice, c in enumerate(self.cursos):
            if c.id == id:
                self.cursos.pop(indice)
                return {"mensaje": "Curso eliminado correctamente"}
        return {"mensaje": "Curso no encontrado"}