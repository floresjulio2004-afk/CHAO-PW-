from models.usuario import Usuario
from factories.creador_usuario import CreadorUsuario


class AdministradorService:
    def __init__(self, usuario_repository, facultad_repository, carrera_repository, nivel_repository, paralelo_repository):
        self.__usuario_repository = usuario_repository
        self.__facultad_repository = facultad_repository
        self.__carrera_repository = carrera_repository
        self.__nivel_repository = nivel_repository
        self.__paralelo_repository = paralelo_repository
        self.__referencias = {
            "id_carrera": ("carrera", carrera_repository),
            "id_nivel": ("nivel", nivel_repository),
            "id_paralelo": ("paralelo", paralelo_repository)
        }


    def crear_usuario(self, usuario):
        if not isinstance(usuario, Usuario):
            raise TypeError("El usuario debe ser un objeto de tipo Usuario.")
        self.__validar_referencias(usuario.datos_adicionales())
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


    def consultar_usuarios_con_detalle(self):
        facultades = {
            facultad.id_facultad: facultad.nombre
            for facultad in self.__facultad_repository.obtener_todos()
        }
        carreras = {
            carrera.id_carrera: f"{carrera.nombre} ({facultades.get(carrera.id_facultad, 'Sin facultad')})"
            for carrera in self.__carrera_repository.obtener_todos()
        }
        niveles = {
            nivel.id_nivel: nivel.nombre
            for nivel in self.__nivel_repository.obtener_todos()
        }
        paralelos = {
            paralelo.id_paralelo: paralelo.nombre
            for paralelo in self.__paralelo_repository.obtener_todos()
        }
        vistas = []
        for usuario in self.__usuario_repository.obtener_todos():
            vista = {
                campo: valor
                for campo, valor in usuario.items()
                if campo != "contrasena_hash"
            }
            vista["detalle"] = self.__detalle(usuario, carreras, niveles, paralelos)
            vistas.append(vista)
        return vistas


    def modificar_usuario(self, id_usuario, datos):
        return self.__usuario_repository.actualizar(id_usuario, datos)


    def eliminar_usuario(self, id_usuario):
        return self.__usuario_repository.eliminar(id_usuario)


    def consultar_facultades(self):
        return self.__facultad_repository.obtener_todos()


    def consultar_carreras(self):
        return self.__carrera_repository.obtener_todos()


    def consultar_niveles(self):
        return self.__nivel_repository.obtener_todos()

    
    def consultar_paralelos(self):
        return self.__paralelo_repository.obtener_todos()


    def __validar_referencias(self, datos):
        for campo, (nombre, repositorio) in self.__referencias.items():
            if campo in datos and repositorio.obtener_por_id(datos[campo]) is None:
                raise ValueError(f"La opción elegida para {nombre} no existe.")

    
    @staticmethod
    def __detalle(usuario, carreras, niveles, paralelos):
        if usuario.get("rol") == "estudiante":
            return " · ".join([
                carreras.get(usuario.get("id_carrera"), "Sin carrera"),
                niveles.get(usuario.get("id_nivel"), "Sin nivel"),
                f"Paralelo {paralelos.get(usuario.get('id_paralelo'), '—')}"
            ])
        return usuario.get("especialidad", "—")