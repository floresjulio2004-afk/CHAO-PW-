class CoordinadorService:
    def __init__(self, horario_repository, aula_repository, asignatura_repository, usuario_repository, paralelo_repository, periodo_repository, horario_service, fabrica_constructor):
        self.__horario_repository = horario_repository
        self.__aula_repository = aula_repository
        self.__asignatura_repository = asignatura_repository
        self.__usuario_repository = usuario_repository
        self.__paralelo_repository = paralelo_repository
        self.__periodo_repository = periodo_repository
        self.__horario_service = horario_service
        self.__fabrica_constructor = fabrica_constructor

    # GESTIÓN DE HORARIOS
    def crear_horario(self, horario, ids_estudiantes=()):
        ids_estudiantes = list(dict.fromkeys(ids_estudiantes))
        self.__validar_referencias(horario, ids_estudiantes)
        self.__horario_service.validar_conflictos(horario, ids_estudiantes)
        return self.__horario_repository.guardar(horario, ids_estudiantes)


    def consultar_horarios(self):
        asignaturas = {
            asignatura.id_asignatura: asignatura.nombre
            for asignatura in self.__asignatura_repository.obtener_todos()
        }
        paralelos = {
            paralelo.id_paralelo: f"Paralelo {paralelo.nombre}"
            for paralelo in self.__paralelo_repository.obtener_todos()
        }
        periodos = {
            periodo.id_periodo: periodo.nombre
            for periodo in self.__periodo_repository.obtener_todos()
        }
        vistas = []
        for horario in self.__horario_repository.obtener_todos():
            docente = self.__usuario_repository.obtener_por_id(horario.id_docente)
            vistas.append({
                "id_horario": horario.id_horario,
                "asignatura": asignaturas.get(horario.id_asignatura, horario.id_asignatura),
                "paralelo": paralelos.get(horario.id_paralelo, horario.id_paralelo),
                "periodo": periodos.get(horario.id_periodo, horario.id_periodo),
                "docente": docente["nombre"] if docente else "Docente no registrado",
                "sesiones": [
                    {
                        "dia": tiempo.dia,
                        "hora_inicio": tiempo.hora_inicio,
                        "hora_fin": tiempo.hora_fin,
                        "id_aula": tiempo.id_aula
                    }
                    for tiempo in horario.tiempos
                ],
                "inscritos": len(
                    self.__horario_repository.obtener_inscritos(horario.id_horario)
                ),
                "observacion": horario.observacion
            })
        return sorted(
            vistas,
            key=lambda vista: (vista["asignatura"].lower(), vista["paralelo"])
        )


    def modificar_horario(self, id_horario, datos):
        pass


    def eliminar_horario(self, id_horario):
        return self.__horario_repository.eliminar(id_horario)

    # GESTIÓN DE AULAS
    def crear_aula(self, aula):
        pass

    def consultar_aulas(self):
        return self.__aula_repository.obtener_todos()

    def modificar_aula(self, id_aula, datos):
        pass

    def eliminar_aula(self, id_aula):
        pass

    # GESTIÓN DE ASIGNATURAS
    def crear_asignatura(self, asignatura):
        pass

    def consultar_asignaturas(self):
        return self.__asignatura_repository.obtener_todos()

    def modificar_asignatura(self, id_asignatura, datos):
        pass

    def eliminar_asignatura(self, id_asignatura):
        pass

    # GESTIÓN DE DOCENTES
    def crear_docente(self, docente):
        pass

    def consultar_docentes(self):
        return self.__usuarios_por_rol("docente")

    def modificar_docente(self, id_docente, datos):
        pass

    def eliminar_docente(self, id_docente):
        pass

    # CONSULTA DE ESTUDIANTES (para inscribirlos en un horario)
    def consultar_estudiantes(self):
        return self.__usuarios_por_rol("estudiante")

    # GESTIÓN DE PARALELOS
    def crear_paralelo(self, paralelo):
        pass

    def consultar_paralelos(self):
        return self.__paralelo_repository.obtener_todos()

    def modificar_paralelo(self, id_paralelo, datos):
        pass

    def eliminar_paralelo(self, id_paralelo):
        pass

    # GESTIÓN DE PERIODOS ACADÉMICOS
    def crear_periodo(self, periodo):
        pass

    def consultar_periodos(self):
        return self.__periodo_repository.obtener_todos()

    def modificar_periodo(self, id_periodo, datos):
        pass

    def eliminar_periodo(self, id_periodo):
        pass

    # GENERACIÓN DE HORARIOS
    def generar_horario(self, datos):
        constructor = (
            self.__fabrica_constructor()
            .con_asignatura(datos.get("id_asignatura"))
            .con_paralelo(datos.get("id_paralelo"))
            .con_periodo(datos.get("id_periodo"))
            .con_docente(datos.get("id_docente"))
            .con_observacion(datos.get("observacion"))
        )
        for tiempo in datos.get("tiempos", []):
            constructor.agregar_tiempo(
                tiempo.get("dia"),
                tiempo.get("hora_inicio"),
                tiempo.get("hora_fin"),
                tiempo.get("id_aula")
            )
        horario = constructor.construir()
        return self.crear_horario(horario, datos.get("estudiantes", []))

    # MÉTODOS PRIVADOS
    def __usuarios_por_rol(self, rol):
        usuarios = [
            {
                "id_usuario": usuario["id_usuario"],
                "nombre": usuario["nombre"],
                "cedula": usuario["cedula"]
            }
            for usuario in self.__usuario_repository.obtener_todos()
            if usuario.get("rol") == rol
        ]
        return sorted(usuarios, key=lambda usuario: usuario["nombre"].lower())


    def __validar_referencias(self, horario, ids_estudiantes):
        if self.__asignatura_repository.obtener_por_id(horario.id_asignatura) is None:
            raise ValueError("La asignatura seleccionada no existe.")
        if self.__paralelo_repository.obtener_por_id(horario.id_paralelo) is None:
            raise ValueError("El paralelo seleccionado no existe.")
        if self.__periodo_repository.obtener_por_id(horario.id_periodo) is None:
            raise ValueError("El periodo académico seleccionado no existe.")
        docente = self.__usuario_repository.obtener_por_id(horario.id_docente)
        if not docente or docente.get("rol") != "docente":
            raise ValueError("El docente seleccionado no es válido.")
        for tiempo in horario.tiempos:
            if self.__aula_repository.obtener_por_id(tiempo.id_aula) is None:
                raise ValueError(f"El aula {tiempo.id_aula} no existe.")
        for id_estudiante in ids_estudiantes:
            estudiante = self.__usuario_repository.obtener_por_id(id_estudiante)
            if not estudiante or estudiante.get("rol") != "estudiante":
                raise ValueError("Uno de los estudiantes seleccionados no es válido.")