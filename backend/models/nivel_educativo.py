class NivelEducativo:
    def __init__(self, id_nivel, nombre, descripcion):
        self.id_nivel = id_nivel
        self.nombre = nombre
        self.descripcion = descripcion


    @property
    def id_nivel(self):
        return self.__id_nivel


    @id_nivel.setter
    def id_nivel(self, id_nivel):
        if id_nivel is None or str(id_nivel).strip() == "":
            raise ValueError("El ID del nivel educativo no puede quedar vacío.")
        self.__id_nivel = id_nivel


    @property
    def nombre(self):
        return self.__nombre


    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del nivel educativo no puede quedar vacío.")
        self.__nombre = nombre.strip()


    @property
    def descripcion(self):
        return self.__descripcion


    @descripcion.setter
    def descripcion(self, descripcion):
        if not isinstance(descripcion, str) or not descripcion.strip():
            raise ValueError("La descripción no puede quedar vacía.")
        self.__descripcion = descripcion.strip()