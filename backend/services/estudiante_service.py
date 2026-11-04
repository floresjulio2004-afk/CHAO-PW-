class EstudianteService:
    def __init__(self, horario_repository, usuario_repository, asignatura_repository, incidencia_repository):
        self.__horario_repository = horario_repository
        self.__usuario_repository = usuario_repository
        self.__asignatura_repository = asignatura_repository
        self.__incidencia_repository = incidencia_repository


    def consultar_horario(self, id_estudiante):
        self.__validar_id(id_estudiante)
        return self.__horario_repository.obtener_por_estudiante(id_estudiante)


    def consultar_docente(self, id_estudiante):
        self.__validar_id(id_estudiante)
        return self.__usuario_repository.obtener_docentes_por_estudiante(id_estudiante)


    def consultar_asignatura(self, id_estudiante):
        self.__validar_id(id_estudiante)
        return self.__asignatura_repository.obtener_por_estudiante(id_estudiante)


    def consultar_incidencias(self, id_estudiante):
        self.__validar_id(id_estudiante)
        incidencias = (
            self.__incidencia_repository.obtener_por_estudiante(
                id_estudiante
            )
        )
        avisos_generales = (
            self.__incidencia_repository.obtener_avisos_generales(
                id_estudiante
            )
        )
        return {
            "incidencias": incidencias,
            "avisos_generales": avisos_generales
        }


    def personalizar_interfaz(self, estudiante, tema):
        if estudiante is None:
            raise ValueError("El estudiante no puede quedar vacío.")
        estudiante.personalizar_interfaz(tema)
        return estudiante.tema


    @staticmethod
    def __validar_id(id_estudiante):
        if id_estudiante is None or not str(id_estudiante).strip():
            raise ValueError("El ID del estudiante no puede quedar vacío.")