from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, id_usuario, nombre, cedula, correo, contrasena_hash):
        self.__id_usuario = id_usuario
        self.nombre = nombre
        self.__cedula = cedula
        self.correo = correo
        self.__contrasena_hash = contrasena_hash


    @property
    def id_usuario(self):
        return self.__id_usuario


    @property
    def nombre(self):
        return self.__nombre


    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre no puede quedar vacío")
        self.__nombre = nombre.strip()


    @property
    def cedula(self):
        return self.__cedula


    @property
    def correo(self):
        return self.__correo


    @correo.setter
    def correo(self, correo):
        if not isinstance(correo, str) or "@" not in correo:
            raise ValueError("El correo debe contener @")
        self.__correo = correo.strip()


    @property
    def contrasena_hash(self):
        return self.__contrasena_hash


    @abstractmethod
    def editar_perfil(self, vista_horario):
        pass