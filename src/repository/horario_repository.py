from src.schema.horario import Horario, HorarioActualizar

class HorarioRepository:

    def __init__(self):
        self.horarios: list[Horario] = []

    async def mostrarHorarios(self):
        return self.horarios

    async def agregarHorario(self, horario: Horario):
        for h in self.horarios:
            if h.id == horario.id:
                return {"mensaje": "Ya existe un horario con ese ID"}

        self.horarios.append(horario)
        return horario

    async def actualizarHorario(self, id: int, horario: HorarioActualizar):
        for h in self.horarios:
            if h.id == id:
                h.curso_id = horario.curso_id
                h.dia = horario.dia
                h.hora_inicio = horario.hora_inicio
                h.hora_fin = horario.hora_fin
                h.modalidad = horario.modalidad
                h.cupos = horario.cupos
                h.estado = horario.estado
                return h
        return {"mensaje": "Horario no encontrado"}

    async def eliminarHorario(self, id: int):
        for indice, h in enumerate(self.horarios):
            if h.id == id:
                self.horarios.pop(indice)
                return {"mensaje": "Horario eliminado correctamente"}
        return {"mensaje": "Horario no encontrado"}