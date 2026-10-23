class Facultad():
    def __init__(self, id_facultad, nombre):
        self.id_facultad = id_facultad
        self.nombre = nombre

    @property
    def id_facultad(self):
        return self.id_facultad

    @id_facultad.setter
    def id_facultad(self, id_facultad):
        id_facultad = str(id_facultad)
        if id_facultad.isalpha() and len(id_facultad) == 10:
            self__id_facultad = id_facultad
        else:
            raise ValueError("El ID ingresado no existe.")

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nombre):
        nombre = str(nombre)
        if nombre.isalpha() and len(nombre) == 50:
            self__nomnre = nombre
        else:
            raise ValueError("El nombre de la facultad es incorrecto.")
        
    # MÉTODOS

    def registrar(self):
        pass

    def actualizar(self):
        pass

    def consultar(self):
        pass