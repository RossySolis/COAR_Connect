from fastapi import APIRouter
from src.services.material_service import MaterialService
from src.schema.material import Material, MaterialActualizar

routerMaterial = APIRouter(prefix="/material", tags=["Material"])

materialService = MaterialService()

@routerMaterial.get("/")
async def obtenerMateriales():
    return await materialService.mostrarMateriales()

@routerMaterial.post("/agregar")
async def agregarMaterial(material: Material):
    return await materialService.agregarMaterial(material)

@routerMaterial.put("/{id_material}")
async def actualizarMaterial(id_material: int, material: MaterialActualizar):
    return await materialService.actualizarMaterial(id_material, material)

@routerMaterial.delete("/{id_material}")
async def eliminarMaterial(id_material: int):
    return await materialService.eliminarMaterial(id_material)