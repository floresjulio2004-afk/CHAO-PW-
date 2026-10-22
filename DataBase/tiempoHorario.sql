USE CHAO;
GO

CREATE TABLE dbo.TiempoHorario(
    id_tiempo INT PRIMARY KEY,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    dia NVARCHAR(25) NOT NULL
);
