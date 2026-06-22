from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.apis.rol_api import routerRol
from src.apis.usuario_api import routerUsuario
from src.apis.estudiante_api import routerEstudiante
from src.apis.padre_api import routerPadre
from src.apis.docente_api import routerDocente
from src.apis.curso_api import routerCurso
from src.apis.horario_api import routerHorario
from src.apis.inscripcion_api import routerInscripcion
from src.apis.material_api import routerMaterial
from src.apis.simulacro_api import routerSimulacro
from src.apis.resultado_api import routerResultado
from src.apis.seguimiento_academico_api import routerSeguimientoAcademico
from src.apis.auth_api import routerAuth

app = FastAPI(
    title="COAR Connect API",
    description="Backend de COAR Connect",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routerRol, prefix="/api")
app.include_router(routerUsuario, prefix="/api")
app.include_router(routerEstudiante, prefix="/api")
app.include_router(routerPadre, prefix="/api")
app.include_router(routerDocente, prefix="/api")
app.include_router(routerCurso, prefix="/api")
app.include_router(routerHorario, prefix="/api")
app.include_router(routerInscripcion, prefix="/api")
app.include_router(routerMaterial, prefix="/api")
app.include_router(routerSimulacro, prefix="/api")
app.include_router(routerResultado, prefix="/api")
app.include_router(routerSeguimientoAcademico, prefix="/api")
app.include_router(routerAuth, prefix="/api")

@app.get("/")
async def inicio():
    return {"mensaje": "API COAR Connect funcionando correctamente"}