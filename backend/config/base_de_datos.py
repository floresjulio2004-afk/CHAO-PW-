
import os
import pyodbc


def obtener_conexion():
    servidor = os.getenv("DB_SERVER")
    base_de_datos = os.getenv("DB_NAME")
    usuario = os.getenv("DB_USER")
    contrasena = os.getenv("DB_PASSWORD")

    cadena_conexion = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={servidor};"
        f"DATABASE={base_de_datos};"
        f"UID={usuario};"
        f"PWD={contrasena};"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
        "Connection Timeout=5;"
    )

    return pyodbc.connect(cadena_conexion)