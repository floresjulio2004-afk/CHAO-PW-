from datetime import datetime


class Incidencia:
    def __init__(self, id_incidencia, descripcion, fecha, tipo, estado):
        self.id_incidencia = id_incidencia
        self.descripcion = descripcion
        self.fecha = fecha
        self.tipo = tipo
        self.estado = estado


    @property
    def id_incidencia(self):
        return self.__id_incidencia


    @id_incidencia.setter
    def id_incidencia(self, id_incidencia):
        if id_incidencia is None or not str(id_incidencia).strip():
            raise ValueError("El ID de la incidencia no puede quedar vacío.")
        self.__id_incidencia = str(id_incidencia).strip()


    @property
    def descripcion(self):
        return self.__descripcion


    @descripcion.setter
    def descripcion(self, descripcion):
        if not isinstance(descripcion, str) or not descripcion.strip():
            raise ValueError("La descripción no puede quedar vacía.")
        self.__descripcion = descripcion.strip()


    @property
    def fecha(self):
        return self.__fecha


    @fecha.setter
    def fecha(self, fecha):
        if isinstance(fecha, datetime):
            self.__fecha = fecha
            return
        if not isinstance(fecha, str):
            raise ValueError("La fecha debe ser válida.")
        try:
            self.__fecha = datetime.fromisoformat(fecha)
        except ValueError:
            raise ValueError("La fecha debe tener un formato válido.")


    @property
    def tipo(self):
        return self.__tipo


    @tipo.setter
    def tipo(self, tipo):
        if not isinstance(tipo, str) or not tipo.strip():
            raise ValueError("El tipo de incidencia no puede quedar vacío.")
        self.__tipo = tipo.strip().lower()


    @property
    def estado(self):
        return self.__estado


    @estado.setter
    def estado(self, estado):
        if not isinstance(estado, str) or not estado.strip():
            raise ValueError("El estado no puede quedar vacío.")
        self.__estado = estado.strip().lower()