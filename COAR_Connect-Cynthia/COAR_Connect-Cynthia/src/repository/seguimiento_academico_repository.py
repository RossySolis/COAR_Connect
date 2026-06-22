from src.schema.seguimiento_academico import SeguimientoAcademico, SeguimientoAcademicoActualizar
from src.database import get_connection


class SeguimientoAcademicoRepository:

    async def mostrarSeguimientos(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id,
                   estudiante_id,
                   curso_id,
                   avance_porcentaje,
                   horas_estudio,
                   asistencia_porcentaje,
                   recomendacion,
                   fecha_registro
            FROM seguimiento_academico
        """)

        seguimientos = []
        for row in cursor.fetchall():
            seguimientos.append({
                "id": row.id,
                "estudiante_id": row.estudiante_id,
                "curso_id": row.curso_id,
                "avance_porcentaje": float(row.avance_porcentaje),
                "horas_estudio": row.horas_estudio,
                "asistencia_porcentaje": float(row.asistencia_porcentaje),
                "recomendacion": row.recomendacion,
                "fecha_registro": row.fecha_registro
            })

        conn.close()
        return seguimientos

    async def agregarSeguimiento(self, seguimiento: SeguimientoAcademico):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO seguimiento_academico
            (estudiante_id, curso_id, avance_porcentaje,
             horas_estudio, asistencia_porcentaje,
             recomendacion, fecha_registro)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            seguimiento.estudiante_id,
            seguimiento.curso_id,
            seguimiento.avance_porcentaje,
            seguimiento.horas_estudio,
            seguimiento.asistencia_porcentaje,
            seguimiento.recomendacion,
            seguimiento.fecha_registro
        ))

        conn.commit()
        conn.close()

        return {"mensaje": "Seguimiento agregado correctamente"}

    async def actualizarSeguimiento(self, id: int, seguimiento: SeguimientoAcademicoActualizar):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE seguimiento_academico
            SET estudiante_id = ?,
                curso_id = ?,
                avance_porcentaje = ?,
                horas_estudio = ?,
                asistencia_porcentaje = ?,
                recomendacion = ?,
                fecha_registro = ?
            WHERE id = ?
        """, (
            seguimiento.estudiante_id,
            seguimiento.curso_id,
            seguimiento.avance_porcentaje,
            seguimiento.horas_estudio,
            seguimiento.asistencia_porcentaje,
            seguimiento.recomendacion,
            seguimiento.fecha_registro,
            id
        ))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Seguimiento académico no encontrado"}

        return {"mensaje": "Seguimiento académico actualizado correctamente"}

    async def eliminarSeguimiento(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM seguimiento_academico
            WHERE id = ?
        """, (id,))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Seguimiento académico no encontrado"}

        return {"mensaje": "Seguimiento académico eliminado correctamente"}