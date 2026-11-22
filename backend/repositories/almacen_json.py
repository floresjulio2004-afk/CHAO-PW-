import json
import os
import tempfile
from pathlib import Path


class AlmacenJson:
    def __init__(self, ruta_archivo, tipo):
        self.__ruta = Path(ruta_archivo)
        self.__tipo = tipo

    
    def leer(self):
        if not self.__ruta.exists():
            return self.__tipo()
        with open(self.__ruta, "r", encoding = "utf-8") as archivo:
            datos = json.load(archivo)
        if not isinstance(datos, self.__tipo):
            raise ValueError(f"El archivo {self.__ruta.name} tiene un formato inválido.")
        return datos


    def guardar(self, datos):
        self.__ruta.parent.mkdir(parents = True, exist_ok = True)
        descriptor, ruta_temporal = tempfile.mkstemp(
            dir = self.__ruta.parent,
            suffix = ".tmp"
        )
        try:
            with os.fdopen(descriptor, "w", encoding = "utf-8") as archivo:
                json.dump(datos, archivo, ensure_ascii = False, indent = 4)
            os.replace(ruta_temporal, self.__ruta)
        except Exception:
            if os.path.exists(ruta_temporal):
                os.unlink(ruta_temporal)
            raise