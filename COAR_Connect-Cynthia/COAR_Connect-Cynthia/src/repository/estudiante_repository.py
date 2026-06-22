from src.schema.estudiante import Estudiante, EstudianteActualizar
from src.database import get_connection


class EstudianteRepository:

    async def mostrarEstudiantes(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, usuario_id, grado, colegio, distrito
            FROM estudiantes
        """)

        estudiantes = []
        for row in cursor.fetchall():
            estudiantes.append({
                "id": row.id,
                "usuario_id": row.usuario_id,
                "grado": row.grado,
                "colegio": row.colegio,
                "distrito": row.distrito
            })

        conn.close()
        return estudiantes

    async def agregarEstudiante(self, estudiante: Estudiante):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO estudiantes (usuario_id, grado, colegio, distrito)
            VALUES (?, ?, ?, ?)
        """, (
            estudiante.usuario_id,
            estudiante.grado,
            estudiante.colegio,
            estudiante.distrito
        ))

        conn.commit()
        conn.close()

        return {"mensaje": "Estudiante agregado correctamente"}

    async def actualizarEstudiante(self, id: int, estudiante: EstudianteActualizar):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE estudiantes
            SET usuario_id = ?, grado = ?, colegio = ?, distrito = ?
            WHERE id = ?
        """, (
            estudiante.usuario_id,
            estudiante.grado,
            estudiante.colegio,
            estudiante.distrito,
            id
        ))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Estudiante no encontrado"}

        return {"mensaje": "Estudiante actualizado correctamente"}

    async def eliminarEstudiante(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM estudiantes
            WHERE id = ?
        """, (id,))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Estudiante no encontrado"}

        return {"mensaje": "Estudiante eliminado correctamente"}