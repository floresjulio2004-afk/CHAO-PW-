USE CHAO;
GO

CREATE TABLE dbo.TiempoHorario(
    id_tiempo INT PRIMARY KEY,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    dia NVARCHAR(25) NOT NULL,
    id_horario INT NOT NULL,
    CONSTRAINT FK_TiempoHorario_Horario
        FOREIGN KEY (id_horario)
        REFERENCES dbo.Horario(id_horario)
);
GO