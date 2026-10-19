USE CHAO;
GO

CREATE TABLE dbo.Incidencia(
    id_incidencia INTEGER PRIMARY KEY,
    descripción NVARCHAR(120),
    fecha DATE,
    tipo NVARCHAR(120),
    estado NVARCHAR(120)
);
