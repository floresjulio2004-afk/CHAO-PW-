from abc import ABC, abstractmethod


class Autenticador(ABC):
    @abstractmethod
    def iniciar_sesion(self, correo, contrasena):
        pass


    @abstractmethod
    def cerrar_sesion(self):
        pass