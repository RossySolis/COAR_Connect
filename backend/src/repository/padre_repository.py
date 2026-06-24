from src.schema.padre import Padre, PadreActualizar
from src.database import get_connection


class PadreRepository:

    async def mostrarPadres(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id,
                   usuario_id,
                   parentesco,
                   codigo_vinculacion
            FROM padres
        """)

        padres = []
        for row in cursor.fetchall():
            padres.append({
                "id": row.id,
                "usuario_id": row.usuario_id,
                "parentesco": row.parentesco,
                "codigo_vinculacion": row.codigo_vinculacion
            })

        conn.close()
        return padres

    async def agregarPadre(self, padre: Padre):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO padres
            (usuario_id, parentesco, codigo_vinculacion)
            VALUES (?, ?, ?)
        """, (
            padre.usuario_id,
            padre.parentesco,
            padre.codigo_vinculacion
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
                parentesco = ?,
                codigo_vinculacion = ?
            WHERE id = ?
        """, (
            padre.usuario_id,
            padre.parentesco,
            padre.codigo_vinculacion,
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