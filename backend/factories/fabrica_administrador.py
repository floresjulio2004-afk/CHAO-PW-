from factories.creador_usuario import CreadorUsuario
from models.administrador import Administrador


class FabricaAdministrador(CreadorUsuario):
    def crear_usuario(self, nombre, cedula, correo, contrasena_hash, **datos):
        return Administrador(
            nombre,
            cedula,
            correo,
            contrasena_hash
        )