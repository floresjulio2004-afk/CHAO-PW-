import os 
from pathlib import path 
from threading import RLock
from dotenv import load_dotenv
from flask import Flask 
from flask_wtf.csrf import CSRFError, CSRFProtect 

from builders.constructor_horario import ConstructorHorario
from factories.registro_fabricas import RegistroFabricas
from models.asignatura import Asignatura
from models.aula import Aula
from models.carrera import Carrera
from models.facultad import Facultad
from models.nivel_educativo import NivelEducativo
from models.paralelo import Paralelo
from models.periodo_academico import PeriodoAcademico
from repositories.almacen_json import AlmacenJson
from repositories.catalogo_json_repository import CatalogoJsonRepository
from repositories.horario_json_repository import HorarioJsonRepository
from repositories.usuario_json_repository import UsuarioJsonRepository
from routes.administrador_routes import crear_blueprint_administrador
from routes.coordinador_routes import crear_blueprint_coordinador
from routes.horario_routes import crear_blueprint_horario
from routes.sesion_routes import registrar_rutas_sesion
from routes.sistema_routes import crear_blueprint_sistema
from services.administrador_service import AdministradorService
from services.autenticacion_service import AutenticacionService
from services.coordinador_service import CoordinadorService
from services.gestor_contrasenas import GestorContrasenas
from services.horario_service import HorarioService
from services.sistema_service import SistemaService

RUTA_BACKEND = Path(__file__).resolve().parent 

def create_app(config=None):
    load_dotenv(RUTA_BACKEND.parent/".env")
    app = Flask(__name__, template_folder="../frontend/templates",
                static_folder="../frontend/static")
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY"),
        SESSION_COOKIE_SAMESITE="Lax",
        DATA_DIR=RUTA_BACKEND / "data",
    )
    app.config.update(config or {})
    if not app.secret_key
        raise RuntimeError("El valor Secret_Key está sin configurar")
    CSRFProtect(app)

    @app.errorhandler(CSRFError)
    def formulario_invalido(error):
        return "El formulario no es válido o caducó. " \
        "Vuelve a abrirlo e inténtalo de nuevo.", 400

    datos=Path(app.config["DATA_DIR"])
    block = RLock()
    usuarios = UsuarioJsonRepository(datos/"usuarios.json", block=block)
    horarios = HorarioJsonRepository(datos/"horarios.json")

    def catalogo(clave, clase, campo_id):
        return CatalogoJsonRepository(datos/"catalogo.json", clave, clase, campo_id)

        asignaturas = catalogo("asignaturas", Asignatura, "id_asignatura")
    aulas = catalogo("aulas", Aula, "id_aula")
    paralelos = catalogo("paralelos", Paralelo, "id_paralelo")
    periodos = catalogo("periodos", PeriodoAcademico, "id_periodo")
    facultades = catalogo("facultades", Facultad, "id_facultad")
    carreras = catalogo("carreras", Carrera, "id_carrera")
    niveles = catalogo("niveles", NivelEducativo, "id_nivel")

    contrasenas = GestorContrasenas()
    fabricas = RegistroFabricas.por_defecto()
    autenticacion = AutenticacionService(usuarios, contrasenas)
    consulta = HorarioService(horarios, asignaturas, aulas, usuarios)
    administrador = AdministradorService(
        usuarios, facultades, carreras, niveles, paralelos, horarios, bloqueo=bloqueo
    )
    coordinador = CoordinadorService(
        horarios, aulas, asignaturas, usuarios, paralelos, periodos, consulta, ConstructorHorario,
        bloqueo=bloqueo
    )

    sistema = SistemaService(AlmacenJson(datos / "configuracion.json", dict), usuarios, horarios)

    @app.context_processor
    def informacion_publica():
        return {"configuracion_sistema": sistema.consultar_configuracion()}

    roles = fabricas.roles()
    registrar_rutas_sesion(app, autenticacion, roles, usuarios)
    app.register_blueprint(crear_blueprint_sistema(sistema, roles))
    app.register_blueprint(crear_blueprint_administrador(administrador, fabricas, contrasenas))
    app.register_blueprint(crear_blueprint_coordinador(coordinador))
    app.register_blueprint(crear_blueprint_horario(
        "estudiante", "Mi horario estudiantil", consulta.clases_de_estudiante
    ))
    app.register_blueprint(crear_blueprint_horario(
        "docente", "Mi horario docente", consulta.clases_de_docente
    ))
    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000)