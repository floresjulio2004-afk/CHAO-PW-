import json
from pathlib import Path
from models.horario import Horario
from models.tiempo_horario import TiempoHorario
from repositories.horario_repository import HorarioRepository


class HorarioJsonRepository(HorarioRepository):
    def __init__(self, ruta_archivo=None):
        if ruta_archivo is None:
            ruta_archivo = (
                Path(__file__).resolve().parent.parent
                / "data"
                / "horarios.json"
            )
        self.__ruta_archivo = Path(ruta_archivo)


    def __leer_archivo(self):
        if not self.__ruta_archivo.exists():
            return []
        with open(self.__ruta_archivo, "r", encoding="utf-8") as archivo:
            registros = json.load(archivo)
        if not isinstance(registros, list):
            raise ValueError(
                "El archivo de horarios debe contener una lista."
            )
        return registros


    def __guardar_archivo(self, registros):
        with open(self.__ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(
                registros,
                archivo,
                ensure_ascii=False,
                indent=4
            )


    @staticmethod
    def __a_horario(registro):
        tiempos = [
            TiempoHorario(
                tiempo["id_tiempo"],
                tiempo["dia"],
                tiempo["hora_inicio"],
                tiempo["hora_fin"],
                tiempo["id_aula"]
            )
            for tiempo in registro.get("tiempos", [])
        ]
        return Horario(
            registro["id_horario"],
            registro["id_asignatura"],
            registro["id_paralelo"],
            registro["id_periodo"],
            registro["id_docente"],
            tiempos,
            registro.get("estado", "activo"),
            registro.get("observacion", "")
        )


    @staticmethod
    def __a_registro(horario, ids_estudiantes):
        return {
            "id_horario": horario.id_horario,
            "id_asignatura": horario.id_asignatura,
            "id_paralelo": horario.id_paralelo,
            "id_periodo": horario.id_periodo,
            "id_docente": horario.id_docente,
            "estado": horario.estado,
            "observacion": horario.observacion,
            "tiempos": [
                {
                    "id_tiempo": tiempo.id_tiempo,
                    "dia": tiempo.dia,
                    "hora_inicio": tiempo.hora_inicio,
                    "hora_fin": tiempo.hora_fin,
                    "id_aula": tiempo.id_aula
                }
                for tiempo in horario.tiempos
            ],
            "estudiantes": list(ids_estudiantes)
        }


    def obtener_todos(self):
        return [
            self.__a_horario(registro)
            for registro in self.__leer_archivo()
        ]


    def obtener_por_id(self, id_horario):
        for registro in self.__leer_archivo():
            if registro.get("id_horario") == id_horario:
                return self.__a_horario(registro)
        return None


    def obtener_por_estudiante(self, id_estudiante):
        return [
            self.__a_horario(registro)
            for registro in self.__leer_archivo()
            if id_estudiante in registro.get("estudiantes", [])
        ]


    def obtener_inscritos(self, id_horario):
        for registro in self.__leer_archivo():
            if registro.get("id_horario") == id_horario:
                return list(registro.get("estudiantes", []))
        return []


    def guardar(self, horario, ids_estudiantes=()):
        if not isinstance(horario, Horario):
            raise TypeError("El horario debe ser un objeto Horario.")
        registros = self.__leer_archivo()
        if any(
            registro.get("id_horario") == horario.id_horario
            for registro in registros
        ):
            raise ValueError("Ya existe un horario con ese ID.")
        registros.append(self.__a_registro(horario, ids_estudiantes))
        self.__guardar_archivo(registros)
        return horario


    def eliminar(self, id_horario):
        registros = self.__leer_archivo()
        restantes = [
            registro for registro in registros
            if registro.get("id_horario") != id_horario
        ]
        if len(restantes) == len(registros):
            return False
        self.__guardar_archivo(restantes)
        return True