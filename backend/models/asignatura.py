class Asignatura:
    def __init__(self, id_asignatura, codigo, nombre, creditos):
        self.id_asignatura = id_asignatura
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos


    @property
    def id_asignatura(self):
        return self.__id_asignatura


    @id_asignatura.setter
    def id_asignatura(self, id_asignatura):
        if id_asignatura is None or not str(id_asignatura).strip():
            raise ValueError("El ID de la asignatura no puede quedar vacío.")
        self.__id_asignatura = str(id_asignatura).strip()


    @property
    def codigo(self):
        return self.__codigo


    @codigo.setter
    def codigo(self, codigo):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El código de la asignatura no puede quedar vacío.")
        self.__codigo = codigo.strip()


    @property
    def nombre(self):
        return self.__nombre


    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre de la asignatura no puede quedar vacío.")
        self.__nombre = nombre.strip()


    @property
    def creditos(self):
        return self.__creditos


    @creditos.setter
    def creditos(self, creditos):
        if type(creditos) is not int or creditos <= 0:
            raise ValueError("Los créditos deben ser un número entero positivo.")
        self.__creditos = creditos