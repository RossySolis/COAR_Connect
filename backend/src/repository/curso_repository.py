from src.schema.curso import Curso, CursoActualizar
from src.database import get_connection


class CursoRepository:

    async def mostrarCursos(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nombre, descripcion, area, nivel, docente_id, estado
            FROM cursos
        """)

        cursos = []
        for row in cursor.fetchall():
            cursos.append({
                "id": row.id,
                "nombre": row.nombre,
                "descripcion": row.descripcion,
                "area": row.area,
                "nivel": row.nivel,
                "docente_id": row.docente_id,
                "estado": row.estado
            })

        conn.close()
        return cursos

    async def agregarCurso(self, curso: Curso):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO cursos (nombre, descripcion, area, nivel, docente_id, estado)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            curso.nombre,
            curso.descripcion,
            curso.area,
            curso.nivel,
            curso.docente_id,
            curso.estado
        ))

        conn.commit()
        conn.close()

        return {"mensaje": "Curso agregado correctamente"}

    async def actualizarCurso(self, id: int, curso: CursoActualizar):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE cursos
            SET nombre = ?, descripcion = ?, area = ?, nivel = ?, docente_id = ?, estado = ?
            WHERE id = ?
        """, (
            curso.nombre,
            curso.descripcion,
            curso.area,
            curso.nivel,
            curso.docente_id,
            curso.estado,
            id
        ))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Curso no encontrado"}

        return {"mensaje": "Curso actualizado correctamente"}

    async def eliminarCurso(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM cursos WHERE id = ?", (id,))
        conn.commit()

        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Curso no encontrado"}

        return {"mensaje": "Curso eliminado correctamente"}