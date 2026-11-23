from functools import wraps
from flask import redirect, url_for, session


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