from usuario import Usuario


class Coordinador(Usuario):
    def __init__(self, id_usuario, nombre, cedula, correo, contrasena):
        super().__init__(id_usuario, nombre, cedula, correo, contrasena)

    
    def editar_perfil(self):
        pass


    def gestionar_horario(self):
        pass


    def gestionar_aula(self):
        pass


    def gestionar_asignatura(self):
        pass


    def gestionar_docente(self):
        pass


    def gestionar_paralelo(self):
        pass


    def gestionar_periodo(self):
        pass