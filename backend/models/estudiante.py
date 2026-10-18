from usuario import Usuario


class Estudiante(Usuario):

    def __init__(self, id_usuario, nombre, cedula, correo, contrasena, nivel):
        super().__init__(id_usuario, nombre, cedula, correo, contrasena)
        self.__nivel = nivel
    

    @property
    def nivel(self):
        return self.__nivel


    @nivel.setter
    def nivel(self, nivel):
        if nivel is None:
            raise ValueError("El nivel del estudiante no puede quedar vacio")
        self.__nivel = nivel
        

    def iniciar_sesion(self):
        pass


    def editar_perfil(self):
        pass


    def cerrar_sesion(self):
        pass


    def consultar_horario(self):
        pass


    def consultar_docente(self):
        pass


    def consultar_asignatura(self):
        pass


    def consultar_incidencia(self):
        pass
