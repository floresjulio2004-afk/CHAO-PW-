from pathlib import Path
from models.usuario import Usuario
from repositories.almacen_json import AlmacenJson
from repositories.usuario_repository import UsuarioRepository


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
        self.__almacen = AlmacenJson(ruta_archivo, list)


    def obtener_todos(self):
        return self.__almacen.leer()


    def obtener_por_id(self, id_usuario):
        return next(
            (
                usuario for usuario in self.__almacen.leer()
                if usuario.get("id_usuario") == id_usuario
            ),
            None
        )


    def obtener_por_correo(self, correo):
        if not isinstance(correo, str):
            return None
        correo = correo.strip().lower()
        return next(
            (
                usuario for usuario in self.__almacen.leer()
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
            usuario_guardado.update(usuario.datos_adicionales())
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
        usuarios = self.__almacen.leer()
        correo = usuario_guardado["correo"].strip().lower()
        if any(
            u.get("correo", "").strip().lower() == correo
            for u in usuarios
            if isinstance(u.get("correo"), str)
        ):
            raise ValueError("Ya existe un usuario con ese correo.")
        cedula = usuario_guardado["cedula"].strip()
        if any(u.get("cedula") == cedula for u in usuarios):
            raise ValueError("Ya existe un usuario con esa cédula.")
        id_usuario = usuario_guardado["id_usuario"].strip()
        if any(u.get("id_usuario") == id_usuario for u in usuarios):
            raise ValueError("Ya existe un usuario con ese ID.")
        usuario_guardado["correo"] = correo
        usuario_guardado["cedula"] = cedula
        usuario_guardado["id_usuario"] = id_usuario
        usuarios.append(usuario_guardado)
        self.__almacen.guardar(usuarios)
        return usuario_guardado


    def actualizar(self, id_usuario, datos):
        if not isinstance(datos, dict):
            raise TypeError("Los datos deben ser un diccionario.")
        campos_protegidos = self.CAMPOS_PROTEGIDOS.intersection(datos)
        if campos_protegidos:
            raise ValueError(
                "No se pueden modificar estos campos: "
                + ", ".join(sorted(campos_protegidos))
            )
        usuarios = self.__almacen.leer()
        for indice, usuario in enumerate(usuarios):
            if usuario.get("id_usuario") == id_usuario:
                usuario_actualizado = {**usuario, **datos}
                correo = usuario_actualizado.get("correo")
                if not isinstance(correo, str) or not correo.strip():
                    raise ValueError("El correo debe ser válido.")
                correo = correo.strip().lower()
                if any(
                    otro.get("correo", "").strip().lower() == correo
                    for posicion, otro in enumerate(usuarios)
                    if posicion != indice
                    and isinstance(otro.get("correo"), str)
                ):
                    raise ValueError("Ya existe otro usuario con ese correo.")
                usuario_actualizado["correo"] = correo
                usuarios[indice] = usuario_actualizado
                self.__almacen.guardar(usuarios)
                return usuario_actualizado
        return None


    def eliminar(self, id_usuario):
        usuarios = self.__almacen.leer()
        restantes = [
            usuario for usuario in usuarios
            if usuario.get("id_usuario") != id_usuario
        ]
        if len(restantes) == len(usuarios):
            return False
        self.__almacen.guardar(restantes)
        return True