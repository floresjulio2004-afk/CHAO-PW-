from usuario import Usuario


class Coordinador(Usuario):
    def __init__(self, id_usuario, nombre, cedula, correo, contrasena_hash):
        super().__init__(id_usuario, nombre, cedula, correo, contrasena_hash)


    def editar_perfil(self, vista_horario):
        if not isinstance(vista_horario, str) or vista_horario.strip() == "":
            raise ValueError("La vista del horario no puede quedar vacía")
        return vista_horario.strip()


    def gestionar_horario(self, horario):
        return horario


    def gestionar_aula(self, aula):
        return aula


    def gestionar_asignatura(self, asignatura):
        return asignatura


    def gestionar_docente(self, docente):
        return docente


    def gestionar_paralelo(self, paralelo):
        return paralelo


    def gestionar_periodo(self, periodo):
        return periodo