USE CHAO;
GO

CREATE TABLE dbo.Horario(
    id_horario INT PRIMARY KEY, 
    estado NVARCHAR(20),
    observacion NVARCHAR(200)
);