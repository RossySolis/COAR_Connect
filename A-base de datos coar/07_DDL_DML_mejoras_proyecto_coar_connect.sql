-- ============================================================
-- COAR CONNECT - 07_DDL_DML_MEJORAS_PROYECTO.SQL
-- Mejoras finales del proyecto
-- Ejecutar DESPUÉS de los scripts 00 al 06
-- PostgreSQL 15+ | Base de datos: coar_connect
-- ============================================================

BEGIN;

-- ============================================================
-- A. TABLA PARA COMENTARIOS DE PADRES
-- Permite que el padre/apoderado deje observaciones sobre el avance.
-- ============================================================

CREATE TABLE IF NOT EXISTS COMENTARIOS_PADRES (
    PKCOMENTARIOPADRE SERIAL PRIMARY KEY,
    PKPADRE INT NOT NULL REFERENCES PADRES(PKPADRE) ON DELETE CASCADE,
    PKESTUDIANTE INT NOT NULL REFERENCES ESTUDIANTES(PKESTUDIANTE) ON DELETE CASCADE,
    TITULO VARCHAR(120) NOT NULL,
    COMENTARIO TEXT NOT NULL,
    FECHACOMENTARIO TIMESTAMP NOT NULL DEFAULT NOW(),
    ESTADO CHAR(1) NOT NULL DEFAULT '1',
    FECULTACTUALIZACION TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS IX_COMENTARIOS_PADRES_EST
ON COMENTARIOS_PADRES(PKESTUDIANTE);

-- ============================================================
-- B. TABLA PARA MENSAJES ENTRE USUARIOS
-- Sirve para comunicación docente-estudiante-padre.
-- ============================================================

CREATE TABLE IF NOT EXISTS MENSAJES_USUARIO (
    PKMENSAJE BIGSERIAL PRIMARY KEY,
    PKUSUARIO_EMISOR INT NOT NULL REFERENCES USUARIOS(PKUSUARIO) ON DELETE CASCADE,
    PKUSUARIO_RECEPTOR INT NOT NULL REFERENCES USUARIOS(PKUSUARIO) ON DELETE CASCADE,
    ASUNTO VARCHAR(120) NOT NULL,
    MENSAJE TEXT NOT NULL,
    FECHAENVIO TIMESTAMP NOT NULL DEFAULT NOW(),
    LEIDO CHAR(1) NOT NULL DEFAULT 'N',
    FECULTACTUALIZACION TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS IX_MENSAJES_RECEPTOR
ON MENSAJES_USUARIO(PKUSUARIO_RECEPTOR);

-- ============================================================
-- C. TABLA PARA EVIDENCIAS DE ACTIVIDAD
-- Guarda evidencias como tareas, prácticas o capturas.
-- ============================================================

CREATE TABLE IF NOT EXISTS EVIDENCIAS_ESTUDIANTE (
    PKEVIDENCIA SERIAL PRIMARY KEY,
    PKESTUDIANTE INT NOT NULL REFERENCES ESTUDIANTES(PKESTUDIANTE) ON DELETE CASCADE,
    PKCURSO INT REFERENCES CURSOS(PKCURSO) ON DELETE SET NULL,
    TITULO VARCHAR(150) NOT NULL,
    DESCRIPCION TEXT,
    ARCHIVO_URL TEXT,
    FECHASUBIDA TIMESTAMP NOT NULL DEFAULT NOW(),
    ESTADO CHAR(1) NOT NULL DEFAULT '1',
    FECULTACTUALIZACION TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS IX_EVIDENCIAS_ESTUDIANTE
ON EVIDENCIAS_ESTUDIANTE(PKESTUDIANTE);

-- ============================================================
-- D. TABLA PARA AUDITORÍA SIMPLE
-- Registra acciones importantes dentro del sistema.
-- ============================================================

CREATE TABLE IF NOT EXISTS AUDITORIA_SISTEMA (
    PKAUDITORIA BIGSERIAL PRIMARY KEY,
    PKUSUARIO INT REFERENCES USUARIOS(PKUSUARIO) ON DELETE SET NULL,
    TABLA_AFECTADA VARCHAR(80),
    ACCION VARCHAR(30) NOT NULL,
    DESCRIPCION TEXT,
    FECHAACCION TIMESTAMP NOT NULL DEFAULT NOW(),
    IP_ACCESO VARCHAR(50)
);

CREATE INDEX IF NOT EXISTS IX_AUDITORIA_USUARIO
ON AUDITORIA_SISTEMA(PKUSUARIO);

-- ============================================================
-- E. INSERTAR COMENTARIOS DE PADRES DE PRUEBA
-- ============================================================

INSERT INTO COMENTARIOS_PADRES (
    PKPADRE, PKESTUDIANTE, TITULO, COMENTARIO
) VALUES
((SELECT PKPADRE FROM PADRES WHERE CODPADRE='PAD000001'),
 (SELECT PKESTUDIANTE FROM ESTUDIANTES WHERE CODESTUDIANTE='EST000001'),
 'Seguimiento de avance',
 'Solicito conocer en qué temas debe reforzar mi hija esta semana.'),

((SELECT PKPADRE FROM PADRES WHERE CODPADRE='PAD000003'),
 (SELECT PKESTUDIANTE FROM ESTUDIANTES WHERE CODESTUDIANTE='EST000002'),
 'Consulta sobre asistencia',
 'Deseo saber por qué mi hijo no asistió a la última clase virtual.'),

((SELECT PKPADRE FROM PADRES WHERE CODPADRE='PAD000005'),
 (SELECT PKESTUDIANTE FROM ESTUDIANTES WHERE CODESTUDIANTE='EST000004'),
 'Reforzamiento adicional',
 'Me gustaría que se le recomiende más material de Ciencia y Tecnología.');

-- ============================================================
-- F. INSERTAR MENSAJES DE PRUEBA
-- ============================================================

INSERT INTO MENSAJES_USUARIO (
    PKUSUARIO_EMISOR, PKUSUARIO_RECEPTOR, ASUNTO, MENSAJE
) VALUES
((SELECT PKUSUARIO FROM USUARIOS WHERE CODUSUARIO='USR000002'),
 (SELECT PKUSUARIO FROM USUARIOS WHERE CODUSUARIO='USR000007'),
 'Reforzar matemática',
 'Camila, revisa la práctica de fracciones antes del próximo simulacro.'),

((SELECT PKUSUARIO FROM USUARIOS WHERE CODUSUARIO='USR000015'),
 (SELECT PKUSUARIO FROM USUARIOS WHERE CODUSUARIO='USR000002'),
 'Consulta de padre',
 'Profesora, quisiera saber cómo va el avance de Camila en matemática.'),

((SELECT PKUSUARIO FROM USUARIOS WHERE CODUSUARIO='USR000003'),
 (SELECT PKUSUARIO FROM USUARIOS WHERE CODUSUARIO='USR000008'),
 'Comunicación',
 'Diego, debes practicar comprensión lectora con textos más largos.');

-- ============================================================
-- G. INSERTAR EVIDENCIAS DE PRUEBA
-- ============================================================

INSERT INTO EVIDENCIAS_ESTUDIANTE (
    PKESTUDIANTE, PKCURSO, TITULO, DESCRIPCION, ARCHIVO_URL
) VALUES
((SELECT PKESTUDIANTE FROM ESTUDIANTES WHERE CODESTUDIANTE='EST000001'),
 (SELECT PKCURSO FROM CURSOS WHERE CODCURSO='CUR000001'),
 'Práctica de fracciones resuelta',
 'Evidencia de ejercicios desarrollados por la estudiante.',
 '/evidencias/est000001/fracciones_resueltas.pdf'),

((SELECT PKESTUDIANTE FROM ESTUDIANTES WHERE CODESTUDIANTE='EST000002'),
 (SELECT PKCURSO FROM CURSOS WHERE CODCURSO='CUR000002'),
 'Práctica de razonamiento matemático',
 'Resolución de ejercicios de series numéricas.',
 '/evidencias/est000002/series_numericas.pdf');

-- ============================================================
-- H. INSERTAR AUDITORÍA INICIAL
-- ============================================================

INSERT INTO AUDITORIA_SISTEMA (
    PKUSUARIO, TABLA_AFECTADA, ACCION, DESCRIPCION, IP_ACCESO
) VALUES
((SELECT PKUSUARIO FROM USUARIOS WHERE CODUSUARIO='USR000001'),
 'SISTEMA',
 'CARGA_INICIAL',
 'Se ejecutó el script 07 de mejoras del proyecto COAR Connect.',
 '127.0.0.1');

COMMIT;

-- ============================================================
-- VERIFICACIÓN OPCIONAL
-- ============================================================

-- SELECT * FROM COMENTARIOS_PADRES;
-- SELECT * FROM MENSAJES_USUARIO;
-- SELECT * FROM EVIDENCIAS_ESTUDIANTE;
-- SELECT * FROM AUDITORIA_SISTEMA;