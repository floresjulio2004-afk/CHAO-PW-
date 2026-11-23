from datetime import datetime


class TiempoHorario:
    def __init__(self, id_tiempo, dia, hora_inicio, hora_fin, id_aula):
        self.id_tiempo = id_tiempo
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.id_aula = id_aula


    @property
    def id_tiempo(self):
        return self.__id_tiempo


    @id_tiempo.setter
    def id_tiempo(self, id_tiempo):
        if id_tiempo is None or not str(id_tiempo).strip():
            raise ValueError("El ID del tiempo no puede quedar vacío.")
        self.__id_tiempo = str(id_tiempo).strip()


    @property
    def dia(self):
        return self.__dia


    @dia.setter
    def dia(self, dia):
        if not isinstance(dia, str) or not dia.strip():
            raise ValueError("El día no puede quedar vacío.")
        self.__dia = dia.strip().capitalize()


    @property
    def hora_inicio(self):
        return self.__hora_inicio


    @hora_inicio.setter
    def hora_inicio(self, hora_inicio):
        self.__validar_hora(hora_inicio)
        self.__hora_inicio = hora_inicio


    @property
    def hora_fin(self):
        return self.__hora_fin


    @hora_fin.setter
    def hora_fin(self, hora_fin):
        self.__validar_hora(hora_fin)
        self.__hora_fin = hora_fin


    @property
    def id_aula(self):
        return self.__id_aula


    @id_aula.setter
    def id_aula(self, id_aula):
        if id_aula is None or not str(id_aula).strip():
            raise ValueError("El aula asignada no puede quedar vacía.")
        self.__id_aula = str(id_aula).strip()


    @staticmethod
    def __validar_hora(hora):
        if not isinstance(hora, str):
            raise ValueError("La hora debe tener el formato HH:MM.")
        try:
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            raise ValueError("La hora debe tener el formato HH:MM.")