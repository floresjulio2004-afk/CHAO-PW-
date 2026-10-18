import os

from flask import Flask, render_template

from db import crear_tablas
from routes.estudiante import estudiante_bp

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

crear_tablas()                      
app.register_blueprint(estudiante_bp)  

@app.route("/")
def inicio():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 80)))
