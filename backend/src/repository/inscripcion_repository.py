from src.schema.inscripcion import Inscripcion, InscripcionActualizar
from src.database import get_connection


class InscripcionRepository:

    async def mostrarInscripciones(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id,
                   estudiante_id,
                   horario_id,
                   fecha_inscripcion,
                   estado
            FROM inscripciones
        """)

        inscripciones = []
        for row in cursor.fetchall():
            inscripciones.append({
                "id": row.id,
                "estudiante_id": row.estudiante_id,
                "horario_id": row.horario_id,
                "fecha_inscripcion": row.fecha_inscripcion,
                "estado": row.estado
            })

        conn.close()
        return inscripciones

    async def agregarInscripcion(self, inscripcion: Inscripcion):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO inscripciones
            (estudiante_id, horario_id, fecha_inscripcion, estado)
            VALUES (?, ?, ?, ?)
        """, (
            inscripcion.estudiante_id,
            inscripcion.horario_id,
            inscripcion.fecha_inscripcion,
            inscripcion.estado
        ))

        conn.commit()
        conn.close()

        return {"mensaje": "Inscripción agregada correctamente"}

    async def actualizarInscripcion(self, id: int, inscripcion: InscripcionActualizar):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE inscripciones
            SET estudiante_id = ?,
                horario_id = ?,
                fecha_inscripcion = ?,
                estado = ?
            WHERE id = ?
        """, (
            inscripcion.estudiante_id,
            inscripcion.horario_id,
            inscripcion.fecha_inscripcion,
            inscripcion.estado,
            id
        ))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Inscripción no encontrada"}

        return {"mensaje": "Inscripción actualizada correctamente"}

    async def eliminarInscripcion(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM inscripciones
            WHERE id = ?
        """, (id,))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Inscripción no encontrada"}

        return {"mensaje": "Inscripción eliminada correctamente"}