from itertools import zip_longest
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from builders.constructor_horario import DIAS_SEMANA
from routes.seguridad import rol_requerido


NUMERO_FILAS_SESION = 3
CAMPOS_FILA = ("dia", "hora_inicio", "hora_fin", "aula")


def crear_blueprint_coordinador(coordinador_service):
    bp = Blueprint(
        "coord_horarios",
        __name__,
        url_prefix="/coordinador/horarios"
    )


    def fila_vacia():
        return {campo: "" for campo in CAMPOS_FILA}


    def leer_filas(formulario):
        columnas = [formulario.getlist(campo) for campo in CAMPOS_FILA]
        filas = [
            {campo: valor.strip() for campo, valor in zip(CAMPOS_FILA, valores)}
            for valores in zip_longest(*columnas, fillvalue="")
        ]
        while len(filas) < NUMERO_FILAS_SESION:
            filas.append(fila_vacia())
        return filas


    def leer_datos(formulario, filas):
        return {
            "id_asignatura": formulario.get("id_asignatura", ""),
            "id_paralelo": formulario.get("id_paralelo", ""),
            "id_periodo": formulario.get("id_periodo", ""),
            "id_docente": formulario.get("id_docente", ""),
            "observacion": formulario.get("observacion", ""),
            "tiempos": [
                {
                    "dia": fila["dia"],
                    "hora_inicio": fila["hora_inicio"],
                    "hora_fin": fila["hora_fin"],
                    "id_aula": fila["aula"]
                }
                for fila in filas
                if any(fila.values())
            ],
            "estudiantes": formulario.getlist("estudiantes")
        }


    @bp.route("/", methods=["GET", "POST"])
    @rol_requerido("coordinador")
    def gestionar():
        error = None
        formulario = {
            "filas": [fila_vacia() for _ in range(NUMERO_FILAS_SESION)],
            "estudiantes": []
        }
        if request.method == "POST":
            filas = leer_filas(request.form)
            formulario = request.form.to_dict()
            formulario["filas"] = filas
            formulario["estudiantes"] = request.form.getlist("estudiantes")
            try:
                coordinador_service.generar_horario(
                    leer_datos(request.form, filas)
                )
                flash("Horario creado correctamente.", "ok")
                return redirect(url_for("coord_horarios.gestionar"))
            except ValueError as excepcion:
                error = str(excepcion)
        return render_template(
            "coordinador_horarios.html",
            nombre=session["nombre"],
            dias=DIAS_SEMANA,
            asignaturas=coordinador_service.consultar_asignaturas(),
            paralelos=coordinador_service.consultar_paralelos(),
            periodos=coordinador_service.consultar_periodos(),
            aulas=coordinador_service.consultar_aulas(),
            docentes=coordinador_service.consultar_docentes(),
            estudiantes=coordinador_service.consultar_estudiantes(),
            horarios=coordinador_service.consultar_horarios(),
            formulario=formulario,
            error=error
        )


    @bp.route("/<id_horario>/eliminar", methods=["POST"])
    @rol_requerido("coordinador")
    def eliminar(id_horario):
        if coordinador_service.eliminar_horario(id_horario):
            flash("Horario eliminado.", "ok")
        else:
            flash("No se encontró el horario.", "error")
        return redirect(url_for("coord_horarios.gestionar"))


    return bp