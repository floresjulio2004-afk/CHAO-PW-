import json
from pathlib import Path
from werkzeug.security import check_password_hash
from models.autenticador import Autenticador


class AutenticacionService(Autenticador):
    ROLES_VALIDOS = {
        "estudiante",
        "docente",
        "gestor",
        "administrador"
    }


    def __init__(self, ruta_usuarios=None):
        if ruta_usuarios is None:
            ruta_usuarios = (
                Path(__file__).resolve().parents[1]
                / "data"
                / "usuarios.json"
            )
        self.__ruta_usuarios = Path(ruta_usuarios)


    def iniciar_sesion(self, correo, contrasena):
        if not isinstance(correo, str) or not correo.strip():
            raise ValueError("El correo no puede quedar vacío")
        if not isinstance(contrasena, str) or not contrasena:
            raise ValueError("La contraseña no puede quedar vacía")
        correo = correo.strip().lower()
        usuarios = self.__cargar_usuarios()
        for usuario in usuarios:
            if not isinstance(usuario, dict):
                continue
            correo_guardado = usuario.get("correo")
            contrasena_hash = usuario.get("contrasena_hash")
            rol = usuario.get("rol")
            if not isinstance(correo_guardado, str):
                continue
            if correo_guardado.strip().lower() != correo:
                continue
            if not isinstance(contrasena_hash, str):
                break
            if not isinstance(rol, str) or rol not in self.ROLES_VALIDOS:
                break
            try:
                contrasena_correcta = check_password_hash(
                    contrasena_hash,
                    contrasena
                )
            except (ValueError, TypeError):
                contrasena_correcta = False
            if not contrasena_correcta:
                break
            return {
                "nombre": usuario.get("nombre"),
                "cedula": usuario.get("cedula"),
                "correo": correo_guardado,
                "rol": rol
            }
        raise ValueError("Correo o contraseña incorrectos")


    def cerrar_sesion(self, sesion):
        sesion.clear()
        return "Sesión cerrada correctamente."


    def __cargar_usuarios(self):
        if not self.__ruta_usuarios.is_file():
            raise FileNotFoundError(
                f"No se encontró el archivo: {self.__ruta_usuarios}"
            )
        try:
            with self.__ruta_usuarios.open(
                "r",
                encoding="utf-8"
            ) as archivo:
                usuarios = json.load(archivo)
        except json.JSONDecodeError as error:
            raise ValueError(
                "El archivo de usuarios contiene JSON inválido"
            ) from error
        if not isinstance(usuarios, list):
            raise ValueError(
                "El archivo JSON debe contener una lista de usuarios"
            )
        return usuarios