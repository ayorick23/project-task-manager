-- Creación de la Base de Datos
CREATE DATABASE ProyectoDB;
GO

USE ProyectoDB;
GO

-- Tabla de Usuarios
CREATE TABLE Usuarios (
    UsuarioID INT IDENTITY(1,1) PRIMARY KEY,
    Nombre NVARCHAR(100) NOT NULL,
    Apellido NVARCHAR(100) NOT NULL,
    Contraseña NVARCHAR(255) NOT NULL, -- Almacenar hash, no contraseñas en texto plano
    CorreoElectronico NVARCHAR(150) NOT NULL UNIQUE,
    Carrera NVARCHAR(100) NOT NULL,
    Genero CHAR(1) NOT NULL, -- 'M', 'F', 'O' (otro)
    FechaRegistro DATETIME DEFAULT GETDATE(),
    Foto NVARCHAR(255) -- Ruta al archivo de imagen
);
GO

-- Tabla de Profesores
CREATE TABLE Profesores (
    ProfesorID INT IDENTITY(1,1) PRIMARY KEY,
    Nombre NVARCHAR(100) NOT NULL,
    Apellido NVARCHAR(100) NOT NULL,
    CorreoElectronico NVARCHAR(150) NOT NULL UNIQUE,
);
GO

-- Tabla de Áreas de Formación
CREATE TABLE AreasFormacion (
    AreaFormacionID INT IDENTITY(1,1) PRIMARY KEY,
    Nombre NVARCHAR(100) NOT NULL UNIQUE
);
GO

-- Tabla de Materias
CREATE TABLE Materias (
    MateriaID INT IDENTITY(1,1) PRIMARY KEY,
    Codigo NVARCHAR(20) NOT NULL UNIQUE,
    Nombre NVARCHAR(100) NOT NULL,
    ProfesorID INT,
    Ciclo NVARCHAR(20), -- Ej: "2023-2", "2024-1"
    Seccion NVARCHAR(10), -- Ej: "A", "B", "C"
    Icono NVARCHAR(255), -- Ruta al ícono o nombre del ícono en el sistema
    Horario NVARCHAR(255), -- Formato: "Lunes 10:00-12:00, Miércoles 14:00-16:00"
    AreaFormacionID INT,
    RequisitosPrevios NVARCHAR(255), -- Códigos de materias separados por comas
    UnidadesValorativas INT DEFAULT 0,
    FOREIGN KEY (ProfesorID) REFERENCES Profesores(ProfesorID),
    FOREIGN KEY (AreaFormacionID) REFERENCES AreasFormacion(AreaFormacionID)
);
GO

-- Tabla de Tareas
CREATE TABLE Tareas (
    TareaID INT IDENTITY(1,1) PRIMARY KEY,
    MateriaID INT NOT NULL,
    Titulo NVARCHAR(100) NOT NULL,
    Descripcion NVARCHAR(MAX),
    Semana INT, -- Número de semana en el ciclo
    FechaCreacion DATETIME DEFAULT GETDATE(),
    FechaEntrega DATETIME NOT NULL,
    Observaciones NVARCHAR(MAX),
    FOREIGN KEY (MateriaID) REFERENCES Materias(MateriaID)
);
GO

-- Tabla de Apuntes
CREATE TABLE Apuntes (
    ApunteID INT IDENTITY(1,1) PRIMARY KEY,
    MateriaID INT NOT NULL,
    UsuarioID INT NOT NULL,
    FechaClase DATE NOT NULL,
    Titulo NVARCHAR(100) NOT NULL,
    Contenido NVARCHAR(MAX),
    Adjuntos NVARCHAR(255), -- Rutas a archivos adjuntos separadas por comas
    FechaCreacion DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (MateriaID) REFERENCES Materias(MateriaID),
    FOREIGN KEY (UsuarioID) REFERENCES Usuarios(UsuarioID)
);
GO

-- Tabla de Sesiones (para gestión de autenticación)
CREATE TABLE Sesiones (
    SesionID INT IDENTITY(1,1) PRIMARY KEY,
    UsuarioID INT NOT NULL,
    TokenSesion NVARCHAR(255) NOT NULL UNIQUE,
    FechaCreacion DATETIME DEFAULT GETDATE(),
    FechaExpiracion DATETIME,
    DireccionIP NVARCHAR(50),
    DispositivoInfo NVARCHAR(255),
    UltimaActividad DATETIME,
    FOREIGN KEY (UsuarioID) REFERENCES Usuarios(UsuarioID)
);
GO

-- Agregar datos a las Áreas de Formación
INSERT INTO AreasFormacion (Nombre)
VALUES 
    ('Conocimientos Básicos'),
    ('Desarrollo de Software'),
    ('Ciencia de Datos');
GO

-- Agregar datos a Materias