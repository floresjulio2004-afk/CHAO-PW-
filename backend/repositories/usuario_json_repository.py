import json
from pathlib import Path
from repositories.usuario_repository import UsuarioRepository
from models.usuario import Usuario


class UsuarioJsonRepository(UsuarioRepository):
    CAMPOS_PROTEGIDOS = {
        "id_usuario",
        "rol",
        "contrasena_hash"
    }


    def __init__(self, ruta_archivo=None):
        if ruta_archivo is None:
            ruta_archivo = (
                Path(__file__).resolve().parent.parent
                / "data"
                / "usuarios.json"
            )
        self.__ruta_archivo = Path(ruta_archivo)


    def __leer_archivo(self):
        if not self.__ruta_archivo.exists():
            raise FileNotFoundError(
                f"No se encontró el archivo: {self.__ruta_archivo}"
            )
        with open(self.__ruta_archivo, "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)
        if not isinstance(usuarios, list):
            raise ValueError(
                "El archivo de usuarios debe contener una lista."
            )
        return usuarios


    def __guardar_archivo(self, usuarios):
        with open(self.__ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(
                usuarios,
                archivo,
                ensure_ascii=False,
                indent=4
            )


    def obtener_todos(self):
        return self.__leer_archivo()


    def obtener_por_id(self, id_usuario):
        usuarios = self.__leer_archivo()
        return next(
            (
                usuario for usuario in usuarios
                if usuario.get("id_usuario") == id_usuario
            ),
            None
        )


    def obtener_por_correo(self, correo):
        if not isinstance(correo, str):
            return None
        correo = correo.strip().lower()
        usuarios = self.__leer_archivo()
        return next(
            (
                usuario for usuario in usuarios
                if isinstance(usuario.get("correo"), str)
                and usuario["correo"].strip().lower() == correo
            ),
            None
        )


    def guardar(self, usuario):
        if isinstance(usuario, Usuario):
            usuario_guardado = {
                "id_usuario": usuario.id_usuario,
                "nombre": usuario.nombre,
                "cedula": usuario.cedula,
                "correo": usuario.correo,
                "contrasena_hash": usuario.contrasena_hash,
                "rol": usuario.rol,
                "tema": usuario.tema
            }
            if usuario.rol == "estudiante":
                usuario_guardado["nivel"] = usuario.nivel
            elif usuario.rol == "docente":
                usuario_guardado["especialidad"] = usuario.especialidad
        elif isinstance(usuario, dict):
            usuario_guardado = usuario.copy()
        else:
            raise TypeError(
                "El usuario debe ser un objeto Usuario o un diccionario."
            )
        campos_obligatorios = (
            "id_usuario",
            "nombre",
            "cedula",
            "correo",
            "contrasena_hash",
            "rol"
        )
        for campo in campos_obligatorios:
            valor = usuario_guardado.get(campo)
            if not isinstance(valor, str) or not valor.strip():
                raise ValueError(
                    f"El campo {campo} no puede quedar vacío."
                )
        correo = usuario_guardado["correo"].strip().lower()
        usuario_guardado["correo"] = correo
        usuarios = self.__leer_archivo()
        if any(
            u.get("correo", "").strip().lower() == correo
            for u in usuarios
            if isinstance(u.get("correo"), str)
        ):
            raise ValueError(
                "Ya existe un usuario con ese correo."
            )
        cedula = usuario_guardado["cedula"].strip()
        if any(u.get("cedula") == cedula for u in usuarios):
            raise ValueError("Ya existe un usuario con esa cédula.")
        usuario_guardado["cedula"] = cedula  
        id_usuario = usuario_guardado["id_usuario"].strip()
        if any(
            u.get("id_usuario") == id_usuario
            for u in usuarios
        ):
            raise ValueError("Ya existe un usuario con ese ID.")
        usuario_guardado["id_usuario"] = id_usuario
        usuarios.append(usuario_guardado)
        self.__guardar_archivo(usuarios)
        return usuario_guardado


    def actualizar(self, id_usuario, datos):
        if not isinstance(datos, dict):
            raise TypeError(
                "Los datos deben ser un diccionario."
            )
        campos_protegidos = self.CAMPOS_PROTEGIDOS.intersection(datos)
        if campos_protegidos:
            raise ValueError(
                "No se pueden modificar estos campos: "
                + ", ".join(sorted(campos_protegidos))
            )
        usuarios = self.__leer_archivo()
        for indice, usuario in enumerate(usuarios):
            if usuario.get("id_usuario") == id_usuario:
                usuario_actualizado = {
                    **usuario,
                    **datos
                }
                correo = usuario_actualizado.get("correo")
                if not isinstance(correo, str) or not correo.strip():
                    raise ValueError(
                        "El correo debe ser válido."
                    )
                correo = correo.strip().lower()
                if any(
                    otro.get("correo", "").strip().lower() == correo
                    for posicion, otro in enumerate(usuarios)
                    if posicion != indice
                    and isinstance(otro.get("correo"), str)
                ):
                    raise ValueError(
                        "Ya existe otro usuario con ese correo."
                    )

                usuario_actualizado["correo"] = correo
                usuarios[indice] = usuario_actualizado
                self.__guardar_archivo(usuarios)
                return usuario_actualizado
        return None


    def eliminar(self, id_usuario):
        usuarios = self.__leer_archivo()
        usuarios_actualizados = [
            usuario for usuario in usuarios
            if usuario.get("id_usuario") != id_usuario
        ]
        if len(usuarios_actualizados) == len(usuarios):
            return False
        self.__guardar_archivo(usuarios_actualizados)
        return True