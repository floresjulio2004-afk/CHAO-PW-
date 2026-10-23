class Carrera:
    def __init__(self, id_carrera, nombre, codigo):
        self.id_carrera = id_carrera
        self.nombre = nombre
        self.codigo = codigo

    @property
    def id_carrera(self):
        return self.__id_carrera

    @id_carrera.setter
    def id_carrera(self, id_carrera):
        id_carrera = str(id_carrera)
        if id_carrera.isdigit() and len(id_carrera) ==10:
            self.__id_carrera = id_carrera
        else:
            raise ValueError("ID inválida.")

    @property 
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre (self, nombre):
        nombre = str(nombre)
        if nombre.isalpha() and len(nombre) == 30:
            self.__nombre = nombre
        else:
            raise ValueError("El nombre de la carrera no puede estar vacío.")

    @property
    def codigo(self):
        return self.codigo 

    @codigo.setter
    def codigo(self, codigo):
        codigo = str(codigo)
        if codigo.isdigit() and len(codigo) ==3:
            self.__codigo = codigo
        else:
            raise ValueError("ID inválida.")

    # MÉTODOS
    
    def registrar(self):
        pass

    def actualizar(self):
        pass

    def consultar(self):
        pass