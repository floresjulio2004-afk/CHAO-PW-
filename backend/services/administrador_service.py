from models.usuario import Usuario
from factories.creador_usuario import CreadorUsuario


class AdministradorService:
    def __init__(self, usuario_repository, rol_repository, facultad_repository, carrera_repository, nivel_educativo_repository, configuracion_repository, sistema_service):
        self.__usuario_repository = usuario_repository
        self.__rol_repository = rol_repository
        self.__facultad_repository = facultad_repository
        self.__carrera_repository = carrera_repository
        self.__nivel_educativo_repository = nivel_educativo_repository
        self.__configuracion_repository = configuracion_repository
        self.__sistema_service = sistema_service

    # GESTIÓN DE USUARIOS
    def crear_usuario(self, usuario):
        if not isinstance(usuario, Usuario):
            raise TypeError("El usuario debe ser un objeto de tipo Usuario.")
        return self.__usuario_repository.guardar(usuario)

        
    def crear_usuario_desde_fabrica(self, fabrica, nombre, cedula, correo, contrasena_hash, **datos):
        if not isinstance(fabrica, CreadorUsuario):
            raise TypeError("La fábrica debe implementar CreadorUsuario.")
        usuario = fabrica.crear_usuario(
            nombre,
            cedula,
            correo,
            contrasena_hash,
            **datos
        )
        return self.crear_usuario(usuario)


    def consultar_usuarios(self):
        return self.__usuario_repository.obtener_todos()


    def modificar_usuario(self, id_usuario, datos):
        return self.__usuario_repository.actualizar(id_usuario, datos)


    def eliminar_usuario(self, id_usuario):
        return self.__usuario_repository.eliminar(id_usuario)

    # GESTIÓN DE ROLES
    def crear_rol(self, rol):
        pass


    def consultar_roles(self):
        pass


    def modificar_rol(self, id_rol, datos):
        pass


    def eliminar_rol(self, id_rol):
        pass

    # GESTIÓN DE FACULTADES
    def crear_facultad(self, facultad):
        pass


    def consultar_facultades(self):
        pass


    def modificar_facultad(self, id_facultad, datos):
        pass


    def eliminar_facultad(self, id_facultad):
        pass

    # GESTIÓN DE CARRERAS
    def crear_carrera(self, carrera):
        pass


    def consultar_carreras(self):
        pass


    def modificar_carrera(self, id_carrera, datos):
        pass


    def eliminar_carrera(self, id_carrera):
        pass

    # GESTIÓN DE NIVELES EDUCATIVOS
    def crear_nivel_educativo(self, nivel):
        pass


    def consultar_niveles_educativos(self):
        pass


    def modificar_nivel_educativo(self, id_nivel, datos):
        pass


    def eliminar_nivel_educativo(self, id_nivel):
        pass

    # GESTIÓN DE CONFIGURACIÓN
    def consultar_configuracion(self):
        pass


    def modificar_configuracion(self, datos):
        pass

    # INFORMACIÓN GENERAL DEL SISTEMA
    def consultar_informacion_sistema(self):
        pass