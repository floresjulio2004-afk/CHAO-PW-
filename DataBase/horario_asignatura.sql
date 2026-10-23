USE CHAO;
GO

CREATE TABLE dbo.Horario_Asignatura(
    id_horario INT NOT NULL,
    id_asignatura INT NOT NULL,
    PRIMARY KEY (id_horario, id_asignatura),
    CONSTRAINT FK_HorarioAsignatura_Horario
        FOREIGN KEY (id_horario)
        REFERENCES dbo.Horario (id_horario),
    CONSTRAINT FK_HorarioAsignatura_Asignatura
        FOREIGN KEY (id_asignatura)
        REFERENCES dbo.Asignatura (id_asignatura),    
);
GO