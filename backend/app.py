import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session
from builders.constructor_horario import ConstructorHorario, DIAS_SEMANA
from factories.registro_fabricas import RegistroFabricas
from models.asignatura import Asignatura
from models.aula import Aula
from models.paralelo import Paralelo
from models.periodo_academico import PeriodoAcademico
from repositories.catalogo_json_repository import CatalogoJsonRepository
from repositories.horario_json_repository import HorarioJsonRepository
from repositories.usuario_json_repository import UsuarioJsonRepository
from routes.administrador_routes import crear_blueprint_administrador
from routes.coordinador_routes import crear_blueprint_coordinador
from routes.seguridad import rol_requerido
from services.administrador_service import AdministradorService
from services.autenticacion_service import AutenticacionService
from services.coordinador_service import CoordinadorService
from services.gestor_contrasenas import GestorContrasenas
from services.horario_service import HorarioService


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


RUTA_CATALOGOS = Path(__file__).resolve().parent / "data" / "catalogos.json"
ROLES_VALIDOS = {"estudiante", "docente", "coordinador", "administrador"}


# Repositorios
usuario_repository = UsuarioJsonRepository()
horario_repository = HorarioJsonRepository()
asignatura_repository = CatalogoJsonRepository(
    RUTA_CATALOGOS, "asignaturas", Asignatura, "id_asignatura"
)
aula_repository = CatalogoJsonRepository(
    RUTA_CATALOGOS, "aulas", Aula, "id_aula"
)
paralelo_repository = CatalogoJsonRepository(
    RUTA_CATALOGOS, "paralelos", Paralelo, "id_paralelo"
)
periodo_repository = CatalogoJsonRepository(
    RUTA_CATALOGOS, "periodos", PeriodoAcademico, "id_periodo"
)

# Servicios
gestor_contrasenas = GestorContrasenas()
registro_fabricas = RegistroFabricas.por_defecto()
autenticacion = AutenticacionService(
    usuario_repository,
    gestor_contrasenas
)
horario_service = HorarioService(
    horario_repository,
    asignatura_repository,
    aula_repository,
    usuario_repository
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
coordinador_service = CoordinadorService(
    horario_repository=horario_repository,
    aula_repository=aula_repository,
    asignatura_repository=asignatura_repository,
    usuario_repository=usuario_repository,
    paralelo_repository=paralelo_repository,
    periodo_repository=periodo_repository,
    horario_service=horario_service,
    fabrica_constructor=ConstructorHorario
)


app.register_blueprint(
    crear_blueprint_administrador(
        administrador_service,
        registro_fabricas,
        gestor_contrasenas
    )
)
app.register_blueprint(
    crear_blueprint_coordinador(coordinador_service)
)


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
    clases = horario_service.clases_de_estudiante(session["id"])
    franjas, grilla = horario_service.armar_grilla(clases)
    return render_template(
        "horario.html",
        nombre=session["nombre"],
        dias=DIAS_SEMANA,
        franjas=franjas,
        grilla=grilla
    )


@app.route("/estudiante/clase/<id_clase>")
@rol_requerido("estudiante")
def estudiante_clase(id_clase):
    clases = horario_service.clases_de_estudiante(session["id"])
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