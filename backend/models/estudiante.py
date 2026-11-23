from models.usuario import Usuario


class Estudiante(Usuario):
    def __init__(self, nombre, cedula, correo, contrasena_hash, id_carrera, id_nivel, id_paralelo):
        super().__init__(None, nombre, cedula, correo, contrasena_hash, "estudiante")
        self.id_carrera = id_carrera
        self.id_nivel = id_nivel
        self.id_paralelo = id_paralelo


    @property
    def id_carrera(self):
        return self.__id_carrera


    @id_carrera.setter
    def id_carrera(self, id_carrera):
        self.__id_carrera = self.__validar_id(
            id_carrera,
            "La carrera del estudiante no puede quedar vacia."
        )


    @property
    def id_nivel(self):
        return self.__id_nivel


    @id_nivel.setter
    def id_nivel(self, id_nivel):
        self.__id_nivel = self.__validar_id(
            id_nivel,
            "El nivel del estudiante no puede quedar vacio."
        )


    @property
    def id_paralelo(self):
        return self.__id_paralelo


    @id_paralelo.setter
    def id_paralelo(self, id_paralelo):
        self.__id_paralelo = self.__validar_id(
            id_paralelo,
            "El paralelo del estudiante no puede quedar vacio."
        )


    @staticmethod
    def __validar_id(valor, mensaje):
        if valor is None or not str(valor).strip():
            raise ValueError(mensaje)
        return str(valor).strip()


    def datos_adicionales(self):
        return {
            "id_carrera": self.id_carrera,
            "id_nivel": self.id_nivel,
            "id_paralelo": self.id_paralelo
        }


    def personalizar_interfaz(self, tema):
        self.tema = tema
        return self.tema