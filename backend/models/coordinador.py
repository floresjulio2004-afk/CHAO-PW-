from collections import Counter


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

    
    def crear_horario(self, horario):
        self.__validar_referencias(horario)
        self.__horario_service.validar_conflictos(horario)
        return self.__horario_repository.guardar(horario)


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
        usuarios = self.__usuario_repository.obtener_todos()
        docentes = {
            usuario["id_usuario"]: usuario["nombre"]
            for usuario in usuarios
            if usuario.get("rol") == "docente"
        }
        estudiantes_por_paralelo = Counter(
            usuario.get("id_paralelo")
            for usuario in usuarios
            if usuario.get("rol") == "estudiante"
        )
        vistas = []
        for horario in self.__horario_repository.obtener_todos():
            vistas.append({
                "id_horario": horario.id_horario,
                "asignatura": asignaturas.get(horario.id_asignatura, horario.id_asignatura),
                "paralelo": paralelos.get(horario.id_paralelo, horario.id_paralelo),
                "periodo": periodos.get(horario.id_periodo, horario.id_periodo),
                "docente": docentes.get(horario.id_docente, "Docente no registrado"),
                "sesiones": [
                    {
                        "dia": tiempo.dia,
                        "hora_inicio": tiempo.hora_inicio,
                        "hora_fin": tiempo.hora_fin,
                        "id_aula": tiempo.id_aula
                    }
                    for tiempo in horario.tiempos
                ],
                "estudiantes": estudiantes_por_paralelo.get(horario.id_paralelo, 0),
                "observacion": horario.observacion
            })
        return sorted(
            vistas,
            key=lambda vista: (vista["asignatura"].lower(), vista["paralelo"])
        )


    def eliminar_horario(self, id_horario):
        return self.__horario_repository.eliminar(id_horario)


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
        return self.crear_horario(constructor.construir())

    
    def consultar_aulas(self):
        return self.__aula_repository.obtener_todos()


    def consultar_asignaturas(self):
        return self.__asignatura_repository.obtener_todos()


    def consultar_paralelos(self):
        return self.__paralelo_repository.obtener_todos()


    def consultar_periodos(self):
        return self.__periodo_repository.obtener_todos()


    def consultar_docentes(self):
        docentes = [
            {
                "id_usuario": usuario["id_usuario"],
                "nombre": usuario["nombre"],
                "cedula": usuario["cedula"]
            }
            for usuario in self.__usuario_repository.obtener_todos()
            if usuario.get("rol") == "docente"
        ]
        return sorted(docentes, key=lambda docente: docente["nombre"].lower())


    def __validar_referencias(self, horario):
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