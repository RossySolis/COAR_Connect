-- ============================================================
-- COAR CONNECT - DROP ALL TABLES
-- Ejecutar ANTES de 01_DDL_create_tables_coar_connect.sql
-- Elimina tablas en orden inverso de dependencia (FKs)
-- PostgreSQL 15+ | Base de datos: coar_connect
-- ============================================================

-- ============================================================
-- PASO 0: OPCIÓN NUCLEAR
-- Elimina TODO el schema public y lo recrea limpio
-- USAR SOLO EN AMBIENTE DE DESARROLLO / LOCAL
-- ============================================================

-- DROP SCHEMA public CASCADE;
-- CREATE SCHEMA public;

-- ============================================================
-- PASO 1: DROP TABLAS DE EVALUACIONES Y SIMULACROS
-- Primero se eliminan las tablas que dependen de simulacros,
-- estudiantes, preguntas y alternativas.
-- ============================================================

DROP TABLE IF EXISTS RESPUESTAS_ESTUDIANTE CASCADE;
DROP TABLE IF EXISTS ALTERNATIVAS CASCADE;
DROP TABLE IF EXISTS PREGUNTAS CASCADE;
DROP TABLE IF EXISTS RESULTADOS_SIMULACRO CASCADE;
DROP TABLE IF EXISTS RESULTADOS CASCADE;
DROP TABLE IF EXISTS SIMULACROS CASCADE;
DROP TABLE IF EXISTS TIPOS_SIMULACRO CASCADE;

-- ============================================================
-- PASO 2: DROP TABLAS DE SEGUIMIENTO ACADÉMICO
-- Relacionadas con avance, notas, asistencia, recomendaciones
-- y progreso del estudiante.
-- ============================================================

DROP TABLE IF EXISTS RECOMENDACIONES_ACADEMICAS CASCADE;
DROP TABLE IF EXISTS ASISTENCIAS CASCADE;
DROP TABLE IF EXISTS PROGRESO_CURSO CASCADE;
DROP TABLE IF EXISTS SEGUIMIENTO_ACADEMICO CASCADE;
DROP TABLE IF EXISTS METAS_ESTUDIANTE CASCADE;

-- ============================================================
-- PASO 3: DROP TABLAS DE INSCRIPCIONES Y HORARIOS
-- Dependen de estudiantes, horarios y cursos.
-- ============================================================

DROP TABLE IF EXISTS INSCRIPCIONES CASCADE;
DROP TABLE IF EXISTS HORARIOS CASCADE;
DROP TABLE IF EXISTS MODALIDADES_CLASE CASCADE;

-- ============================================================
-- PASO 4: DROP TABLAS DE MATERIALES EDUCATIVOS
-- Relacionadas con cursos, docentes y recursos de estudio.
-- ============================================================

DROP TABLE IF EXISTS MATERIAL_VISUALIZADO CASCADE;
DROP TABLE IF EXISTS MATERIALES CASCADE;
DROP TABLE IF EXISTS TIPOS_MATERIAL CASCADE;

-- ============================================================
-- PASO 5: DROP TABLAS DE CURSOS
-- Cursos de reforzamiento, áreas académicas y niveles.
-- ============================================================

DROP TABLE IF EXISTS CURSOS CASCADE;
DROP TABLE IF EXISTS AREAS_ACADEMICAS CASCADE;
DROP TABLE IF EXISTS NIVELES_CURSO CASCADE;

-- ============================================================
-- PASO 6: DROP TABLAS DEL CALENDARIO COAR
-- Eventos visibles para estudiantes y padres.
-- ============================================================

DROP TABLE IF EXISTS CALENDARIO_COAR CASCADE;
DROP TABLE IF EXISTS TIPOS_EVENTO_COAR CASCADE;

-- ============================================================
-- PASO 7: DROP TABLAS DE PORTAL DE PADRES
-- Relación padre/apoderado con estudiante.
-- ============================================================

DROP TABLE IF EXISTS PADRES_ESTUDIANTES CASCADE;
DROP TABLE IF EXISTS PADRES CASCADE;
DROP TABLE IF EXISTS PARENTESCOS CASCADE;

-- ============================================================
-- PASO 8: DROP TABLAS DE PERFILES DE USUARIO
-- Estudiantes y docentes dependen de usuarios.
-- ============================================================

DROP TABLE IF EXISTS DOCENTES CASCADE;
DROP TABLE IF EXISTS ESTUDIANTES CASCADE;
DROP TABLE IF EXISTS GRADOS_ACADEMICOS CASCADE;
DROP TABLE IF EXISTS DISTRITOS CASCADE;

-- ============================================================
-- PASO 9: DROP TABLAS DE AUTENTICACIÓN Y USUARIOS
-- Usuarios depende de roles.
-- ============================================================

DROP TABLE IF EXISTS SESIONES_USUARIO CASCADE;
DROP TABLE IF EXISTS USUARIOS CASCADE;
DROP TABLE IF EXISTS ROLES CASCADE;

-- ============================================================
-- PASO 10: DROP TABLAS ANTIGUAS O DE PRUEBA
-- Por si quedaron nombres anteriores durante el desarrollo.
-- ============================================================

DROP TABLE IF EXISTS USUARIO CASCADE;
DROP TABLE IF EXISTS ROL CASCADE;
DROP TABLE IF EXISTS ESTUDIANTE CASCADE;
DROP TABLE IF EXISTS PADRE CASCADE;
DROP TABLE IF EXISTS DOCENTE CASCADE;
DROP TABLE IF EXISTS CURSO CASCADE;
DROP TABLE IF EXISTS HORARIO CASCADE;
DROP TABLE IF EXISTS INSCRIPCION CASCADE;
DROP TABLE IF EXISTS MATERIAL CASCADE;
DROP TABLE IF EXISTS SIMULACRO CASCADE;
DROP TABLE IF EXISTS RESULTADO CASCADE;

-- ============================================================
-- VERIFICACIÓN OPCIONAL
-- Ejecutar después del DROP para comprobar que no quedan tablas.
-- ============================================================

-- SELECT tablename
-- FROM pg_tables
-- WHERE schemaname = 'public'
-- ORDER BY tablename;

-- Resultado esperado: 0 filas