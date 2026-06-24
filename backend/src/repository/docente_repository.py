from src.schema.docente import Docente, DocenteActualizar
from src.database import get_connection


class DocenteRepository:

    async def mostrarDocentes(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, usuario_id, especialidad, experiencia
            FROM docentes
        """)

        docentes = []
        for row in cursor.fetchall():
            docentes.append({
                "id": row.id,
                "usuario_id": row.usuario_id,
                "especialidad": row.especialidad,
                "experiencia": row.experiencia
            })

        conn.close()
        return docentes

    async def agregarDocente(self, docente: Docente):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO docentes (usuario_id, especialidad, experiencia)
            VALUES (?, ?, ?)
        """, (
            docente.usuario_id,
            docente.especialidad,
            docente.experiencia
        ))

        conn.commit()
        conn.close()

        return {"mensaje": "Docente agregado correctamente"}

    async def actualizarDocente(self, id: int, docente: DocenteActualizar):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE docentes
            SET usuario_id = ?, especialidad = ?, experiencia = ?
            WHERE id = ?
        """, (
            docente.usuario_id,
            docente.especialidad,
            docente.experiencia,
            id
        ))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Docente no encontrado"}

        return {"mensaje": "Docente actualizado correctamente"}

    async def eliminarDocente(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM docentes
            WHERE id = ?
        """, (id,))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Docente no encontrado"}

        return {"mensaje": "Docente eliminado correctamente"}