import uuid
from datetime import datetime
from models.horario import Horario
from models.tiempo_horario import TiempoHorario


DIAS_SEMANA = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")


class ConstructorHorario:
    def __init__(self):
        self.reiniciar()


    def reiniciar(self):
        self.__id_horario = None
        self.__id_asignatura = None
        self.__id_paralelo = None
        self.__id_periodo = None
        self.__id_docente = None
        self.__tiempos = []
        self.__estado = "activo"
        self.__observacion = ""
        return self


    def con_id(self, id_horario):
        self.__id_horario = id_horario
        return self


    def con_asignatura(self, id_asignatura):
        self.__id_asignatura = id_asignatura
        return self


    def con_paralelo(self, id_paralelo):
        self.__id_paralelo = id_paralelo
        return self


    def con_periodo(self, id_periodo):
        self.__id_periodo = id_periodo
        return self


    def con_docente(self, id_docente):
        self.__id_docente = id_docente
        return self


    def con_estado(self, estado):
        self.__estado = estado
        return self


    def con_observacion(self, observacion):
        self.__observacion = observacion
        return self


    def agregar_tiempo(self, dia, hora_inicio, hora_fin, id_aula):
        dia = self.__normalizar_dia(dia)
        inicio = self.__normalizar_hora(hora_inicio)
        fin = self.__normalizar_hora(hora_fin)
        if inicio >= fin:
            raise ValueError("La hora de fin debe ser posterior a la hora de inicio.")
        tiempo = TiempoHorario(f"TMP-{uuid.uuid4()}", dia, inicio, fin, id_aula)
        for existente in self.__tiempos:
            if (
                existente.dia == tiempo.dia
                and existente.hora_inicio < tiempo.hora_fin
                and tiempo.hora_inicio < existente.hora_fin
            ):
                raise ValueError(
                    "Las sesiones de un mismo horario no pueden superponerse."
                )
        self.__tiempos.append(tiempo)
        return self


    def construir(self):
        horario = Horario(
            self.__id_horario or f"HOR-{uuid.uuid4()}",
            self.__id_asignatura,
            self.__id_paralelo,
            self.__id_periodo,
            self.__id_docente,
            list(self.__tiempos),
            self.__estado,
            self.__observacion
        )
        self.reiniciar()
        return horario


    @staticmethod
    def __normalizar_dia(dia):
        if not isinstance(dia, str) or not dia.strip():
            raise ValueError("El día no puede quedar vacío.")
        dia = dia.strip().capitalize()
        if dia not in DIAS_SEMANA:
            raise ValueError(f"El día '{dia}' no es válido.")
        return dia


    @staticmethod
    def __normalizar_hora(hora):
        if not isinstance(hora, str):
            raise ValueError("La hora debe tener el formato HH:MM.")
        try:
            return datetime.strptime(hora.strip(), "%H:%M").strftime("%H:%M")
        except ValueError:
            raise ValueError("La hora debe tener el formato HH:MM.")