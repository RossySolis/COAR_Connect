from src.schema.horario import Horario, HorarioActualizar
from src.database import get_connection


class HorarioRepository:

    async def mostrarHorarios(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, curso_id, dia, hora_inicio, hora_fin,
                   modalidad, cupos, estado
            FROM horarios
        """)

        horarios = []
        for row in cursor.fetchall():
            horarios.append({
                "id": row.id,
                "curso_id": row.curso_id,
                "dia": row.dia,
                "hora_inicio": row.hora_inicio,
                "hora_fin": row.hora_fin,
                "modalidad": row.modalidad,
                "cupos": row.cupos,
                "estado": row.estado
            })

        conn.close()
        return horarios

    async def agregarHorario(self, horario: Horario):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO horarios
            (curso_id, dia, hora_inicio, hora_fin,
             modalidad, cupos, estado)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            horario.curso_id,
            horario.dia,
            horario.hora_inicio,
            horario.hora_fin,
            horario.modalidad,
            horario.cupos,
            horario.estado
        ))

        conn.commit()
        conn.close()

        return {"mensaje": "Horario agregado correctamente"}

    async def actualizarHorario(self, id: int, horario: HorarioActualizar):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE horarios
            SET curso_id = ?,
                dia = ?,
                hora_inicio = ?,
                hora_fin = ?,
                modalidad = ?,
                cupos = ?,
                estado = ?
            WHERE id = ?
        """, (
            horario.curso_id,
            horario.dia,
            horario.hora_inicio,
            horario.hora_fin,
            horario.modalidad,
            horario.cupos,
            horario.estado,
            id
        ))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Horario no encontrado"}

        return {"mensaje": "Horario actualizado correctamente"}

    async def eliminarHorario(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM horarios
            WHERE id = ?
        """, (id,))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Horario no encontrado"}

        return {"mensaje": "Horario eliminado correctamente"}