class Horario:
    def __init__(self, id_horario, id_asignatura, id_paralelo, id_periodo, id_docente, tiempos, estado, observacion):
        self.id_horario = id_horario
        self.id_asignatura = id_asignatura
        self.id_paralelo = id_paralelo
        self.id_periodo = id_periodo
        self.id_docente = id_docente
        self.tiempos = tiempos
        self.estado = estado
        self.observacion = observacion


    @property
    def id_horario(self):
        return self.__id_horario


    @id_horario.setter
    def id_horario(self, id_horario):
        if id_horario is None or not str(id_horario).strip():
            raise ValueError("El ID del horario no puede quedar vacío.")
        self.__id_horario = str(id_horario).strip()


    @property
    def id_asignatura(self):
        return self.__id_asignatura


    @id_asignatura.setter
    def id_asignatura(self, id_asignatura):
        if id_asignatura is None or not str(id_asignatura).strip():
            raise ValueError("La asignatura no puede quedar vacía.")
        self.__id_asignatura = str(id_asignatura).strip()


    @property
    def id_paralelo(self):
        return self.__id_paralelo


    @id_paralelo.setter
    def id_paralelo(self, id_paralelo):
        if id_paralelo is None or not str(id_paralelo).strip():
            raise ValueError("El paralelo no puede quedar vacío.")
        self.__id_paralelo = str(id_paralelo).strip()


    @property
    def id_periodo(self):
        return self.__id_periodo


    @id_periodo.setter
    def id_periodo(self, id_periodo):
        if id_periodo is None or not str(id_periodo).strip():
            raise ValueError("El periodo académico no puede quedar vacío.")
        self.__id_periodo = str(id_periodo).strip()


    @property
    def id_docente(self):
        return self.__id_docente


    @id_docente.setter
    def id_docente(self, id_docente):
        if id_docente is None or not str(id_docente).strip():
            raise ValueError("El docente no puede quedar vacío.")
        self.__id_docente = str(id_docente).strip()


    @property
    def tiempos(self):
        return self.__tiempos


    @tiempos.setter
    def tiempos(self, tiempos):
        if not isinstance(tiempos, list) or not tiempos:
            raise ValueError("El horario debe contener al menos una sesión.")
        self.__tiempos = tiempos


    @property
    def estado(self):
        return self.__estado


    @estado.setter
    def estado(self, estado):
        if not isinstance(estado, str) or not estado.strip():
            raise ValueError("El estado no puede quedar vacío.")
        self.__estado = estado.strip().lower()


    @property
    def observacion(self):
        return self.__observacion


    @observacion.setter
    def observacion(self, observacion):
        if observacion is not None and not isinstance(observacion, str):
            raise ValueError("La observación debe ser un texto válido.")
        self.__observacion = observacion.strip() if observacion else ""