from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)


class GestorContrasenas:

    @staticmethod
    def generar_hash(contrasena):
        return generate_password_hash(contrasena)

    @staticmethod
    def verificar_contrasena(contrasena, hash_guardado):
        return check_password_hash(hash_guardado, contrasena)