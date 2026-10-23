USE CHAO;
GO

CREATE TABLE dbo.Incidencia(
    id_incidencia INT PRIMARY KEY,
    descripcion NVARCHAR(120) NOT NULL,
    fecha DATE NOT NULL,
    tipo NVARCHAR(120) NOT NULL,
    estado NVARCHAR(120) NOT NULL,
    id_usuario INT NOT NULL,
    CONSTRAINT FK_Incidencia_Usuario
        FOREIGN KEY (id_usuario)
        REFERENCES dbo.Usuario(id_usuario)
);
GO