from typing import Protocol
from models.autenticador import Autenticador


class UsuarioRepository(Protocol):
    def obtener_todos(self):
        ...


class GestorContrasenasProtocol(Protocol):
    def verificar_contrasena(self, contrasena, hash_guardado):
        ...


class AutenticacionService(Autenticador):
    def __init__(self, usuario_repository, gestor_contrasenas):
        if not callable(getattr(usuario_repository, "obtener_todos", None)):
            raise TypeError(
                "El repositorio debe implementar obtener_todos()."
            )
        if not callable(
            getattr(gestor_contrasenas, "verificar_contrasena", None)
        ):
            raise TypeError(
                "El gestor debe implementar verificar_contrasena()."
            )
        self.__usuario_repository = usuario_repository
        self.__gestor_contrasenas = gestor_contrasenas


    def autenticar(self, correo, contrasena):
        if not isinstance(correo, str) or not correo.strip():
            raise ValueError("El correo no puede quedar vacío.")
        if not isinstance(contrasena, str) or not contrasena:
            raise ValueError("La contraseña no puede quedar vacía.")
        correo = correo.strip().lower()
        usuarios = self.__usuario_repository.obtener_todos()
        if not isinstance(usuarios, list):
            raise ValueError(
                "El repositorio debe devolver una lista de usuarios."
            )
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
            if not isinstance(rol, str) or not rol.strip():
                break
            contrasena_correcta = (
                self.__gestor_contrasenas.verificar_contrasena(
                    contrasena,
                    contrasena_hash
                )
            )
            if not contrasena_correcta:
                break
            return {
                "nombre": usuario.get("nombre"),
                "cedula": usuario.get("cedula"),
                "correo": correo_guardado.strip().lower(),
                "rol": rol.strip().lower()
            }
        raise ValueError("Correo o contraseña incorrectos.")


    def iniciar_sesion(self, correo, contrasena):
        return self.autenticar(correo, contrasena)