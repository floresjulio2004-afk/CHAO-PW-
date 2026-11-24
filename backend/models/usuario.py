import uuid
import re
from abc import ABC, abstractmethod

class Usuario(ABC):
    TEMAS= ("claro","oscuro")

    def __init__(self, id_usuario, nombre, cedula, correo, contrasena_hash, rol):
        if id_usuario is None:
            id_usuario = f"USR-{uuid.uuid4()}"
        elif not isinstance(id_usuario, str) or not id_usuario.strip():
            raise ValueError("El ID del usuario no es válido.")
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
        self.__nombre=self.estructurar_nombre(nombre)

    @staticmethod
    def estructurar_nombre(nombre):
        if not isinstance(nombre,str)or not nombre.strip():
            raise ValueError("El campo NOMBRE no puede quedar vacío. Tiene que llenarlo.")
        return nombre.strip()

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, cedula):
        self.__cedula=self.validar_cedula(cedula)

    @staticmethod
    def validar_cedula(cedula):
        cedula=cedula.strip()if isinstance(cedula,str)else ""
        if not re.fullmatch (r"[0-9]{10}",cedula):
            raise ValueError("El campo CEDULA tiene que tener 10 caracteres numericos.")
        codigo=int(cedula[:2])
        if codigo not in range (1,25)and codigo != 30:
            raise ValueError("El codigo inicial de la cedula no es valida. Ingrese un codigo válido")
        productos=[int(digito)*(2-indice%2)for indice, digito in enumerate(cedula[:9])]
        suma=sum(producto -9 if producto > 9 else producto for producto in productos)
        if int (cedula[-1]!=(suma)%10):
            raise ValueError("El digito verificador de la cedula no es valida. Ingrese un codigo válido")
        return cedula
        
    @property
    def correo(self):
        return self.__correo


    @correo.setter
    def correo(self, correo):
        self.__correo=self.estructurar_correo

    @staticmethod
    def estructurar_correo(correo):
        correo=correo.strip().lower()if isinstance(correo,str)else ""
        if not re.fullmatch(r"[^@\s]+@[^@\s]+", correo):
            raise ValueError ("Los caracteres no coinciden, el correo no es válido. " \
            "Ingrese un correo válido.")

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
        self.__tema= self.estructurar_tema(tema)

    @classmethod
    def estructurar_tema(cls, tema):
        tema=tema.strip().lower()if isinstance(tema, str)else ""
        if tema not in cls.TEMAS:
            raise ValueError ("El tema debe ser CLARO o OSCURO")
        return tema

    def datos_adicionales(self):
        return {}

    @abstractmethod
    def personalizar_interfaz(self, tema):
        pass