USE CHAO;
GO

CREATE TABLE dbo.Horario_Aula(
    id_horario INT NOT NULL,
    id_aula INT NOT NULL,
    PRIMARY KEY (id_horario, id_aula),
    CONSTRAINT FK_HorarioAula_Horario
        FOREIGN KEY (id_horario)
        REFERENCES dbo.Horario(id_horario),
    CONSTRAINT FK_HorarioAula_Aula
        FOREIGN KEY (id_aula)
        REFERENCES dbo.Aula(id_aula)
);
GO