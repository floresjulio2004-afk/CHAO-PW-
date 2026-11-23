import inspect
from datetime import date
from repositories.almacen_json import AlmacenJson
from repositories.catalogo_repository import CatalogoRepository


class CatalogoJsonRepository(CatalogoRepository):
    def __init__(self, ruta_archivo, clave, clase, campo_id):
        self.__almacen = AlmacenJson(ruta_archivo, dict)
        self.__clave = clave
        self.__clase = clase
        self.__campo_id = campo_id
        self.__campos = [
            nombre
            for nombre in inspect.signature(clase.__init__).parameters
            if nombre != "self"
        ]


    def __a_diccionario(self, registro):
        diccionario = {}
        for campo in self.__campos:
            valor = getattr(registro, campo)
            if isinstance(valor, date):
                valor = valor.isoformat()
            diccionario[campo] = valor
        return diccionario


    def obtener_todos(self):
        datos = self.__almacen.leer()
        return [
            self.__clase(**registro)
            for registro in datos.get(self.__clave, [])
        ]


    def obtener_por_id(self, id_registro):
        if id_registro is None:
            return None
        id_registro = str(id_registro).strip()
        return next(
            (
                registro for registro in self.obtener_todos()
                if str(getattr(registro, self.__campo_id)) == id_registro
            ),
            None
        )


    def guardar(self, registro):
        if not isinstance(registro, self.__clase):
            raise TypeError(f"El registro debe ser un objeto {self.__clase.__name__}.")
        datos = self.__almacen.leer()
        registros = datos.setdefault(self.__clave, [])
        nuevo = self.__a_diccionario(registro)
        if any(
            str(existente.get(self.__campo_id)) == str(nuevo[self.__campo_id])
            for existente in registros
        ):
            raise ValueError("Ya existe un registro con ese ID.")
        registros.append(nuevo)
        self.__almacen.guardar(datos)
        return registro

    
    def actualizar(self, id_registro, registro):
        if not isinstance(registro, self.__clase):
            raise TypeError(f"El registro debe ser un objeto {self.__clase.__name__}.")
        id_registro = str(id_registro).strip()
        if str(getattr(registro, self.__campo_id)) != id_registro:
            raise ValueError("El ID de un registro no se puede cambiar.")
        datos = self.__almacen.leer()
        registros = datos.get(self.__clave, [])
        for indice, existente in enumerate(registros):
            if str(existente.get(self.__campo_id)) == id_registro:
                registros[indice] = self.__a_diccionario(registro)
                self.__almacen.guardar(datos)
                return registro
        return None


    def eliminar(self, id_registro):
        id_registro = str(id_registro).strip()
        datos = self.__almacen.leer()
        registros = datos.get(self.__clave, [])
        restantes = [
            existente for existente in registros
            if str(existente.get(self.__campo_id)) != id_registro
        ]
        if len(restantes) == len(registros):
            return False
        datos[self.__clave] = restantes
        self.__almacen.guardar(datos)
        return True