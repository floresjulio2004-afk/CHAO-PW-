class DocenteService:
    def __init__(self, horario_service, asignatura_repository, incidencia_service):
        self.__horario_service = horario_service
        self.__asignatura_repository = asignatura_repository
        self.__incidencia_service = incidencia_service


    def consultar_horario(self, id_docente):
        self.__validar_id(id_docente)
        return self.__horario_service.consultar_por_docente(id_docente)


    def consultar_asignatura(self, id_docente):
        self.__validar_id(id_docente)
        return self.__asignatura_repository.obtener_por_docente(id_docente)


    def consultar_aula(self, id_docente):
        self.__validar_id(id_docente)
        return self.__horario_service.consultar_aulas_por_docente(id_docente)


    def consultar_disponibilidad(self, id_docente):
        self.__validar_id(id_docente)
        return self.__horario_service.consultar_disponibilidad_docente(id_docente)


    def reportar_incidencia(self, id_docente, descripcion, tipo):
        self.__validar_id(id_docente)
        return self.__incidencia_service.registrar_incidencia(
            id_docente,
            descripcion,
            tipo
        )


    @staticmethod
    def __validar_id(id_docente):
        if id_docente is None or not str(id_docente).strip():
            raise ValueError("El ID del docente no puede quedar vacío.")