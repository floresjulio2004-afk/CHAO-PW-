from factories.creador_usuario import CreadorUsuario
from models.estudiante import Estudiante


class FabricaEstudiante(CreadorUsuario):
    CAMPOS_OBLIGATORIOS = ("id_carrera", "id_nivel", "id_paralelo")
    
    
    def crear_usuario(self, nombre, cedula, correo, contrasena_hash, **datos):
        if any(not datos.get(campo) for campo in self.CAMPOS_OBLIGATORIOS):
            raise ValueError("La carrera, el nivel y el paralelo del estudiante son obligatorios.")
        return Estudiante(
            nombre,
            cedula,
            correo,
            contrasena_hash,
            datos["id_carrera"],
            datos["id_nivel"],
            datos["id_paralelo"]
        )