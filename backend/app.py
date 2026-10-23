import json
import os
from functools import wraps

from flask import Flask, render_template, request, redirect, url_for, session
from services.gestor_contrasenas import GestorContrasenas

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

app.secret_key = os.getenv("SECRET_KEY", "clave-de-desarrollo")

RUTA_USUARIOS = os.path.join(
    os.path.dirname(__file__), "data", "usuarios.json"
)

RUTA_HORARIOS = os.path.join(
    os.path.dirname(__file__), "data", "horarios.json"
)


def cargar_json(ruta):
    with open(ruta, encoding="utf-8") as archivo:
        return json.load(archivo)


def buscar_usuario(correo):
    usuarios = cargar_json(RUTA_USUARIOS)

    for usuario in usuarios:
        if usuario["correo"].lower() == correo.lower():
            return usuario

    return None


def buscar_horario(cedula):
    horarios = cargar_json(RUTA_HORARIOS)
    return horarios.get(cedula, [])


def rol_requerido(rol):
    def decorador(funcion):
        @wraps(funcion)
        def envoltura(*args, **kwargs):
            if "rol" not in session:
                return redirect(url_for("login"))

            if session["rol"] != rol:
                return redirect(url_for("perfil"))

            return funcion(*args, **kwargs)

        return envoltura

    return decorador


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        correo = request.form["correo"].strip()
        contrasena = request.form["contrasena"]

        usuario = buscar_usuario(correo)

        if usuario and GestorContrasenas.verificar_contrasena(
            contrasena,
            usuario["contrasena_hash"]
        ):
            session["nombre"] = usuario["nombre"]
            session["cedula"] = usuario["cedula"]
            session["rol"] = usuario["rol"]

            return redirect(url_for("perfil"))

        error = "Correo o contraseña incorrectos"

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/perfil")
def perfil():
    if "rol" not in session:
        return redirect(url_for("login"))

    return redirect(url_for(session["rol"]))


@app.route("/estudiante")
@rol_requerido("estudiante")
def estudiante():
    return render_template(
        "perfil_estudiante.html",
        nombre=session["nombre"]
    )


@app.route("/estudiante/horario")
@rol_requerido("estudiante")
def estudiante_horario():
    cedula = session.get("cedula")

    print("CÉDULA EN SESIÓN:", cedula)

    if not cedula:
        print("ERROR: No se encontró la cédula en la sesión.")
        return redirect(url_for("login"))

    clases = buscar_horario(cedula)

    print("CANTIDAD DE CLASES:", len(clases))

    dias = [
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes"
    ]

    franjas = sorted({
        (clase["hora_inicio"], clase["hora_fin"])
        for clase in clases
    })

    grilla = {}

    for clase in clases:
        clave = (clase["dia"], clase["hora_inicio"])
        grilla[clave] = clase

    return render_template(
        "horario.html",
        nombre=session["nombre"],
        dias=dias,
        franjas=franjas,
        grilla=grilla
    )


@app.route("/estudiante/clase/<int:id_clase>")
@rol_requerido("estudiante")
def estudiante_clase(id_clase):
    clases = buscar_horario(session["cedula"])

    clase = next(
        (c for c in clases if c["id"] == id_clase),
        None
    )

    if clase is None:
        return "No se encontró la clase solicitada.", 404

    return render_template(
        "clase.html",
        clase=clase
    )


@app.route("/docente")
@rol_requerido("docente")
def docente():
    return render_template(
        "perfil_docente.html",
        nombre=session["nombre"]
    )


@app.route("/gestor")
@rol_requerido("gestor")
def gestor():
    return render_template(
        "perfil_gestor.html",
        nombre=session["nombre"]
    )


@app.route("/administrador")
@rol_requerido("administrador")
def administrador():
    return render_template(
        "perfil_administrador.html",
        nombre=session["nombre"]
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)