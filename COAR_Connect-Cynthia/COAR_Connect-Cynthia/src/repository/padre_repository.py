from src.schema.padre import Padre, PadreActualizar
from src.database import get_connection


class PadreRepository:

    async def mostrarPadres(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id,
                   usuario_id,
                   estudiante_id,
                   parentesco
            FROM padres
        """)

        padres = []
        for row in cursor.fetchall():
            padres.append({
                "id": row.id,
                "usuario_id": row.usuario_id,
                "estudiante_id": row.estudiante_id,
                "parentesco": row.parentesco
            })

        conn.close()
        return padres

    async def agregarPadre(self, padre: Padre):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO padres
            (usuario_id, estudiante_id, parentesco)
            VALUES (?, ?, ?)
        """, (
            padre.usuario_id,
            padre.estudiante_id,
            padre.parentesco
        ))

        conn.commit()
        conn.close()

        return {"mensaje": "Padre agregado correctamente"}

    async def actualizarPadre(self, id: int, padre: PadreActualizar):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE padres
            SET usuario_id = ?,
                estudiante_id = ?,
                parentesco = ?
            WHERE id = ?
        """, (
            padre.usuario_id,
            padre.estudiante_id,
            padre.parentesco,
            id
        ))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Padre no encontrado"}

        return {"mensaje": "Padre actualizado correctamente"}

    async def eliminarPadre(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM padres
            WHERE id = ?
        """, (id,))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Padre no encontrado"}

        return {"mensaje": "Padre eliminado correctamente"}