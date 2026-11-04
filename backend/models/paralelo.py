class Paralelo:
    def __init__(self, id_paralelo, nombre, descripcion):
        self.id_paralelo = id_paralelo
        self.nombre = nombre
        self.descripcion = descripcion


    @property
    def id_paralelo(self):
        return self.__id_paralelo


    @id_paralelo.setter
    def id_paralelo(self, id_paralelo):
        if id_paralelo is None or not str(id_paralelo).strip():
            raise ValueError("El ID del paralelo no puede quedar vacío.")
        self.__id_paralelo = str(id_paralelo).strip()


    @property
    def nombre(self):
        return self.__nombre


    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del paralelo no puede quedar vacío.")
        nombre = nombre.strip().upper()
        if len(nombre) != 1 or not nombre.isalpha():
            raise ValueError("El nombre del paralelo debe ser una letra.")
        self.__nombre = nombre


    @property
    def descripcion(self):
        return self.__descripcion


    @descripcion.setter
    def descripcion(self, descripcion):
        if not isinstance(descripcion, str) or not descripcion.strip():
            raise ValueError("La descripción no puede quedar vacía.")
        descripcion = descripcion.strip()
        if len(descripcion) > 300:
            raise ValueError("La descripción no puede superar los 300 caracteres.")
        self.__descripcion = descripcion