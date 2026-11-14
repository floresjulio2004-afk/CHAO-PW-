import json
from pathlib import Path
from repositories.catalogo_repository import CatalogoRepository


class CatalogoJsonRepository(CatalogoRepository):
    def __init__(self, ruta_archivo, clave, clase, campo_id):
        self.__ruta_archivo = Path(ruta_archivo)
        self.__clave = clave
        self.__clase = clase
        self.__campo_id = campo_id


    def __leer_archivo(self):
        if not self.__ruta_archivo.exists():
            raise FileNotFoundError(
                f"No se encontró el archivo: {self.__ruta_archivo}"
            )
        with open(self.__ruta_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        if not isinstance(datos, dict):
            raise ValueError(
                "El archivo de catálogos debe contener un objeto."
            )
        return [
            self.__clase(**registro)
            for registro in datos.get(self.__clave, [])
        ]


    def obtener_todos(self):
        return self.__leer_archivo()


    def obtener_por_id(self, id_registro):
        if id_registro is None:
            return None
        id_registro = str(id_registro).strip()
        return next(
            (
                registro for registro in self.__leer_archivo()
                if getattr(registro, self.__campo_id) == id_registro
            ),
            None
        )