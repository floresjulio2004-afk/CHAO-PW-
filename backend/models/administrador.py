from usuario import Usuario


class Administrador(Usuario):
    def __init__(self, id_usuario, nombre, cedula, correo, contrasena_hash):
        super().__init__(id_usuario, nombre, cedula, correo, contrasena_hash)


    def editar_perfil(self, vista_horario):
        if not isinstance(vista_horario, str) or vista_horario.strip() == "":
            raise ValueError("La vista del horario no puede quedar vacía")
        return vista_horario.strip()


    def gestionar_usuario(self, usuario):
        return usuario


    def gestionar_asignatura(self, asignatura):
        return asignatura


    def gestionar_aula(self, aula):
        return aula


    def gestionar_periodo(self, periodo):
        return periodo


    def gestionar_sistema(self):
        return "Sistema gestionado correctamente."