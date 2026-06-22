from src.schema.rol import Rol, RolActualizar

class RolRepository:
    roles: list[Rol] = []

    async def mostrarRoles(self):
        return self.roles

    async def agregarRol(self, rol: Rol):
        for r in self.roles:
            if r.id == rol.id:
                return {"mensaje": "Ya existe un rol con ese ID"}
            if r.nombre == rol.nombre:
                return {"mensaje": "Ya existe un rol con ese nombre"}

        self.roles.append(rol)
        return rol

    async def actualizarRol(self, id: int, rol: RolActualizar):
        for r in self.roles:
            if r.id == id:
                r.nombre = rol.nombre
                r.descripcion = rol.descripcion
                return r
        return {"mensaje": "Rol no encontrado"}

    async def eliminarRol(self, id: int):
        for indice, r in enumerate(self.roles):
            if r.id == id:
                self.roles.pop(indice)
                return {"mensaje": "Rol eliminado correctamente"}
        return {"mensaje": "Rol no encontrado"}