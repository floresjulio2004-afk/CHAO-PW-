from models.autenticador import Autenticador
from repositories.usuario_repository import UsuarioRepository


class AutenticacionService(Autenticador):
    def __init__(self, usuario_repository, gestor_contrasenas):
        if not callable(
            getattr(usuario_repository, "obtener_por_correo", None)
        ):
            raise TypeError(
                "El repositorio debe implementar obtener_por_correo()."
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
        usuario = self.__usuario_repository.obtener_por_correo(correo)
        if not isinstance(usuario, dict):
            raise ValueError("Correo o contraseña incorrectos.")
        contrasena_hash = usuario.get("contrasena_hash")
        if not isinstance(contrasena_hash, str) or not contrasena_hash:
            raise ValueError("Correo o contraseña incorrectos.")
        contrasena_correcta = (
            self.__gestor_contrasenas.verificar_contrasena(
                contrasena,
                contrasena_hash
            )
        )
        if not contrasena_correcta:
            raise ValueError("Correo o contraseña incorrectos.")
        return {
            "id": usuario.get("id_usuario"),
            "nombre": usuario.get("nombre"),
            "cedula": usuario.get("cedula"),
            "correo": correo,
            "rol": usuario.get("rol", "").strip().lower()
        }


    def iniciar_sesion(self, correo, contrasena):
        return self.autenticar(correo, contrasena)