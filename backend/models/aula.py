class Aula:
    def __init__(self, id_aula, nombre, capacidad, tipo):
        self.id_aula = id_aula
        self.nombre = nombre
        self.capacidad = capacidad
        self.tipo = tipo


    @property
    def id_aula(self):
        return self.__id_aula


    @id_aula.setter
    def id_aula(self, id_aula):
        if id_aula is None or not str(id_aula).strip():
            raise ValueError("El ID del aula no puede quedar vacío.")
        self.__id_aula = str(id_aula).strip()


    @property
    def nombre(self):
        return self.__nombre


    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del aula no puede quedar vacío.")
        self.__nombre = nombre.strip()


    @property
    def capacidad(self):
        return self.__capacidad


    @capacidad.setter
    def capacidad(self, capacidad):
        if type(capacidad) is not int or capacidad <= 0:
            raise ValueError("La capacidad debe ser un número entero positivo.")
        self.__capacidad = capacidad


    @property
    def tipo(self):
        return self.__tipo


    @tipo.setter
    def tipo(self, tipo):
        if not isinstance(tipo, str) or not tipo.strip():
            raise ValueError("El tipo de aula no puede quedar vacío.")
        self.__tipo = tipo.strip()