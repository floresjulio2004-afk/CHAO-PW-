from abc import ABC, abstractmethod


class HorarioRepository(ABC):
    @abstractmethod
    def obtener_todos(self):
        pass


    @abstractmethod
    def obtener_por_id(self, id_horario):
        pass


    @abstractmethod
    def obtener_por_estudiante(self, id_estudiante):
        pass


    @abstractmethod
    def obtener_inscritos(self, id_horario):
        pass


    @abstractmethod
    def guardar(self, horario, ids_estudiantes=()):
        pass


    @abstractmethod
    def eliminar(self, id_horario):
        pass