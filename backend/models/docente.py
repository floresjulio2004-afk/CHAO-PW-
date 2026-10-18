from usuario import Usuario


class Docente(Usuario):
    def __init__(self, id_usuario, nombre, cedula, correo, contrasena, especialidad):
        super().__init__(id_usuario, nombre, cedula, cooreo, contrasena0)
        self.__especialidad = especialidad


    @property
    def especialidad(self):
        return self.__especialidad


    def editar_perfil(self):
        pass


    def consultar_horario(self):
        pass


    def consultar_asignatura(self):
        pass

    
    def consultar_aula(self):
        pass


    def consultar_disponibilidad(self):
        pass


    def reportar_incidencia(self):
        pass