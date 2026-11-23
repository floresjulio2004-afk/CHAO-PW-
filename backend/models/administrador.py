from models.usuario import Usuario


class Administrador(Usuario):
    def __init__(self, nombre, cedula, correo, contrasena_hash):
        super().__init__(None, nombre, cedula, correo, contrasena_hash, "administrador")


    def personalizar_interfaz(self, tema):
        self.tema = tema
        return self.tema