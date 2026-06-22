from src.schema.resultado import Resultado, ResultadoActualizar

class ResultadoRepository:
    resultados: list[Resultado] = []

    async def mostrarResultados(self):
        return self.resultados

    async def agregarResultado(self, resultado: Resultado):
        for r in self.resultados:
            if r.id == resultado.id:
                return {"mensaje": "Ya existe un resultado con ese ID"}
            if r.estudiante_id == resultado.estudiante_id and r.simulacro_id == resultado.simulacro_id:
                return {"mensaje": "Ya existe un resultado para este estudiante y simulacro"}

        self.resultados.append(resultado)
        return resultado

    async def actualizarResultado(self, id: int, resultado: ResultadoActualizar):
        for r in self.resultados:
            if r.id == id:
                r.estudiante_id = resultado.estudiante_id
                r.simulacro_id = resultado.simulacro_id
                r.puntaje = resultado.puntaje
                r.fecha_realizacion = resultado.fecha_realizacion
                r.observacion = resultado.observacion
                return r
        return {"mensaje": "Resultado no encontrado"}

    async def eliminarResultado(self, id: int):
        for indice, r in enumerate(self.resultados):
            if r.id == id:
                self.resultados.pop(indice)
                return {"mensaje": "Resultado eliminado correctamente"}
        return {"mensaje": "Resultado no encontrado"}