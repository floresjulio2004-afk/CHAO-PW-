from flask import Blueprint, abort, render_template, request
from db import obtener_conexion

estudiante_bp = Blueprint("estudiante", __name__, url_prefix="/estudiante")
DIAS = {1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes"}

@estudiante_bp.route("/horario")
def horario():
    id_estudiante = request.args.get("id", 1, type=int)

    con = obtener_conexion()

    estudiante = con.execute("""
        SELECT u.nombre
        FROM usuarios u
        JOIN estudiantes e ON e.id_usuario = u.id_usuario
        WHERE e.id_usuario = ?
    """, (id_estudiante,)).fetchone()
    if estudiante is None:
        con.close()
        abort(404)

    clases = con.execute("""
        SELECT a.id_asignatura AS asignatura_id, a.codigo, a.nombre,
               u.nombre AS docente, au.nombre AS aula,
               t.dia, t.hora_inicio, t.hora_fin
        FROM estudiantes e
        JOIN horarios h             ON h.id_paralelo = e.id_paralelo
        JOIN periodos_academicos p  ON p.id_periodo = h.id_periodo
        JOIN asignaturas a          ON a.id_asignatura = h.id_asignatura
        JOIN usuarios u             ON u.id_usuario = h.id_docente
        JOIN aulas au               ON au.id_aula = h.id_aula
        JOIN tiempos_horario t      ON t.id_horario = h.id_horario
        WHERE e.id_usuario = ? AND p.estado = 'Activo'
        ORDER BY t.hora_inicio
    """, (id_estudiante,)).fetchall()
    con.close()

    franjas = sorted({(c["hora_inicio"], c["hora_fin"]) for c in clases})
    grilla = {(c["dia"], c["hora_inicio"], c["hora_fin"]): c for c in clases}

    return render_template(
        "estudiante/horario.html",
        estudiante=estudiante, dias=DIAS, franjas=franjas, grilla=grilla,
    )