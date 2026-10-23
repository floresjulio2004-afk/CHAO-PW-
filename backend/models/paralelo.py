class Paralelo:
    def __init__(self, id_nivel, nombre, descripcion):
        self.id_nivel = id_nivel
        self.nombre = nombre
        self.descripcion = descripcion

    @property
    def id_nivel(self):
        return self.id_nivel

    @id_nivel.setter
    def id_nivel(self, id_nivel):
        id_nivel = str(id_nivel)
        if id_nivel.isalpha() and len(id_nivel) == 10:
            self__id_facultad = id_nivel
        else:
            raise ValueError("El ID ingresado no existe.")
        
    @property
    def nombre (self):
        return self.nombre
    
    @nombre.setter
    def nombre (self, nombre):
        nombre = str(nombre)
        if nombre.isalpha() and len(nombre) == 1:
            self.__nombre = nombre
        else:
            raise ValueError("Nivel ingresado no válido.")


    @property
    def descripcion(self):
        return self.descripcion

    @descripcion.setter
    def descripcion (self, descripcion):
        descripcion= str(descripcion)
        if len(descripcion) == 300:
            self.__nombre = descripcion
        else:
            raise ValueError("Descipción inválida.")


    # MÉTODOS

    def registrar(self):
        pass

    def actualizar(self):
        pass

    def consultar(self):
        pass