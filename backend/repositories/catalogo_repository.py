from abc import ABC, abstractmethod


class CatalogoRepository(ABC):
    @abstractmethod
    def obtener_todos(self):
        pass


    @abstractmethod
    def obtener_por_id(self, id_registro):
        pass


    @abstractmethod
    def guardar(self, registro):
        pass


    @abstractmethod
    def actualizar(self, id_registro, registro):
        pass


    @abstractmethod
    def eliminar(self, id_registro):
        pass