from factories.creador_usuario import CreadorUsuario
from models.docente import Docente


class FabricaDocente(CreadorUsuario):
    def crear_usuario(self, nombre, cedula, correo, contrasena_hash, **datos):
        if "especialidad" not in datos:
            raise ValueError("La especialidad del docente es obligatoria.")
        return Docente(
            nombre,
            cedula,
            correo,
            contrasena_hash,
            datos["especialidad"]
        )