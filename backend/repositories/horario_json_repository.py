from pathlib import Path
from models.horario import Horario
from models.tiempo_horario import TiempoHorario
from repositories.almacen_json import AlmacenJson
from repositories.horario_repository import HorarioRepository


class HorarioJsonRepository(HorarioRepository):
    def __init__(self, ruta_archivo=None):
        if ruta_archivo is None:
            ruta_archivo = (
                Path(__file__).resolve().parent.parent
                / "data"
                / "horarios.json"
            )
        self.__almacen = AlmacenJson(ruta_archivo, list)


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
    def __a_registro(horario):
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
            ]
        }


    def obtener_todos(self):
        return [
            self.__a_horario(registro)
            for registro in self.__almacen.leer()
        ]


    def obtener_por_id(self, id_horario):
        for registro in self.__almacen.leer():
            if registro.get("id_horario") == id_horario:
                return self.__a_horario(registro)
        return None


    def obtener_por_paralelo(self, id_paralelo):
        return [
            self.__a_horario(registro)
            for registro in self.__almacen.leer()
            if registro.get("id_paralelo") == id_paralelo
        ]


    def obtener_por_docente(self, id_docente):
        return [
            self.__a_horario(registro)
            for registro in self.__almacen.leer()
            if registro.get("id_docente") == id_docente
        ]


    def guardar(self, horario):
        if not isinstance(horario, Horario):
            raise TypeError("El horario debe ser un objeto Horario.")
        registros = self.__almacen.leer()
        if any(
            registro.get("id_horario") == horario.id_horario
            for registro in registros
        ):
            raise ValueError("Ya existe un horario con ese ID.")
        registros.append(self.__a_registro(horario))
        self.__almacen.guardar(registros)
        return horario


    def actualizar(self, horario):
        if not isinstance(horario, Horario):
            raise TypeError("El horario debe ser un objeto Horario.")
        registros = self.__almacen.leer()
        for indice, registro in enumerate(registros):
            if registro.get("id_horario") == horario.id_horario:
                registros[indice] = self.__a_registro(horario)
                self.__almacen.guardar(registros)
                return horario
        return None


    def eliminar(self, id_horario):
        registros = self.__almacen.leer()
        restantes = [
            registro for registro in registros
            if registro.get("id_horario") != id_horario
        ]
        if len(restantes) == len(registros):
            return False
        self.__almacen.guardar(restantes)
        return True