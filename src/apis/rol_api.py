from fastapi import APIRouter
from src.services.rol_service import RolService
from src.schema.rol import Rol, RolActualizar

routerRol = APIRouter(prefix="/rol", tags=["Rol"])

rolService = RolService()

@routerRol.get("/")
async def obtenerRoles():
    return await rolService.mostrarRoles()

@routerRol.post("/agregar")
async def agregarRol(rol: Rol):
    return await rolService.agregarRol(rol)

@routerRol.put("/{id_rol}")
async def actualizarRol(id_rol: int, rol: RolActualizar):
    return await rolService.actualizarRol(id_rol, rol)

@routerRol.delete("/{id_rol}")
async def eliminarRol(id_rol: int):
    return await rolService.eliminarRol(id_rol)