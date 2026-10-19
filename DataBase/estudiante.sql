USE CHAO;
GO


CREATE TABLE dbo.Estudiante(
    id_usuario INT PRIMARY KEY,
    nivel NVARCHAR(20) NOT NULL,
    CONSTRAINT Fk_Estudiante_Usuario
        FOREIGN KEY(id_usuario)
        REFERENCES dbo.Usuario(id_usuario)
);