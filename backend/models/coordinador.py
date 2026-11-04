from usuario import Usuario


class Coordinador(Usuario):
    def __init__(self, id_usuario, nombre, cedula, correo, contrasena_hash):
        super().__init__(id_usuario, nombre, cedula, correo, contrasena_hash, "coordinador")


    def personalizar_interfaz(self, tema):
        self.tema = tema
        return self.tema