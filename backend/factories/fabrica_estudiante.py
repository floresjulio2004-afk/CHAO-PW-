from factories.creador_usuario import CreadorUsuario
from models.estudiante import Estudiante


class FabricaEstudiante(CreadorUsuario):
    def crear_usuario(self, nombre, cedula, correo, contrasena_hash, **datos):
        if "nivel" not in datos:
            raise ValueError("El nivel del estudiante es obligatorio.")
        return Estudiante(
            nombre,
            cedula,
            correo,
            contrasena_hash,
            datos["nivel"]
        )