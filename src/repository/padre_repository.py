from src.schema.padre import Padre, PadreActualizar

class PadreRepository:
    padres: list[Padre] = []

    async def mostrarPadres(self):
        return self.padres

    async def agregarPadre(self, padre: Padre):
        for p in self.padres:
            if p.id == padre.id:
                return {"mensaje": "Ya existe un padre con ese ID"}
            if p.usuario_id == padre.usuario_id:
                return {"mensaje": "Este usuario ya está registrado como padre"}

        self.padres.append(padre)
        return padre

    async def actualizarPadre(self, id: int, padre: PadreActualizar):
        for p in self.padres:
            if p.id == id:
                p.usuario_id = padre.usuario_id
                p.estudiante_id = padre.estudiante_id
                p.parentesco = padre.parentesco
                return p
        return {"mensaje": "Padre no encontrado"}

    async def eliminarPadre(self, id: int):
        for indice, p in enumerate(self.padres):
            if p.id == id:
                self.padres.pop(indice)
                return {"mensaje": "Padre eliminado correctamente"}
        return {"mensaje": "Padre no encontrado"}