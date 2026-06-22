from src.schema.usuario import Usuario, UsuarioActualizar

class UsuarioRepository:

    def __init__(self):
        self.usuarios: list[Usuario] = []

    async def mostrarUsuarios(self):
        return self.usuarios

    async def agregarUsuario(self, usuario: Usuario):
        for u in self.usuarios:
            if u.id == usuario.id:
                return {"mensaje": "Ya existe un usuario con ese ID"}
        self.usuarios.append(usuario)
        return usuario

    async def actualizarUsuario(self, id: int, usuario: UsuarioActualizar):
        for u in self.usuarios:
            if u.id == id:
                u.nombre = usuario.nombre
                u.apellido = usuario.apellido
                u.correo = usuario.correo
                u.rol = usuario.rol
                u.telefono = usuario.telefono
                u.estado = usuario.estado
                return u
        return {"mensaje": "Usuario no encontrado"}

    async def eliminarUsuario(self, id: int):
        for indice, u in enumerate(self.usuarios):
            if u.id == id:
                self.usuarios.pop(indice)
                return {"mensaje": "Usuario eliminado correctamente"}
        return {"mensaje": "Usuario no encontrado"}