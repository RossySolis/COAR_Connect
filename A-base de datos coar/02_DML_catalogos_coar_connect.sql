-- ============================================================
-- COAR CONNECT - 02_DML_CATALOGOS.SQL
-- Catálogos base — ejecutar después del 01_DDL_create_tables
-- PostgreSQL 15+ | Base de datos: coar_connect
-- ============================================================

BEGIN;

-- ============================================================
-- BLOQUE 1: ROLES
-- ============================================================

INSERT INTO ROLES (CODROL, NOMROL, DESROL) VALUES
('ADM','Administrador','Gestiona usuarios, cursos, inscripciones y reportes'),
('EST','Estudiante','Accede a cursos, materiales, simulacros y seguimiento'),
('PAD','Padre de familia','Visualiza el avance académico de su hijo'),
('DOC','Docente','Gestiona cursos, horarios, materiales y evaluaciones');

-- ============================================================
-- BLOQUE 2: DISTRITOS PRINCIPALES DE HUANCAYO
-- ============================================================

INSERT INTO DISTRITOS (CODDISTRITO, DEPARTAMENTO, PROVINCIA, DISTRITO) VALUES
('120101','Junín','Huancayo','Huancayo'),
('120104','Junín','Huancayo','El Tambo'),
('120106','Junín','Huancayo','Chilca'),
('120107','Junín','Huancayo','Chongos Alto'),
('120108','Junín','Huancayo','Chupuro'),
('120111','Junín','Huancayo','Huancán'),
('120112','Junín','Huancayo','Huasicancha'),
('120113','Junín','Huancayo','Huayucachi'),
('120114','Junín','Huancayo','Ingenio'),
('120116','Junín','Huancayo','Pilcomayo'),
('120117','Junín','Huancayo','Pucará'),
('120119','Junín','Huancayo','Sapallanga'),
('120120','Junín','Huancayo','Sicaya'),
('120121','Junín','Huancayo','Santo Domingo de Acobamba'),
('120122','Junín','Huancayo','Viques');

-- ============================================================
-- BLOQUE 3: GRADOS ACADÉMICOS
-- ============================================================

INSERT INTO GRADOS_ACADEMICOS (CODGRADO, DESGRADO, NIVEL) VALUES
('1S','1ro de secundaria','Secundaria'),
('2S','2do de secundaria','Secundaria'),
('3S','3ro de secundaria','Secundaria'),
('4S','4to de secundaria','Secundaria'),
('5S','5to de secundaria','Secundaria');

-- ============================================================
-- BLOQUE 4: PARENTESCOS
-- ============================================================

INSERT INTO PARENTESCOS (CODPARENTESCO, DESPARENTESCO) VALUES
('PAD','Padre'),
('MAD','Madre'),
('APO','Apoderado'),
('TIO','Tío/Tía'),
('HER','Hermano/Hermana'),
('ABU','Abuelo/Abuela');

-- ============================================================
-- BLOQUE 5: ÁREAS ACADÉMICAS
-- ============================================================

INSERT INTO AREAS_ACADEMICAS (CODAREAACADEMICA, DESAREAACADEMICA) VALUES
('MAT','Matemática'),
('COM','Comunicación'),
('RVM','Razonamiento Verbal'),
('RMT','Razonamiento Matemático'),
('CYT','Ciencia y Tecnología'),
('ING','Inglés'),
('GEN','Preparación General COAR');

-- ============================================================
-- BLOQUE 6: NIVELES DE CURSO
-- ============================================================

INSERT INTO NIVELES_CURSO (CODNIVELCURSO, DESNIVELCURSO) VALUES
('BAS','Básico'),
('INT','Intermedio'),
('AVA','Avanzado'),
('PRE','Pre-COAR');

-- ============================================================
-- BLOQUE 7: MODALIDADES DE CLASE
-- ============================================================

INSERT INTO MODALIDADES_CLASE (CODMODALIDADCLASE, DESMODALIDADCLASE) VALUES
('VIR','Virtual'),
('PRE','Presencial'),
('HIB','Híbrida'),
('GRA','Clase grabada');

-- ============================================================
-- BLOQUE 8: TIPOS DE MATERIAL
-- ============================================================

INSERT INTO TIPOS_MATERIAL (CODTIPOMATERIAL, DESTIPOMATERIAL) VALUES
('PDF','Documento PDF'),
('GUI','Guía de ejercicios'),
('VID','Video educativo'),
('LIN','Enlace externo'),
('PPT','Presentación'),
('PRA','Práctica dirigida');

-- ============================================================
-- BLOQUE 9: TIPOS DE SIMULACRO
-- ============================================================

INSERT INTO TIPOS_SIMULACRO (CODTIPOSIMULACRO, DESTIPOSIMULACRO) VALUES
('CUR','Simulacro por curso'),
('GEN','Simulacro general COAR'),
('DIA','Diagnóstico inicial'),
('REP','Repaso final');

-- ============================================================
-- BLOQUE 10: TIPOS DE EVENTO COAR
-- ============================================================

INSERT INTO TIPOS_EVENTO_COAR (CODTIPOEVENTOCOAR, DESTIPOEVENTOCOAR) VALUES
('ADM','Admisión COAR'),
('SIM','Simulacro'),
('CLA','Clase de reforzamiento'),
('CHA','Charla informativa'),
('MAT','Entrega de material'),
('EVA','Evaluación'),
('REC','Recomendación académica');

-- ============================================================
-- BLOQUE 11: ESTADOS DE INSCRIPCIÓN
-- ============================================================

INSERT INTO ESTADOS_INSCRIPCION (CODESTADOINSCRIPCION, DESESTADOINSCRIPCION) VALUES
('ACT','Activa'),
('CAN','Cancelada'),
('FIN','Finalizada'),
('PEN','Pendiente');

-- ============================================================
-- BLOQUE 12: ESTADOS DE EVALUACIÓN
-- ============================================================

INSERT INTO ESTADOS_EVALUACION (CODESTADOEVALUACION, DESESTADOEVALUACION) VALUES
('INI','Iniciado'),
('FIN','Finalizado'),
('PEN','Pendiente'),
('REV','Revisado'),
('ANU','Anulado');

-- ============================================================
-- BLOQUE 13: MEDALLAS / LOGROS
-- ============================================================

INSERT INTO MEDALLAS (CODMEDALLA, NOMMEDALLA, DESMEDALLA, ICONO_URL) VALUES
('M001','Primer curso inscrito','El estudiante se inscribió a su primer curso','/iconos/primer_curso.png'),
('M002','Primer simulacro','El estudiante completó su primer simulacro','/iconos/primer_simulacro.png'),
('M003','Constancia semanal','El estudiante cumplió su meta semanal','/iconos/constancia.png'),
('M004','Buen puntaje','El estudiante obtuvo una nota destacada','/iconos/buen_puntaje.png'),
('M005','Material completado','El estudiante revisó todos los materiales asignados','/iconos/materiales.png');

COMMIT;

-- ============================================================
-- VERIFICACIÓN OPCIONAL
-- ============================================================

-- SELECT * FROM ROLES;
-- SELECT * FROM DISTRITOS;
-- SELECT * FROM GRADOS_ACADEMICOS;
-- SELECT * FROM AREAS_ACADEMICAS;