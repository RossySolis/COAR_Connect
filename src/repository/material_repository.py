from src.schema.material import Material, MaterialActualizar

class MaterialRepository:
    materiales: list[Material] = []

    async def mostrarMateriales(self):
        return self.materiales

    async def agregarMaterial(self, material: Material):
        for m in self.materiales:
            if m.id == material.id:
                return {"mensaje": "Ya existe un material con ese ID"}

        self.materiales.append(material)
        return material

    async def actualizarMaterial(self, id: int, material: MaterialActualizar):
        for m in self.materiales:
            if m.id == id:
                m.curso_id = material.curso_id
                m.titulo = material.titulo
                m.descripcion = material.descripcion
                m.tipo = material.tipo
                m.archivo_url = material.archivo_url
                m.fecha_subida = material.fecha_subida
                return m
        return {"mensaje": "Material no encontrado"}

    async def eliminarMaterial(self, id: int):
        for indice, m in enumerate(self.materiales):
            if m.id == id:
                self.materiales.pop(indice)
                return {"mensaje": "Material eliminado correctamente"}
        return {"mensaje": "Material no encontrado"}