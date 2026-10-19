USE CHAO;
GO


CREATE TABLE dbo.Coordinador(
    id_usuario INT PRIMARY KEY
    CONSTRAINT FK_Coordinador_Usuario
        FOREIGN KEY(id_usuario)
        REFERENCES dbo.Usuario(id_usuario)
);
GO