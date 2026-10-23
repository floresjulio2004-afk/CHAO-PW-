USE CHAO;
GO

CREATE TABLE dbo.Aula(
    id_aula INT PRIMARY KEY,
    nombre NVARCHAR(150) NOT NULL,
    capacidad INT NOT NULL,
    tipo NVARCHAR(50) NOT NULL,
    disponibilidad NVARCHAR(30) NOT NULL
);
GO