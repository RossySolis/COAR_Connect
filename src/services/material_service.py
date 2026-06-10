from src.repository.material_repository import MaterialRepository
from src.schema.material import Material, MaterialActualizar

class MaterialService:
    def __init__(self):
        self.materialRepository = MaterialRepository()

    async def mostrarMateriales(self):
        return await self.materialRepository.mostrarMateriales()

    async def agregarMaterial(self, material: Material):
        return await self.materialRepository.agregarMaterial(material)

    async def actualizarMaterial(self, id: int, material: MaterialActualizar):
        return await self.materialRepository.actualizarMaterial(id, material)

    async def eliminarMaterial(self, id: int):
        return await self.materialRepository.eliminarMaterial(id)