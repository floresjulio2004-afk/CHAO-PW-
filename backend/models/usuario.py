from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, id_usuario, nombre, cedula, correo, contrasena):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__cedula = cedula
        self.__correo = correo
        self.__contrasena = contrasena

    @abstractmethod
    def iniciar_sesion(self):
        pass


    @abstractmethod
    def editar_perfil(self):
        pass


    @abstractmethod
    def cerrar_sesion(self):
        pass