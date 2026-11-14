import json
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session
from factories.registro_fabricas import RegistroFabricas
from repositories.usuario_json_repository import UsuarioJsonRepository
from routes.administrador_routes import crear_blueprint_administrador
from routes.seguridad import rol_requerido
from services.administrador_service import AdministradorService
from services.autenticacion_service import AutenticacionService
from services.gestor_contrasenas import GestorContrasenas


RUTA_ENV = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(RUTA_ENV)


app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)


app.secret_key = os.getenv("SECRET_KEY")
if not app.secret_key:
    raise RuntimeError("La variable SECRET_KEY no está configurada")


usuario_repository = UsuarioJsonRepository()
gestor_contrasenas = GestorContrasenas()
registro_fabricas = RegistroFabricas.por_defecto()
autenticacion = AutenticacionService(
    usuario_repository,
    gestor_contrasenas
)
# Los repositorios en None se conectarán cuando existan sus implementaciones.
administrador_service = AdministradorService(
    usuario_repository=usuario_repository,
    rol_repository=None,
    facultad_repository=None,
    carrera_repository=None,
    nivel_educativo_repository=None,
    configuracion_repository=None,
    sistema_service=None
)


app.register_blueprint(
    crear_blueprint_administrador(
        administrador_service,
        registro_fabricas,
        gestor_contrasenas
    )
)


RUTA_HORARIOS = os.path.join(
    os.path.dirname(__file__), "data", "horarios.json"
)

ROLES_VALIDOS = {"estudiante", "docente", "coordinador", "administrador"}
DIAS_SEMANA = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]


def cargar_json(ruta):
    if not os.path.exists(ruta):
        return {}
    with open(ruta, encoding="utf-8") as archivo:
        return json.load(archivo)


def buscar_horario(cedula):
    horarios = cargar_json(RUTA_HORARIOS)
    return horarios.get(cedula, [])


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        correo = request.form.get("correo", "").strip()
        contrasena = request.form.get("contrasena", "")
        try:
            usuario = autenticacion.iniciar_sesion(
                correo,
                contrasena
            )
            session.clear()
            session["id"] = usuario["id"]
            session["nombre"] = usuario["nombre"]
            session["cedula"] = usuario["cedula"]
            session["correo"] = usuario["correo"]
            session["rol"] = usuario["rol"]
            return redirect(url_for("perfil"))
        except ValueError:
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
    if session["rol"] not in ROLES_VALIDOS:
        session.clear()
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
    if not cedula:
        return redirect(url_for("login"))
    clases = buscar_horario(cedula)
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
        dias=DIAS_SEMANA,
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


@app.route("/coordinador")
@rol_requerido("coordinador")
def coordinador():
    return render_template(
        "perfil_coordinador.html",
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