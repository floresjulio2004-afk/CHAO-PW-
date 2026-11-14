from abc import ABC, abstractmethod


class CatalogoRepository(ABC):
    @abstractmethod
    def obtener_todos(self):
        pass


    @abstractmethod
    def obtener_por_id(self, id_registro):
        pass