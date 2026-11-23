from abc import ABC, abstractmethod


class CreadorUsuario(ABC):
    @abstractmethod
    def crear_usuario(self, nombre, cedula, correo, contrasena_hash, **datos):
        pass