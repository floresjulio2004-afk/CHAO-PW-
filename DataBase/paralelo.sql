USE CHAO;
GO

CREATE TABLE dbo.Paralelo(
    id_paralelo INT PRIMARY KEY,
    id_nivel INT NOT NULL,
    nombre NVARCHAR(120) NOT NULL,
    descripcion NVARCHAR(120),
    id_carrera INT NOT NULL,
    CONSTRAINT FK_Paralelo_NivelEducativo
        FOREIGN KEY (id_nivel)
        REFERENCES dbo.NivelEducativo(id_nivel),
    CONSTRAINT FK_Paralelo_Carrera
        FOREIGN KEY (id_carrera)
        REFERENCES dbo.Carrera(id_carrera)
);
GO