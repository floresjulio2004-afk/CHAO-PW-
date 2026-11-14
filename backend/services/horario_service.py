import zlib


class HorarioService:
    def __init__(self, horario_repository, asignatura_repository, aula_repository, usuario_repository):
        self.__horario_repository = horario_repository
        self.__asignatura_repository = asignatura_repository
        self.__aula_repository = aula_repository
        self.__usuario_repository = usuario_repository


    def clases_de_estudiante(self, id_estudiante):
        asignaturas = self.__nombres_de_asignaturas()
        aulas = {
            aula.id_aula: aula.nombre
            for aula in self.__aula_repository.obtener_todos()
        }
        clases = []
        for horario in self.__horario_repository.obtener_por_estudiante(id_estudiante):
            nombre_docente = self.__nombre_usuario(
                horario.id_docente,
                "Docente no registrado"
            )
            color = zlib.crc32(horario.id_horario.encode("utf-8")) % 5
            for tiempo in horario.tiempos:
                clases.append({
                    "id": tiempo.id_tiempo,
                    "dia": tiempo.dia,
                    "hora_inicio": tiempo.hora_inicio,
                    "hora_fin": tiempo.hora_fin,
                    "asignatura": asignaturas.get(
                        horario.id_asignatura,
                        horario.id_asignatura
                    ),
                    "docente": nombre_docente,
                    "salon": aulas.get(tiempo.id_aula, "Aula sin registrar"),
                    "codigo_aula": tiempo.id_aula,
                    "color": color
                })
        return clases


    @staticmethod
    def armar_grilla(clases):
        franjas = sorted({
            (clase["hora_inicio"], clase["hora_fin"])
            for clase in clases
        })
        grilla = {
            (clase["dia"], clase["hora_inicio"], clase["hora_fin"]): clase
            for clase in clases
        }
        return franjas, grilla


    def validar_conflictos(self, horario, ids_estudiantes=()):
        asignaturas = self.__nombres_de_asignaturas()
        otros_horarios = [
            otro for otro in self.__horario_repository.obtener_todos()
            if otro.id_periodo == horario.id_periodo
            and otro.id_horario != horario.id_horario
        ]
        for otro in otros_horarios:
            materia = asignaturas.get(otro.id_asignatura, otro.id_asignatura)
            for nuevo in horario.tiempos:
                for existente in otro.tiempos:
                    if not self.__se_superponen(nuevo, existente):
                        continue
                    if otro.id_docente == horario.id_docente:
                        raise ValueError(self.__mensaje(
                            "El docente ya tiene clase",
                            existente,
                            materia
                        ))
                    if existente.id_aula == nuevo.id_aula:
                        raise ValueError(self.__mensaje(
                            f"El aula {nuevo.id_aula} ya está ocupada",
                            existente,
                            materia
                        ))
        for id_estudiante in ids_estudiantes:
            for otro in self.__horario_repository.obtener_por_estudiante(id_estudiante):
                if (
                    otro.id_periodo != horario.id_periodo
                    or otro.id_horario == horario.id_horario
                ):
                    continue
                materia = asignaturas.get(otro.id_asignatura, otro.id_asignatura)
                for nuevo in horario.tiempos:
                    for existente in otro.tiempos:
                        if self.__se_superponen(nuevo, existente):
                            nombre = self.__nombre_usuario(
                                id_estudiante,
                                id_estudiante
                            )
                            raise ValueError(self.__mensaje(
                                f"El estudiante {nombre} ya tiene clase",
                                existente,
                                materia
                            ))


    def __nombres_de_asignaturas(self):
        return {
            asignatura.id_asignatura: asignatura.nombre
            for asignatura in self.__asignatura_repository.obtener_todos()
        }


    def __nombre_usuario(self, id_usuario, por_defecto):
        usuario = self.__usuario_repository.obtener_por_id(id_usuario)
        return usuario["nombre"] if usuario else por_defecto


    @staticmethod
    def __se_superponen(tiempo_a, tiempo_b):
        return (
            tiempo_a.dia == tiempo_b.dia
            and tiempo_a.hora_inicio < tiempo_b.hora_fin
            and tiempo_b.hora_inicio < tiempo_a.hora_fin
        )


    @staticmethod
    def __mensaje(prefijo, tiempo, materia):
        return (
            f"{prefijo} el {tiempo.dia} de "
            f"{tiempo.hora_inicio} a {tiempo.hora_fin} ({materia})."
        )