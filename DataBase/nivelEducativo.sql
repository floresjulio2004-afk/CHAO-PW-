USE CHAO;
GO

CREATE TABLE dbo.NivelEducativo(
    id_nivel INT PRIMARY KEY,
    nombre NVARCHAR(50) NOT NULL, 
    decripcion NVARCHAR(200) NOT NULL
);
