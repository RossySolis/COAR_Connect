USE COAR_CONNECT;
GO

DROP TABLE IF EXISTS seguimiento_academico;
DROP TABLE IF EXISTS resultados;
DROP TABLE IF EXISTS simulacros;
DROP TABLE IF EXISTS materiales;
DROP TABLE IF EXISTS inscripciones;
DROP TABLE IF EXISTS horarios;
DROP TABLE IF EXISTS cursos;
DROP TABLE IF EXISTS docentes;
DROP TABLE IF EXISTS padres;
DROP TABLE IF EXISTS estudiantes;
DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS roles;
GO

CREATE TABLE roles (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    descripcion VARCHAR(150) NOT NULL
);

CREATE TABLE usuarios (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(80) NOT NULL,
    apellido VARCHAR(80) NOT NULL,
    correo VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    rol_id INT NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    FOREIGN KEY (rol_id) REFERENCES roles(id)
);

CREATE TABLE estudiantes (
    id INT IDENTITY(1,1) PRIMARY KEY,
    usuario_id INT NOT NULL,
    grado VARCHAR(50) NOT NULL,
    colegio VARCHAR(150) NOT NULL,
    distrito VARCHAR(100) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE padres (
    id INT IDENTITY(1,1) PRIMARY KEY,
    usuario_id INT NOT NULL,
    estudiante_id INT NOT NULL,
    parentesco VARCHAR(50) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id)
);

CREATE TABLE docentes (
    id INT IDENTITY(1,1) PRIMARY KEY,
    usuario_id INT NOT NULL,
    especialidad VARCHAR(100) NOT NULL,
    experiencia VARCHAR(150) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE cursos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    area VARCHAR(80) NOT NULL,
    nivel VARCHAR(50) NOT NULL,
    docente_id INT NOT NULL,
    estado VARCHAR(20) NOT NULL,
    FOREIGN KEY (docente_id) REFERENCES docentes(id)
);

CREATE TABLE horarios (
    id INT IDENTITY(1,1) PRIMARY KEY,
    curso_id INT NOT NULL,
    dia VARCHAR(30) NOT NULL,
    hora_inicio VARCHAR(20) NOT NULL,
    hora_fin VARCHAR(20) NOT NULL,
    modalidad VARCHAR(50) NOT NULL,
    cupos INT NOT NULL,
    estado VARCHAR(20) NOT NULL,
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

CREATE TABLE inscripciones (
    id INT IDENTITY(1,1) PRIMARY KEY,
    estudiante_id INT NOT NULL,
    horario_id INT NOT NULL,
    fecha_inscripcion VARCHAR(30) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
    FOREIGN KEY (horario_id) REFERENCES horarios(id)
);

CREATE TABLE materiales (
    id INT IDENTITY(1,1) PRIMARY KEY,
    curso_id INT NOT NULL,
    titulo VARCHAR(150) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    archivo_url VARCHAR(255) NOT NULL,
    fecha_subida VARCHAR(30) NOT NULL,
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

CREATE TABLE simulacros (
    id INT IDENTITY(1,1) PRIMARY KEY,
    curso_id INT NOT NULL,
    titulo VARCHAR(150) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    fecha_publicacion VARCHAR(30) NOT NULL,
    tiempo_minutos INT NOT NULL,
    estado VARCHAR(20) NOT NULL,
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

CREATE TABLE resultados (
    id INT IDENTITY(1,1) PRIMARY KEY,
    estudiante_id INT NOT NULL,
    simulacro_id INT NOT NULL,
    puntaje FLOAT NOT NULL,
    fecha_realizacion VARCHAR(30) NOT NULL,
    observacion VARCHAR(255) NOT NULL,
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
    FOREIGN KEY (simulacro_id) REFERENCES simulacros(id)
);

CREATE TABLE seguimiento_academico (
    id INT IDENTITY(1,1) PRIMARY KEY,
    estudiante_id INT NOT NULL,
    curso_id INT NOT NULL,
    avance_porcentaje FLOAT NOT NULL,
    horas_estudio INT NOT NULL,
    asistencia_porcentaje FLOAT NOT NULL,
    recomendacion VARCHAR(255) NOT NULL,
    fecha_registro VARCHAR(30) NOT NULL,
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);
GO
