USE CHAO;
GO

CREATE TABLE dbo.NivelEducativo(
    id_nivel INT PRIMARY KEY,
    nombre NVARCHAR(50) NOT NULL,
    descripcion NVARCHAR(200) NOT NULL
);
GO