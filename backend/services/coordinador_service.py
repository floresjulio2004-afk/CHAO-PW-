class CoordinadorService:
    def __init__(self, horario_repository, aula_repository, asignatura_repository, usuario_repository, paralelo_repository, periodo_repository, horario_service):
        self.__horario_repository = horario_repository
        self.__aula_repository = aula_repository
        self.__asignatura_repository = asignatura_repository
        self.__usuario_repository = usuario_repository
        self.__paralelo_repository = paralelo_repository
        self.__periodo_repository = periodo_repository
        self.__horario_service = horario_service

    # GESTIÓN DE HORARIOS
    def crear_horario(self, horario):
        pass


    def consultar_horarios(self):
        pass


    def modificar_horario(self, id_horario, datos):
        pass


    def eliminar_horario(self, id_horario):
        pass

    # GESTIÓN DE AULAS
    def crear_aula(self, aula):
        pass

    def consultar_aulas(self):
        pass

    def modificar_aula(self, id_aula, datos):
        pass

    def eliminar_aula(self, id_aula):
        pass

    # GESTIÓN DE ASIGNATURAS
    def crear_asignatura(self, asignatura):
        pass

    def consultar_asignaturas(self):
        pass

    def modificar_asignatura(self, id_asignatura, datos):
        pass

    def eliminar_asignatura(self, id_asignatura):
        pass

    # GESTIÓN DE DOCENTES
    def crear_docente(self, docente):
        pass

    def consultar_docentes(self):
        pass

    def modificar_docente(self, id_docente, datos):
        pass

    def eliminar_docente(self, id_docente):
        pass

    # GESTIÓN DE PARALELOS
    def crear_paralelo(self, paralelo):
        pass

    def consultar_paralelos(self):
        pass

    def modificar_paralelo(self, id_paralelo, datos):
        pass

    def eliminar_paralelo(self, id_paralelo):
        pass

    # GESTIÓN DE PERIODOS ACADÉMICOS
    def crear_periodo(self, periodo):
        pass

    def consultar_periodos(self):
        pass

    def modificar_periodo(self, id_periodo, datos):
        pass

    def eliminar_periodo(self, id_periodo):
        pass

    # GENERACIÓN DE HORARIOS
    def generar_horario(self, datos):
        pass