class Facultad:
    def __init__(self, id_facultad, nombre):
        self.id_facultad = id_facultad
        self.nombre = nombre


    @property
    def id_facultad(self):
        return self.__id_facultad


    @id_facultad.setter
    def id_facultad(self, id_facultad):
        if id_facultad is None or not str(id_facultad).strip():
            raise ValueError("El ID de la facultad no puede quedar vacío.")
        self.__id_facultad = str(id_facultad).strip()


    @property
    def nombre(self):
        return self.__nombre


    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre de la facultad no puede quedar vacío.")
        self.__nombre = nombre.strip()