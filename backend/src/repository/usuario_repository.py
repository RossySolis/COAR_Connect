from src.schema.usuario import Usuario, UsuarioActualizar
from src.database import get_connection


class UsuarioRepository:

    async def mostrarUsuarios(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nombre, apellido, correo, password, rol_id, telefono, estado
            FROM usuarios
        """)

        usuarios = []
        for row in cursor.fetchall():
            usuarios.append({
                "id": row.id,
                "nombre": row.nombre,
                "apellido": row.apellido,
                "correo": row.correo,
                "password": row.password,
                "rol_id": row.rol_id,
                "telefono": row.telefono,
                "estado": row.estado
            })

        conn.close()
        return usuarios

    async def agregarUsuario(self, usuario: Usuario):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO usuarios (nombre, apellido, correo, password, rol_id, telefono, estado)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            usuario.nombre,
            usuario.apellido,
            usuario.correo,
            usuario.password,
            usuario.rol_id,
            usuario.telefono,
            usuario.estado
        ))

        conn.commit()
        conn.close()

        return {"mensaje": "Usuario agregado correctamente"}

    async def actualizarUsuario(self, id: int, usuario: UsuarioActualizar):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE usuarios
            SET nombre = ?, apellido = ?, correo = ?, rol_id = ?, telefono = ?, estado = ?
            WHERE id = ?
        """, (
            usuario.nombre,
            usuario.apellido,
            usuario.correo,
            usuario.rol_id,
            usuario.telefono,
            usuario.estado,
            id
        ))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Usuario no encontrado"}

        return {"mensaje": "Usuario actualizado correctamente"}

    async def eliminarUsuario(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
        conn.commit()

        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Usuario no encontrado"}

        return {"mensaje": "Usuario eliminado correctamente"}