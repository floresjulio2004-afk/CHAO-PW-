from abc import ABC, abstractmethod


class UsuarioRepository(ABC):
    @abstractmethod
    def obtener_todos(self):
        pass


    @abstractmethod
    def obtener_por_id(self, id_usuario):
        pass


    @abstractmethod
    def obtener_por_correo(self, correo):
        pass


    @abstractmethod
    def guardar(self, usuario):
        pass


    @abstractmethod
    def actualizar(self, id_usuario, datos):
        pass


    @abstractmethod
    def eliminar(self, id_usuario):
        pass