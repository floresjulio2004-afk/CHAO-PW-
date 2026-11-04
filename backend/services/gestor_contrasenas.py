from werkzeug.security import (generate_password_hash, check_password_hash)


class GestorContrasenas:
    @staticmethod
    def generar_hash(contrasena):
        if not isinstance(contrasena, str) or not contrasena:
            raise ValueError("La contraseña no puede quedar vacía.")
        return generate_password_hash(contrasena)


    @staticmethod
    def verificar_contrasena(contrasena, hash_guardado):
        if not isinstance(contrasena, str) or not contrasena:
            return False
        if not isinstance(hash_guardado, str) or not hash_guardado:
            return False
        try:
            return check_password_hash(hash_guardado, contrasena)
        except (ValueError, TypeError):
            return False