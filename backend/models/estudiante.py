from usuario import Usuario


class Estudiante(Usuario):
    def __init__(self, id_usuario, nombre, cedula, correo, contrasena_hash, nivel):
        super().__init__(id_usuario, nombre, cedula, correo, contrasena_hash)
        self.nivel = nivel


    @property
    def nivel(self):
        return self.__nivel


    @nivel.setter
    def nivel(self, nivel):
        if not isinstance(nivel, str) or not nivel.strip():
            raise ValueError("El nivel del estudiante no puede quedar vacío")
        self.__nivel = nivel.strip()


    def editar_perfil(self, vista_horario):
        if not isinstance(vista_horario, str) or vista_horario.strip() == "":
            raise ValueError("La vista del horario no puede quedar vacía")
        return vista_horario.strip()


    def consultar_horario(self, horarios):
        return horarios


    def consultar_docente(self, asignatura):
        if not asignatura:
            return None
        return asignatura.get("docente")


    def consultar_asignatura(self, horario):
        if not horario:
            return None
        return horario.get("asignatura")


    def consultar_incidencia(self, incidencias):
        return incidencias