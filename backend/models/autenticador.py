from abc import ABC, abstractmethod


class Autenticador(ABC):
    @abstractmethod
    def autenticar(self, correo, contrasena):
        pass