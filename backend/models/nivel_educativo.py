class nivel_educativo:
    tipo = "tercer nivel educativo"

        def __init__(self, id_nivel, nombre, tipo):
            self.id_nivel = id_nivel
            self.nombre = nombre
            self.tipo = tipo

        def mostrar_datos(self):    
            print(f"ID: {self.id_nivel}")
            print(f"Nombre: {self.nombre}")
            print(f"Tipo: {self.tipo}")
        
        def consultar_nivel(self):
            pass    
        @classmethod
        def mostrar_tipo(cls):
            print(f"Tipo de nivel educativo: {cls.tipo}")   
        @staticmethod
        def mostrar_mensaje():
            print("Este es un nivel educativo") 
        
    nivel1 = nivel_educativo(1, "Ingenieria de Sistemas", "tercer nivel educativo")
    nivel_educativo.mostrar_tipo()
    nivel_educativo.mostrar_mensaje()
    nivel1.mostrar_datos()
    print(type(nivel1))