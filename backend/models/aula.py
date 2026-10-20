class Aula:
    def __init__(self, id_aula, nombre, capacidad, tipo):
        self.id_aula = id_aula
        self.nombre = nombre
        self.capacidad = capacidad
        self.tipo = tipo
        self.__disponibilidad = True

    @property
    def id_aula(self):
        return self.__id_aula

    @id_aula.setter
    def id_aula(self, id_aula):
        id_aula = str(id_aula)
        if id_aula.isdigit() and len(id_aula) ==3:
            self.__id_aula = id_aula
        else:
            raise ValueError("ID inválida.")

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str) or nombre.strip() == "": 
            raise ValueError("El aula no está identificada.")
        else:
            self.__nombre = nombre

    @property
    def capacidad(self):
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, capacidad):
        if isinstance(capacidad, int) and 1 <= capacidad <= 40:
            self.__capacidad = capacidad
        else:
            raise ValueError("El aula ha superado el límite de capacidad.")

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        if not isinstance(tipo, str) or tipo.strip() == "":
            raise ValueError("Tipo de aula inválido.")
        self.__tipo = tipo.strip()
     

    @property
    def disponibilidad(self):
        return self.__disponibilidad

    def registrar(self):
        print("Aula registrada.")

    def actualizar(self):
        print("Aula actualizada.")

    def eliminar(self):
        print("Aula eliminada")

aula1 = Aula("131", "Laboratorio de Informática", 35, "Laboratorio")

print(aula1.id_aula)
print(aula1.nombre)
print(aula1.capacidad)
print(aula1.tipo)
print(aula1.disponibilidad)

aula1.registrar()
