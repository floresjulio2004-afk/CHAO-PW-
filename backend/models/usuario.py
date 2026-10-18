from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, id_usuario, nombre, cedula, correo, contrasena):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__cedula = cedula
        self.__correo = correo
        self.__contrasena = contrasena


    @property
    def id_usuario(self):
        return self.__id_usuario


    @property
    def nombre(self):
        return self.__nombre


    @nombre.setter
    def nombre(self, nombre):
        if nombre.strip() == "":
            raise ValueError ("El nombre no puede quedar vacío")
        self.__nombre = nombre


    @property
    def cedula(self):
        return self.__cedula


    @property
    def correo(self):
        return self.__correo


    @correo.setter
    def correo(self, correo):
        if "@" not in correo:
            raise ValueError ("El correo debe contener @")
        self.__correo = correo


    @property
    def contrasena(self):
        return self.__contrasena


    @abstractmethod
    def editar_perfil(self):
        pass