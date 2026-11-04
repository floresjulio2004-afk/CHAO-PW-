from datetime import date


class PeriodoAcademico:
    def __init__(self, id_periodo, nombre, fecha_inicio, fecha_fin, estado):
        self.id_periodo = id_periodo
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado
        if self.fecha_inicio >= self.fecha_fin:
            raise ValueError("La fecha de inicio debe ser anterior a la fecha de finalización.")


    @property
    def id_periodo(self):
        return self.__id_periodo


    @id_periodo.setter
    def id_periodo(self, id_periodo):
        if id_periodo is None or not str(id_periodo).strip():
            raise ValueError("El ID del periodo no puede quedar vacío.")
        self.__id_periodo = str(id_periodo).strip()


    @property
    def nombre(self):
        return self.__nombre


    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del periodo no puede quedar vacío.")
        self.__nombre = nombre.strip()


    @property
    def fecha_inicio(self):
        return self.__fecha_inicio


    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = self.__validar_fecha(fecha_inicio)


    @property
    def fecha_fin(self):
        return self.__fecha_fin


    @fecha_fin.setter
    def fecha_fin(self, fecha_fin):
        self.__fecha_fin = self.__validar_fecha(fecha_fin)


    @property
    def estado(self):
        return self.__estado


    @estado.setter
    def estado(self, estado):
        if not isinstance(estado, str) or not estado.strip():
            raise ValueError("El estado del periodo no puede quedar vacío.")
        self.__estado = estado.strip().lower()


    @staticmethod
    def __validar_fecha(fecha):
        if isinstance(fecha, date):
            return fecha
        if not isinstance(fecha, str):
            raise ValueError("La fecha debe tener el formato YYYY-MM-DD.")
        try:
            return date.fromisoformat(fecha)
        except ValueError:
            raise ValueError("La fecha debe tener el formato YYYY-MM-DD.")