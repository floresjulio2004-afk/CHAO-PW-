USE CHAO;
GO

CREATE TABLE dbo.Horario(
    id_horario INT PRIMARY KEY, 
    estado NVARCHAR(20) NOT NULL,
    observacion NVARCHAR(200) NULL
);
