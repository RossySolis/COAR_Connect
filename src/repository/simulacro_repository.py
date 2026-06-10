from src.schema.simulacro import Simulacro, SimulacroActualizar

class SimulacroRepository:
    simulacros: list[Simulacro] = []

    async def mostrarSimulacros(self):
        return self.simulacros

    async def agregarSimulacro(self, simulacro: Simulacro):
        for s in self.simulacros:
            if s.id == simulacro.id:
                return {"mensaje": "Ya existe un simulacro con ese ID"}

        self.simulacros.append(simulacro)
        return simulacro

    async def actualizarSimulacro(self, id: int, simulacro: SimulacroActualizar):
        for s in self.simulacros:
            if s.id == id:
                s.curso_id = simulacro.curso_id
                s.titulo = simulacro.titulo
                s.descripcion = simulacro.descripcion
                s.fecha_publicacion = simulacro.fecha_publicacion
                s.tiempo_minutos = simulacro.tiempo_minutos
                s.estado = simulacro.estado
                return s
        return {"mensaje": "Simulacro no encontrado"}

    async def eliminarSimulacro(self, id: int):
        for indice, s in enumerate(self.simulacros):
            if s.id == id:
                self.simulacros.pop(indice)
                return {"mensaje": "Simulacro eliminado correctamente"}
        return {"mensaje": "Simulacro no encontrado"}