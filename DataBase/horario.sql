USE CHAO;
GO

CREATE TABLE dbo.Horario(
    id_horario INT PRIMARY KEY,
    estado NVARCHAR(20) NOT NULL,
    observacion NVARCHAR(200),
    id_periodo INT NOT NULL,
    id_paralelo INT NOT NULL,
    CONSTRAINT FK_Horario_Periodo
        FOREIGN KEY (id_periodo)
        REFERENCES dbo.PeriodoAcademico(id_periodo),
    CONSTRAINT FK_Horario_Paralelo
        FOREIGN KEY (id_paralelo)
        REFERENCES dbo.Paralelo(id_paralelo)
);
GO