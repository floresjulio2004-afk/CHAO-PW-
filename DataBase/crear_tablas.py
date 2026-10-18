import sqlite3
from pathlib import Path

ruta_db = Path(__file__).resolve().parent / "horarios.db"


def crear_tablas():
    conexion = sqlite3.connect(ruta_db)
    conexion.executescript("""

    CREATE TABLE IF NOT EXISTS facultades (
        id_facultad INTEGER PRIMARY KEY,
        nombre_facultad VARCHAR(60)
    );

    CREATE TABLE IF NOT EXISTS carreras (
        id_carrera INTEGER PRIMARY KEY,
        nombre_carrera VARCHAR(60),
        codigo VARCHAR(20),
        id_facultad INTEGER,
        FOREIGN KEY (id_facultad) REFERENCES facultades(id_facultad)
    );

    CREATE TABLE IF NOT EXISTS niveles_educativos (
        id_nivel_educativo INTEGER PRIMARY KEY,
        tipo_nivel_educativo VARCHAR(60),
        descripcion VARCHAR(80)
    );

    CREATE TABLE IF NOT EXISTS paralelos (
        id_paralelo INTEGER PRIMARY KEY,
        nombre VARCHAR(60),
        descripcion VARCHAR(80),
        id_nivel INTEGER,
        id_carrera INTEGER,
        FOREIGN KEY (id_nivel) REFERENCES niveles_educativos(id_nivel_educativo),
        FOREIGN KEY (id_carrera) REFERENCES carreras(id_carrera)
    );

    CREATE TABLE IF NOT EXISTS asignaturas (
        id_asignatura INTEGER PRIMARY KEY,
        codigo VARCHAR(30),
        nombre VARCHAR(60),
        credito INTEGER,
        hora INTEGER
    );

    CREATE TABLE IF NOT EXISTS aulas (
        id_aula INTEGER PRIMARY KEY,
        nombre VARCHAR(60),
        capacidad INTEGER,
        tipo VARCHAR(30),
        disponibilidad INTEGER DEFAULT 1
    );

    CREATE TABLE IF NOT EXISTS periodos_academicos (
        id_periodo INTEGER PRIMARY KEY,
        nombre VARCHAR(40),
        fecha_inicio DATE,
        fecha_fin DATE,
        estado VARCHAR(40)
    );

    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY,
        nombre VARCHAR(60),
        cedula VARCHAR(10) UNIQUE,
        correo VARCHAR(60),
        contrasena VARCHAR(100)
    );

    CREATE TABLE IF NOT EXISTS estudiantes (
        id_usuario INTEGER PRIMARY KEY,
        nivel VARCHAR(60),
        id_carrera INTEGER,
        id_paralelo INTEGER,
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
        FOREIGN KEY (id_carrera) REFERENCES carreras(id_carrera),
        FOREIGN KEY (id_paralelo) REFERENCES paralelos(id_paralelo)
    );

    CREATE TABLE IF NOT EXISTS docentes (
        id_usuario INTEGER PRIMARY KEY,
        especialidad VARCHAR(60),
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
    );

    CREATE TABLE IF NOT EXISTS coordinadores (
        id_usuario INTEGER PRIMARY KEY,
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
    );

    CREATE TABLE IF NOT EXISTS incidencias (
        id_incidencia INTEGER PRIMARY KEY,
        motivo VARCHAR(120),
        tipo VARCHAR(20),
        fecha DATE,
        estado VARCHAR(20),
        id_usuario INTEGER,
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
    );

    CREATE TABLE IF NOT EXISTS horarios (
        id_horario INTEGER PRIMARY KEY,
        estado VARCHAR(20),
        observacion VARCHAR(100),
        id_asignatura INTEGER,
        id_docente INTEGER,
        id_aula INTEGER,
        id_paralelo INTEGER,
        id_periodo INTEGER,
        FOREIGN KEY (id_asignatura) REFERENCES asignaturas(id_asignatura),
        FOREIGN KEY (id_docente) REFERENCES docentes(id_usuario),
        FOREIGN KEY (id_aula) REFERENCES aulas(id_aula),
        FOREIGN KEY (id_paralelo) REFERENCES paralelos(id_paralelo),
        FOREIGN KEY (id_periodo) REFERENCES periodos_academicos(id_periodo)
    );

    CREATE TABLE IF NOT EXISTS tiempos_horario (
        id_tiempo_horario INTEGER PRIMARY KEY,
        dia INTEGER,
        hora_inicio VARCHAR(5),
        hora_fin VARCHAR(5),
        id_horario INTEGER,
        FOREIGN KEY (id_horario) REFERENCES horarios(id_horario)
    );

    """)

    cantidad = conexion.execute("SELECT COUNT(*) FROM usuarios").fetchone()[0]
    if cantidad == 0:
        conexion.executescript("""
        INSERT INTO facultades VALUES (1, 'Facultad Ciencias de la vida y Tecnologia');
        INSERT INTO carreras VALUES (1, 'Ingeniería de Software', 'SOF', 1);
        INSERT INTO niveles_educativos VALUES (1, 'Tercer', 'Tercer semestre');
        INSERT INTO paralelos VALUES (1, 'B', 'Paralelo B', 1, 1);
        INSERT INTO periodos_academicos VALUES (1, 'Periodo 2026-2', '2026-08-31', '2026-12-18', 'Activo');

        INSERT INTO asignaturas VALUES (1, 'AUP-101', 'Estructura de datos', 4, 4);
        INSERT INTO asignaturas VALUES (2, 'AUR-201', 'Modelado Orientado a Objetos', 4, 4);
        INSERT INTO asignaturas VALUES (3, 'AUC-301', 'Base de datos', 4, 4);

        INSERT INTO aulas VALUES (1, 'Aula 101', 35, 'Aula', 1);
        INSERT INTO aulas VALUES (2, 'Lab 2', 25, 'Laboratorio', 1);

        INSERT INTO usuarios VALUES (1, 'Estudiante de Prueba', '1300000000', 'estudiante@correo.com', '1234');
        INSERT INTO usuarios VALUES (2, 'Ing. Flores', '1300000001', 'mora@correo.com', '1234');
        INSERT INTO usuarios VALUES (3, 'Ing. Lucas', '1300000002', 'vera@correo.com', '1234');
        INSERT INTO usuarios VALUES (4, 'Coordinador de Prueba', '1300000003', 'coordinador@correo.com', '1234');

        INSERT INTO estudiantes VALUES (1, 'Tercer', 1, 1);
        INSERT INTO docentes VALUES (2, 'Estructura de datos');
        INSERT INTO docentes VALUES (3, 'Programación orientada a objetos');
        INSERT INTO coordinadores VALUES (4);

        INSERT INTO horarios VALUES (1, 'Activo', '', 1, 2, 1, 1, 1);
        INSERT INTO horarios VALUES (2, 'Activo', '', 2, 3, 1, 1, 1);
        INSERT INTO horarios VALUES (3, 'Activo', '', 3, 2, 2, 1, 1);

        INSERT INTO tiempos_horario (dia, hora_inicio, hora_fin, id_horario) VALUES (1, '07:00', '09:00', 1);
        INSERT INTO tiempos_horario (dia, hora_inicio, hora_fin, id_horario) VALUES (3, '07:00', '09:00', 1);
        INSERT INTO tiempos_horario (dia, hora_inicio, hora_fin, id_horario) VALUES (2, '09:00', '11:00', 2);
        INSERT INTO tiempos_horario (dia, hora_inicio, hora_fin, id_horario) VALUES (4, '09:00', '11:00', 2);
        INSERT INTO tiempos_horario (dia, hora_inicio, hora_fin, id_horario) VALUES (3, '09:00', '11:00', 3);
        """)

    conexion.commit()
    conexion.close()


if __name__ == "__main__":
    crear_tablas()
    print("La base de datos ha sido creada:", ruta_db)