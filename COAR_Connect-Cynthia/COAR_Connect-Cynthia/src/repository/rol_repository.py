from src.schema.rol import Rol, RolActualizar
from src.database import get_connection


class RolRepository:

    async def mostrarRoles(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nombre, descripcion
            FROM roles
        """)

        roles = []
        for row in cursor.fetchall():
            roles.append({
                "id": row.id,
                "nombre": row.nombre,
                "descripcion": row.descripcion
            })

        conn.close()
        return roles

    async def agregarRol(self, rol: Rol):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO roles (nombre, descripcion)
            VALUES (?, ?)
        """, (
            rol.nombre,
            rol.descripcion
        ))

        conn.commit()
        conn.close()

        return {"mensaje": "Rol agregado correctamente"}

    async def actualizarRol(self, id: int, rol: RolActualizar):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE roles
            SET nombre = ?, descripcion = ?
            WHERE id = ?
        """, (
            rol.nombre,
            rol.descripcion,
            id
        ))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Rol no encontrado"}

        return {"mensaje": "Rol actualizado correctamente"}

    async def eliminarRol(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM roles WHERE id = ?", (id,))
        conn.commit()

        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Rol no encontrado"}

        return {"mensaje": "Rol eliminado correctamente"}