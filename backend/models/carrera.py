class Carrera:
    def __init__(self, id_carrera, nombre, codigo):
        self.id_carrera = id_carrera
        self.nombre = nombre
        self.codigo = codigo


    @property
    def id_carrera(self):
        return self.__id_carrera


    @id_carrera.setter
    def id_carrera(self, id_carrera):
        if id_carrera is None or not str(id_carrera).strip():
            raise ValueError("El ID de la carrera no puede quedar vacío.")
        self.__id_carrera = str(id_carrera).strip()


    @property
    def nombre(self):
        return self.__nombre


    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre de la carrera no puede quedar vacío.")
        self.__nombre = nombre.strip()


    @property
    def codigo(self):
        return self.__codigo


    @codigo.setter
    def codigo(self, codigo):
        if codigo is None or not str(codigo).strip():
            raise ValueError("El código de la carrera no puede quedar vacío.")
        self.__codigo = str(codigo).strip()