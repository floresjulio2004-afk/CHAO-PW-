USE CHAO;
GO

CREATE TABLE dbo.Docente(
    id_usuario INT PRIMARY KEY,
    especialidad NVARCHAR(100) NOT NULL,
    CONSTRAINT FK_Docente_Usuario
        FOREIGN KEY (id_usuario)
        REFERENCES dbo.Usuario(id_usuario)
);
GO