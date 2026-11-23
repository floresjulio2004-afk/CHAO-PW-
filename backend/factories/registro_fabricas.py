from factories.creador_usuario import CreadorUsuario
from factories.fabrica_administrador import FabricaAdministrador
from factories.fabrica_coordinador import FabricaCoordinador
from factories.fabrica_docente import FabricaDocente
from factories.fabrica_estudiante import FabricaEstudiante


class RegistroFabricas:
    def __init__(self):
        self.__fabricas = {}


    def registrar(self, rol, fabrica):
        if not isinstance(rol, str) or not rol.strip():
            raise ValueError("El rol no puede quedar vacío.")
        if not isinstance(fabrica, CreadorUsuario):
            raise TypeError("La fábrica debe implementar CreadorUsuario.")
        self.__fabricas[rol.strip().lower()] = fabrica


    def obtener(self, rol):
        if not isinstance(rol, str) or rol.strip().lower() not in self.__fabricas:
            raise ValueError("El rol seleccionado no es válido.")
        return self.__fabricas[rol.strip().lower()]


    def roles(self):
        return list(self.__fabricas)


    @classmethod
    def por_defecto(cls):
        registro = cls()
        registro.registrar("estudiante", FabricaEstudiante())
        registro.registrar("docente", FabricaDocente())
        registro.registrar("coordinador", FabricaCoordinador())
        registro.registrar("administrador", FabricaAdministrador())
        return registro