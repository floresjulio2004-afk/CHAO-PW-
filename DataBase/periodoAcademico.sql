USE CHAO;
GO

CREATE TABLE dbo.PeriodoAcademico(
    id_periodo INT PRIMARY KEY,
    nombre NVARCHAR(100) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    estado NVARCHAR(30) NOT NULL
);
GO