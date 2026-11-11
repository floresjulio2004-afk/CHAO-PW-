from models.usuario import Usuario


class Estudiante(Usuario):
    def __init__(self, nombre, cedula, correo, contrasena_hash, nivel):
        super().__init__(None, nombre, cedula, correo, contrasena_hash, "estudiante")
        self.nivel = nivel


    @property
    def nivel(self):
        return self.__nivel


    @nivel.setter
    def nivel(self, nivel):
        if not isinstance(nivel, str) or not nivel.strip():
            raise ValueError("El nivel del estudiante no puede quedar vacío.")
        self.__nivel = nivel.strip()


    def personalizar_interfaz(self, tema):
        self.tema = tema
        return self.tema