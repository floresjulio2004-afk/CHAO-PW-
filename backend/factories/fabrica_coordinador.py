from factories.creador_usuario import CreadorUsuario
from models.coordinador import Coordinador


class FabricaCoordinador(CreadorUsuario):
    def crear_usuario(self, nombre, cedula, correo, contrasena_hash, **datos):
        return Coordinador(
            nombre,
            cedula,
            correo,
            contrasena_hash
        )