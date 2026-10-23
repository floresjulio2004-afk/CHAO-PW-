USE CHAO;
GO

CREATE TABLE dbo.Estudiante(
    id_usuario INT PRIMARY KEY,
    nivel NVARCHAR(50) NOT NULL,
    id_carrera INT NOT NULL,
    id_paralelo INT NOT NULL,
    CONSTRAINT FK_Estudiante_Usuario
        FOREIGN KEY (id_usuario)
        REFERENCES dbo.Usuario(id_usuario),
    CONSTRAINT FK_Estudiante_Carrera
        FOREIGN KEY (id_carrera)
        REFERENCES dbo.Carrera(id_carrera),
    CONSTRAINT FK_Estudiante_Paralelo
        FOREIGN KEY (id_paralelo)
        REFERENCES dbo.Paralelo(id_paralelo)
);
GO