from src.schema.resultado import Resultado, ResultadoActualizar
from src.database import get_connection


class ResultadoRepository:

    async def mostrarResultados(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id,
                   estudiante_id,
                   simulacro_id,
                   puntaje,
                   fecha_realizacion,
                   observacion
            FROM resultados
        """)

        resultados = []
        for row in cursor.fetchall():
            resultados.append({
                "id": row.id,
                "estudiante_id": row.estudiante_id,
                "simulacro_id": row.simulacro_id,
                "puntaje": float(row.puntaje),
                "fecha_realizacion": row.fecha_realizacion,
                "observacion": row.observacion
            })

        conn.close()
        return resultados

    async def agregarResultado(self, resultado: Resultado):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO resultados
            (estudiante_id, simulacro_id, puntaje,
             fecha_realizacion, observacion)
            VALUES (?, ?, ?, ?, ?)
        """, (
            resultado.estudiante_id,
            resultado.simulacro_id,
            resultado.puntaje,
            resultado.fecha_realizacion,
            resultado.observacion
        ))

        conn.commit()
        conn.close()

        return {"mensaje": "Resultado agregado correctamente"}

    async def actualizarResultado(self, id: int, resultado: ResultadoActualizar):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE resultados
            SET estudiante_id = ?,
                simulacro_id = ?,
                puntaje = ?,
                fecha_realizacion = ?,
                observacion = ?
            WHERE id = ?
        """, (
            resultado.estudiante_id,
            resultado.simulacro_id,
            resultado.puntaje,
            resultado.fecha_realizacion,
            resultado.observacion,
            id
        ))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Resultado no encontrado"}

        return {"mensaje": "Resultado actualizado correctamente"}

    async def eliminarResultado(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM resultados
            WHERE id = ?
        """, (id,))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Resultado no encontrado"}

        return {"mensaje": "Resultado eliminado correctamente"}