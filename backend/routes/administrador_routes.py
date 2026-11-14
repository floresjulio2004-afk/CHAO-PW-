from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from routes.seguridad import rol_requerido


LONGITUD_MINIMA_CONTRASENA = 8
CAMPOS_ADICIONALES = ("nivel", "especialidad")


def crear_blueprint_administrador(administrador_service, registro_fabricas, gestor_contrasenas):
    bp = Blueprint(
        "admin_usuarios",
        __name__,
        url_prefix="/administrador/usuarios"
    )


    def listar_usuarios():
        usuarios = [
            {
                campo: valor
                for campo, valor in usuario.items()
                if campo != "contrasena_hash"
            }
            for usuario in administrador_service.consultar_usuarios()
        ]
        return sorted(
            usuarios,
            key=lambda u: (str(u.get("rol", "")), str(u.get("nombre", "")).lower())
        )


    def crear_desde_formulario(formulario):
        contrasena = formulario.get("contrasena", "")
        if len(contrasena) < LONGITUD_MINIMA_CONTRASENA:
            raise ValueError(
                f"La contraseña debe tener al menos {LONGITUD_MINIMA_CONTRASENA} caracteres."
            )
        fabrica = registro_fabricas.obtener(formulario.get("rol", ""))
        datos = {
            campo: formulario.get(campo, "").strip()
            for campo in CAMPOS_ADICIONALES
            if formulario.get(campo, "").strip()
        }
        return administrador_service.crear_usuario_desde_fabrica(
            fabrica,
            formulario.get("nombre", ""),
            formulario.get("cedula", ""),
            formulario.get("correo", ""),
            gestor_contrasenas.generar_hash(contrasena),
            **datos
        )


    @bp.route("/", methods=["GET", "POST"])
    @rol_requerido("administrador")
    def gestionar():
        error = None
        formulario = {}
        if request.method == "POST":
            formulario = request.form.to_dict()
            try:
                usuario = crear_desde_formulario(formulario)
                flash(
                    f"Usuario {usuario['nombre']} creado como {usuario['rol']}.",
                    "ok"
                )
                return redirect(url_for("admin_usuarios.gestionar"))
            except ValueError as excepcion:
                error = str(excepcion)
        return render_template(
            "admin_usuarios.html",
            nombre=session["nombre"],
            usuarios=listar_usuarios(),
            roles=registro_fabricas.roles(),
            formulario=formulario,
            error=error
        )


    @bp.route("/<id_usuario>/eliminar", methods=["POST"])
    @rol_requerido("administrador")
    def eliminar(id_usuario):
        if id_usuario == session.get("id"):
            flash("No puedes eliminar tu propia cuenta.", "error")
        elif administrador_service.eliminar_usuario(id_usuario):
            flash("Usuario eliminado.", "ok")
        else:
            flash("No se encontró el usuario.", "error")
        return redirect(url_for("admin_usuarios.gestionar"))


    return bp