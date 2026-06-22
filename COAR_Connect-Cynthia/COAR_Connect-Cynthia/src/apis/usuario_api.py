from fastapi import APIRouter
from src.services.usuario_service import UsuarioService
from src.schema.usuario import Usuario, UsuarioActualizar

routerUsuario = APIRouter(
    prefix="/usuario",
    tags=["Usuario"]
)

usuarioService = UsuarioService()

@routerUsuario.get("/")
async def obtenerUsuarios():
    return await usuarioService.mostrarUsuarios()

@routerUsuario.post("/agregar")
async def agregarUsuario(usuario: Usuario):
    return await usuarioService.agregarUsuario(usuario)

@routerUsuario.put("/{id_usuario}")
async def actualizarUsuario(id_usuario: int, usuario: UsuarioActualizar):
    return await usuarioService.actualizarUsuario(id_usuario, usuario)

@routerUsuario.delete("/{id_usuario}")
async def eliminarUsuario(id_usuario: int):
    return await usuarioService.eliminarUsuario(id_usuario)