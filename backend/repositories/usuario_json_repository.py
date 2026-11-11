import json
import uuid
from pathlib import Path
from repositories.usuario_repository import UsuarioRepository
from models.usuario import Usuario


class UsuarioJsonRepository(UsuarioRepository):


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
            (usuario for usuario in usuarios
             if usuario.get("id_usuario") == id_usuario),
            None
        )


    def obtener_por_correo(self, correo):
        if not isinstance(correo, str):
            return None
        correo = correo.strip().lower()
        usuarios = self.__leer_archivo()
        return next(
            (usuario for usuario in usuarios
             if isinstance(usuario.get("correo"), str)
             and usuario["correo"].strip().lower() == correo),
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
            raise TypeError("El usuario debe ser un objeto Usuario o un diccionario.")
        correo = usuario_guardado.get("correo")
        if not isinstance(correo, str) or not correo.strip():
            raise ValueError("El usuario debe tener un correo válido.")
        usuarios = self.__leer_archivo()
        if any(
            isinstance(u.get("correo"), str)
            and u["correo"].strip().lower() == correo.strip().lower()
            for u in usuarios
        ):
            raise ValueError("Ya existe un usuario con ese correo.")
        id_usuario = usuario_guardado.get("id_usuario")
        if not isinstance(id_usuario, str) or not id_usuario.strip():
            id_usuario = f"USR-{uuid.uuid4()}"
            while any(u.get("id_usuario") == id_usuario for u in usuarios):
                id_usuario = f"USR-{uuid.uuid4()}"
            usuario_guardado["id_usuario"] = id_usuario
        elif any(u.get("id_usuario") == id_usuario for u in usuarios):
            raise ValueError("Ya existe un usuario con ese ID.")
        usuarios.append(usuario_guardado)
        self.__guardar_archivo(usuarios)
        return usuario_guardado


    def actualizar(self, id_usuario, datos):
        if not isinstance(datos, dict):
            raise TypeError("Los datos deben ser un diccionario.")
        usuarios = self.__leer_archivo()
        for indice, usuario in enumerate(usuarios):
            if usuario.get("id_usuario") == id_usuario:
                usuario_actualizado = {**usuario, **datos}
                if usuario_actualizado.get("id_usuario") != id_usuario:
                    raise ValueError("No se puede cambiar el ID del usuario.")
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