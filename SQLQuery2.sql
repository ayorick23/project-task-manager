SELECT * FROM Materias
SELECT * FROM Profesores
SELECT * FROM Usuarios

INSERT INTO Materias (Icono) VALUES(
	'C:\Users\Dereck\Documents\UEES\PROGRAMACIÓN I\Project\src\assets\programacion.png',
	'C:\Users\Dereck\Documents\UEES\PROGRAMACIÓN I\Project\src\assets\sistemas-operativos.png',
	'C:\Users\Dereck\Documents\UEES\PROGRAMACIÓN I\Project\src\assets\matematica.png',
	'C:\Users\Dereck\Documents\UEES\PROGRAMACIÓN I\Project\src\assets\fisica.png',
	'C:\Users\Dereck\Documents\UEES\PROGRAMACIÓN I\Project\src\assets\etica.png'
)

UPDATE Materias
SET Icono = 'C:\Users\Dereck\Documents\UEES\PROGRAMACIÓN I\Project\src\assets\etica.png'
WHERE MateriaID = 5

ALTER TABLE Usuarios DROP COLUMN Apellido
ALTER TABLE Usuarios ALTER COLUMN Carrera NVARCHAR(100) NULL
ALTER TABLE Usuarios ALTER COLUMN Genero NVARCHAR(100) NULL
ALTER TABLE Usuarios ALTER COLUMN Carrera NVARCHAR(100) NULL