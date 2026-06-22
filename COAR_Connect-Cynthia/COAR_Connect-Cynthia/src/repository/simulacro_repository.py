from src.schema.simulacro import Simulacro, SimulacroActualizar
from src.database import get_connection


class SimulacroRepository:

    async def mostrarSimulacros(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id,
                   curso_id,
                   titulo,
                   descripcion,
                   fecha_publicacion,
                   tiempo_minutos,
                   estado
            FROM simulacros
        """)

        simulacros = []
        for row in cursor.fetchall():
            simulacros.append({
                "id": row.id,
                "curso_id": row.curso_id,
                "titulo": row.titulo,
                "descripcion": row.descripcion,
                "fecha_publicacion": row.fecha_publicacion,
                "tiempo_minutos": row.tiempo_minutos,
                "estado": row.estado
            })

        conn.close()
        return simulacros

    async def agregarSimulacro(self, simulacro: Simulacro):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO simulacros
            (curso_id, titulo, descripcion,
             fecha_publicacion, tiempo_minutos, estado)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            simulacro.curso_id,
            simulacro.titulo,
            simulacro.descripcion,
            simulacro.fecha_publicacion,
            simulacro.tiempo_minutos,
            simulacro.estado
        ))

        conn.commit()
        conn.close()

        return {"mensaje": "Simulacro agregado correctamente"}

    async def actualizarSimulacro(self, id: int, simulacro: SimulacroActualizar):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE simulacros
            SET curso_id = ?,
                titulo = ?,
                descripcion = ?,
                fecha_publicacion = ?,
                tiempo_minutos = ?,
                estado = ?
            WHERE id = ?
        """, (
            simulacro.curso_id,
            simulacro.titulo,
            simulacro.descripcion,
            simulacro.fecha_publicacion,
            simulacro.tiempo_minutos,
            simulacro.estado,
            id
        ))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Simulacro no encontrado"}

        return {"mensaje": "Simulacro actualizado correctamente"}

    async def eliminarSimulacro(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM simulacros
            WHERE id = ?
        """, (id,))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Simulacro no encontrado"}

        return {"mensaje": "Simulacro eliminado correctamente"}