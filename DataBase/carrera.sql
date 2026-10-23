USE CHAO;
GO

CREATE TABLE dbo.Carrera(
    id_carrera INT PRIMARY KEY,
    nombre NVARCHAR(120) NOT NULL,
    codigo INT NOT NULL,
    id_facultad INT NOT NULL,
    CONSTRAINT FK_Carrera_Facultad
        FOREIGN KEY (id_facultad)
        REFERENCES dbo.Facultad(id_facultad)
);
GO