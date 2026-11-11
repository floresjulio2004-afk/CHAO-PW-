from models.usuario import Usuario


class Docente(Usuario):
    def __init__(self, nombre, cedula, correo, contrasena_hash, especialidad):
        super().__init__(None, nombre, cedula, correo, contrasena_hash, "docente")
        self.especialidad = especialidad


    @property
    def especialidad(self):
        return self.__especialidad


    @especialidad.setter
    def especialidad(self, especialidad):
        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ValueError("La especialidad del docente no puede quedar vacía.")
        self.__especialidad = especialidad.strip()


    def personalizar_interfaz(self, tema):
        self.tema = tema
        return self.tema