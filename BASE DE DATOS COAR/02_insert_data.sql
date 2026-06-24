USE COAR_CONNECT;
GO

-- =====================================================
-- ROLES
-- =====================================================
INSERT INTO roles (nombre, descripcion) VALUES
('administrador', 'Gestiona toda la plataforma'),
('estudiante', 'Accede a cursos, materiales y simulacros'),
('padre', 'Visualiza el avance académico de su hijo'),
('docente', 'Gestiona cursos, horarios y materiales');

-- =====================================================
-- USUARIOS
-- rol_id:
-- 1 = administrador
-- 2 = estudiante
-- 3 = padre
-- 4 = docente
-- =====================================================
INSERT INTO usuarios (nombre, apellido, correo, password, rol_id, telefono, estado) VALUES
('Admin', 'COAR', 'admin@coar.com', '123456', 1, '900000001', 'activo'),

('Rosa', 'Quispe', 'rosa@coar.com', '123456', 4, '900000002', 'activo'),
('Luis', 'Mendoza', 'luis@coar.com', '123456', 4, '900000003', 'activo'),
('Carmen', 'Torres', 'carmen@coar.com', '123456', 4, '900000004', 'activo'),

('Camila', 'Solis', 'camila@coar.com', '123456', 2, '900000005', 'activo'),
('Diego', 'Ramos', 'diego@coar.com', '123456', 2, '900000006', 'activo'),
('Valeria', 'Torres', 'valeria@coar.com', '123456', 2, '900000007', 'activo'),
('Miguel', 'Huaman', 'miguel@coar.com', '123456', 2, '900000008', 'activo'),
('Lucia', 'Chavez', 'lucia@coar.com', '123456', 2, '900000009', 'activo'),

('Walter', 'Solis', 'walter@coar.com', '123456', 3, '900000010', 'activo'),
('Juana', 'Hinostroza', 'juana@coar.com', '123456', 3, '900000011', 'activo'),
('Carlos', 'Ramos', 'carlos@coar.com', '123456', 3, '900000012', 'activo');

-- =====================================================
-- DOCENTES
-- usuarios 2, 3, 4 son docentes
-- =====================================================
INSERT INTO docentes (usuario_id, especialidad, experiencia) VALUES
(2, 'Matemática y Razonamiento Matemático', '5 años de experiencia'),
(3, 'Comunicación y Razonamiento Verbal', '4 años de experiencia'),
(4, 'Ciencia, Tecnología e Inglés', '6 años de experiencia');

-- =====================================================
-- PADRES
-- usuarios 10, 11, 12 son padres
-- Se registran ANTES que los estudiantes
-- =====================================================
INSERT INTO padres (usuario_id, parentesco, codigo_vinculacion) VALUES
(10, 'Padre', 'PADRE100001'),
(11, 'Madre', 'PADRE100002'),
(12, 'Padre', 'PADRE100003');

-- =====================================================
-- ESTUDIANTES
-- usuarios 5, 6, 7, 8, 9 son estudiantes
-- padre_id:
-- 1 = Walter Solis
-- 2 = Juana Hinostroza
-- 3 = Carlos Ramos
-- =====================================================
INSERT INTO estudiantes (usuario_id, padre_id, grado, colegio, distrito) VALUES
(5, 1, '2do de secundaria', 'Colegio Estatal de El Tambo', 'El Tambo'),
(6, 3, '2do de secundaria', 'I.E. Santa Isabel', 'Huancayo'),
(7, 2, '1ro de secundaria', 'I.E. Nuestra Señora del Rosario', 'Huancayo'),
(8, 1, '3ro de secundaria', 'I.E. Mariscal Castilla', 'El Tambo'),
(9, 3, '2do de secundaria', 'I.E. San Juan Bosco', 'Pilcomayo');

-- =====================================================
-- CURSOS
-- =====================================================
INSERT INTO cursos (nombre, descripcion, area, nivel, docente_id, estado) VALUES
('Matemática Básica COAR', 'Curso de reforzamiento matemático', 'Matemática', 'Básico', 1, 'activo'),
('Razonamiento Matemático', 'Series, patrones y lógica matemática', 'Matemática', 'Intermedio', 1, 'activo'),
('Comunicación', 'Comprensión lectora y producción de textos', 'Comunicación', 'Básico', 2, 'activo'),
('Razonamiento Verbal', 'Analogías, sinónimos, antónimos e inferencias', 'Comunicación', 'Intermedio', 2, 'activo'),
('Ciencia y Tecnología', 'Conceptos científicos para admisión COAR', 'Ciencias', 'Básico', 3, 'activo'),
('Inglés Básico', 'Vocabulario y comprensión básica en inglés', 'Inglés', 'Básico', 3, 'activo');

-- =====================================================
-- HORARIOS
-- =====================================================
INSERT INTO horarios (curso_id, dia, hora_inicio, hora_fin, modalidad, cupos, estado) VALUES
(1, 'Lunes', '16:00', '17:30', 'Virtual', 30, 'activo'),
(2, 'Martes', '16:00', '17:30', 'Virtual', 30, 'activo'),
(3, 'Miércoles', '16:00', '17:30', 'Virtual', 30, 'activo'),
(4, 'Jueves', '16:00', '17:30', 'Virtual', 30, 'activo'),
(5, 'Viernes', '16:00', '17:30', 'Virtual', 30, 'activo'),
(6, 'Sábado', '09:00', '10:30', 'Virtual', 30, 'activo'),
(1, 'Lunes', '18:00', '19:30', 'Virtual', 25, 'activo'),
(3, 'Miércoles', '18:00', '19:30', 'Virtual', 25, 'activo');

-- =====================================================
-- INSCRIPCIONES
-- =====================================================
INSERT INTO inscripciones (estudiante_id, horario_id, fecha_inscripcion, estado) VALUES
(1, 1, '2026-07-01', 'activo'),
(1, 3, '2026-07-01', 'activo'),
(2, 1, '2026-07-01', 'activo'),
(2, 2, '2026-07-01', 'activo'),
(3, 3, '2026-07-02', 'activo'),
(3, 4, '2026-07-02', 'activo'),
(4, 5, '2026-07-03', 'activo'),
(4, 6, '2026-07-03', 'activo'),
(5, 1, '2026-07-04', 'activo'),
(5, 5, '2026-07-04', 'activo');

-- =====================================================
-- MATERIALES
-- =====================================================
INSERT INTO materiales (curso_id, titulo, descripcion, tipo, archivo_url, fecha_subida) VALUES
(1, 'Guía de Matemática', 'Ejercicios de fracciones y porcentajes', 'PDF', '/materiales/matematica_guia.pdf', '2026-07-01'),
(1, 'Práctica de Porcentajes', 'Problemas resueltos paso a paso', 'PDF', '/materiales/porcentajes.pdf', '2026-07-02'),
(2, 'Series y Patrones', 'Ejercicios de razonamiento matemático', 'PDF', '/materiales/series_patrones.pdf', '2026-07-02'),
(3, 'Comprensión Lectora', 'Lecturas con preguntas', 'PDF', '/materiales/comprension.pdf', '2026-07-03'),
(4, 'Analogías Verbales', 'Práctica de razonamiento verbal', 'PDF', '/materiales/analogias.pdf', '2026-07-03'),
(5, 'Ciencia y Tecnología', 'Resumen de conceptos científicos', 'PDF', '/materiales/ciencia.pdf', '2026-07-04'),
(6, 'Inglés Básico', 'Vocabulario y lecturas cortas', 'PDF', '/materiales/ingles.pdf', '2026-07-04');

-- =====================================================
-- SIMULACROS
-- =====================================================
INSERT INTO simulacros (curso_id, titulo, descripcion, fecha_publicacion, tiempo_minutos, estado) VALUES
(1, 'Simulacro Matemática 01', 'Primer simulacro de matemática', '2026-07-10', 60, 'activo'),
(2, 'Simulacro Razonamiento Matemático 01', 'Evaluación de lógica y patrones', '2026-07-11', 60, 'activo'),
(3, 'Simulacro Comunicación 01', 'Evaluación de comprensión lectora', '2026-07-12', 60, 'activo'),
(4, 'Simulacro Razonamiento Verbal 01', 'Evaluación verbal inicial', '2026-07-13', 60, 'activo'),
(5, 'Simulacro Ciencia y Tecnología 01', 'Evaluación de ciencias', '2026-07-14', 60, 'activo');

-- =====================================================
-- RESULTADOS
-- =====================================================
INSERT INTO resultados (estudiante_id, simulacro_id, puntaje, fecha_realizacion, observacion) VALUES
(1, 1, 15.5, '2026-07-10', 'Buen desempeño en matemática'),
(1, 3, 14.0, '2026-07-12', 'Debe mejorar comprensión lectora'),
(2, 1, 13.5, '2026-07-10', 'Necesita reforzar porcentajes'),
(2, 2, 14.5, '2026-07-11', 'Buen avance en lógica'),
(3, 3, 16.0, '2026-07-12', 'Buena comprensión lectora'),
(3, 4, 15.0, '2026-07-13', 'Buen razonamiento verbal'),
(4, 5, 13.0, '2026-07-14', 'Debe reforzar ciencias'),
(5, 1, 17.0, '2026-07-10', 'Excelente resultado'),
(5, 5, 15.5, '2026-07-14', 'Buen desempeño general');

-- =====================================================
-- SEGUIMIENTO ACADÉMICO
-- =====================================================
INSERT INTO seguimiento_academico (
    estudiante_id, curso_id, avance_porcentaje, horas_estudio,
    asistencia_porcentaje, recomendacion, fecha_registro
) VALUES
(1, 1, 70, 14, 95, 'Mantener ritmo de práctica matemática', '2026-07-15'),
(1, 3, 55, 10, 90, 'Practicar textos largos', '2026-07-15'),
(2, 1, 45, 8, 85, 'Reforzar fracciones y porcentajes', '2026-07-15'),
(2, 2, 50, 9, 88, 'Practicar series numéricas', '2026-07-15'),
(3, 3, 75, 12, 92, 'Continuar con lectura diaria', '2026-07-15'),
(3, 4, 65, 11, 90, 'Reforzar analogías', '2026-07-15'),
(4, 5, 40, 7, 80, 'Repasar conceptos científicos básicos', '2026-07-15'),
(4, 6, 45, 8, 82, 'Practicar vocabulario básico', '2026-07-15'),
(5, 1, 85, 16, 98, 'Mantener desempeño destacado', '2026-07-15'),
(5, 5, 70, 13, 94, 'Seguir practicando problemas de ciencias', '2026-07-15');
GO
