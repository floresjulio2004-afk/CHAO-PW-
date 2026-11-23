from abc import ABC, abstractmethod


class HorarioRepository(ABC):
    @abstractmethod
    def obtener_todos(self):
        pass


    @abstractmethod
    def obtener_por_id(self, id_horario):
        pass


    @abstractmethod
    def obtener_por_paralelo(self, id_paralelo):
        pass


    @abstractmethod
    def obtener_por_docente(self, id_docente):
        pass


    @abstractmethod
    def guardar(self, horario):
        pass


    @abstractmethod
    def actualizar(self, horario):
        pass
    

    @abstractmethod
    def eliminar(self, id_horario):
        pass