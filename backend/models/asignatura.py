class Asignatura:
    def __init__(self, id, codigo, nombre, creditos, hora):

        self.id = id
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.hora = hora    
    def mostrar_datos(self):
        print(f"ID: {self.id}")
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Créditos: {self.creditos}")
        print(f"Hora: {self.hora}")
    def consultar_docente(self):
        pass    
    @classmethod
    def mostrar_tipo(cls):
        print(f"Tipo de asignatura: {cls.tipo}")
    @staticmethod
    def mostrar_mensaje():
        print("Esta es una asignatura académica")
    aignatura1 = asignatura(1, "MAT101", "POO", 3, "13.:00-16:00")
    Asignatura.mostrar_tipo()
    Asignatura.mostrar_mensaje()
    print(type(asignatura1))
