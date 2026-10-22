USE CHAO;
GO

CREATE TABLE dbo.Asignatura(
    id_asignatura INT PRIMARY KEY,
    codigo INT NOT NULL, 
    nombre NVARCHAR(50)
    credito INT NOT NULL,
    hora TIME NOT NULL,
);