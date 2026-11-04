from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, id_usuario, nombre, cedula, correo, contrasena_hash, rol):
        self.__id_usuario = id_usuario
        self.nombre = nombre
        self.cedula = cedula
        self.correo = correo
        self.__contrasena_hash = contrasena_hash
        self.__rol = rol
        self.tema = "claro"


    @property
    def id_usuario(self):
        return self.__id_usuario


    @property
    def nombre(self):
        return self.__nombre


    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede quedar vacío.")
        self.__nombre = nombre.strip()


    @property
    def cedula(self):
        return self.__cedula


    @cedula.setter
    def cedula(self, cedula):
        if not isinstance(cedula, str) or not cedula.strip():
            raise ValueError("La cédula no puede quedar vacía.")
        self.__cedula = cedula.strip()

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, correo):
        if not isinstance(correo, str):
            raise ValueError("El correo debe ser un texto válido.")
        correo = correo.strip().lower()
        if not correo or "@" not in correo:
            raise ValueError("El correo debe contener @.")
        self.__correo = correo


    @property
    def contrasena_hash(self):
        return self.__contrasena_hash


    @property
    def rol(self):
        return self.__rol


    @property
    def tema(self):
        return self.__tema


    @tema.setter
    def tema(self, tema):
        if not isinstance(tema, str):
            raise ValueError("El tema debe ser un texto válido.")
        tema = tema.strip().lower()
        if tema not in ("claro", "oscuro"):
            raise ValueError("El tema debe ser claro u oscuro.")
        self.__tema = tema


    @abstractmethod
    def personalizar_interfaz(self, tema):
        pass