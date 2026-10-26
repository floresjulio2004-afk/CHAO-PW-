from usuario import Usuario


class Docente(Usuario):
    def __init__(self, id_usuario, nombre, cedula, correo, contrasena_hash, especialidad):
        super().__init__(id_usuario, nombre, cedula, correo, contrasena_hash)
        self.especialidad = especialidad


    @property
    def especialidad(self):
        return self.__especialidad


    @especialidad.setter
    def especialidad(self, especialidad):
        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ValueError("La especialidad de un docente no puede quedar vacía")
        self.__especialidad = especialidad.strip()


    def editar_perfil(self, vista_horario):
        if not isinstance(vista_horario, str) or vista_horario.strip() == "":
            raise ValueError("La vista del horario no puede quedar vacía")
        return vista_horario.strip()


    def consultar_horario(self, horarios):
        return horarios


    def consultar_asignatura(self, asignaturas):
        return asignaturas


    def consultar_aula(self, aula):
        return aula


    def consultar_disponibilidad(self, disponibilidad):
        return disponibilidad


    def reportar_incidencia(self, incidencia):
        if not isinstance(incidencia, str) or not incidencia.strip():
            raise ValueError("La incidencia no puede quedar vacía")
        return incidencia.strip()