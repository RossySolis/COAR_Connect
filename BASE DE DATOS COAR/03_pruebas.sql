USE COAR_CONNECT;
GO

-- 1. Cantidad de registros por tabla
SELECT 'roles' AS tabla, COUNT(*) AS total FROM roles
UNION ALL SELECT 'usuarios', COUNT(*) FROM usuarios
UNION ALL SELECT 'docentes', COUNT(*) FROM docentes
UNION ALL SELECT 'estudiantes', COUNT(*) FROM estudiantes
UNION ALL SELECT 'padres', COUNT(*) FROM padres
UNION ALL SELECT 'cursos', COUNT(*) FROM cursos
UNION ALL SELECT 'horarios', COUNT(*) FROM horarios
UNION ALL SELECT 'inscripciones', COUNT(*) FROM inscripciones
UNION ALL SELECT 'materiales', COUNT(*) FROM materiales
UNION ALL SELECT 'simulacros', COUNT(*) FROM simulacros
UNION ALL SELECT 'resultados', COUNT(*) FROM resultados
UNION ALL SELECT 'seguimiento_academico', COUNT(*) FROM seguimiento_academico;

-- 2. Usuarios con roles
SELECT 
    u.id,
    u.nombre,
    u.apellido,
    u.correo,
    r.nombre AS rol,
    u.estado
FROM usuarios u
INNER JOIN roles r ON u.rol_id = r.id;

-- 3. Cursos con docentes
SELECT 
    c.nombre AS curso,
    c.area,
    c.nivel,
    u.nombre + ' ' + u.apellido AS docente
FROM cursos c
INNER JOIN docentes d ON c.docente_id = d.id
INNER JOIN usuarios u ON d.usuario_id = u.id;

-- 4. Estudiantes inscritos en cursos
SELECT 
    u.nombre + ' ' + u.apellido AS estudiante,
    c.nombre AS curso,
    h.dia,
    h.hora_inicio,
    h.hora_fin,
    i.estado
FROM inscripciones i
INNER JOIN estudiantes e ON i.estudiante_id = e.id
INNER JOIN usuarios u ON e.usuario_id = u.id
INNER JOIN horarios h ON i.horario_id = h.id
INNER JOIN cursos c ON h.curso_id = c.id;

-- 5. Materiales por curso
SELECT 
    c.nombre AS curso,
    m.titulo,
    m.tipo,
    m.archivo_url
FROM materiales m
INNER JOIN cursos c ON m.curso_id = c.id;

-- 6. Resultados de simulacros
SELECT 
    u.nombre + ' ' + u.apellido AS estudiante,
    s.titulo AS simulacro,
    r.puntaje,
    r.fecha_realizacion,
    r.observacion
FROM resultados r
INNER JOIN estudiantes e ON r.estudiante_id = e.id
INNER JOIN usuarios u ON e.usuario_id = u.id
INNER JOIN simulacros s ON r.simulacro_id = s.id;

-- 7. Seguimiento académico
SELECT 
    u.nombre + ' ' + u.apellido AS estudiante,
    c.nombre AS curso,
    sa.avance_porcentaje,
    sa.horas_estudio,
    sa.asistencia_porcentaje,
    sa.recomendacion
FROM seguimiento_academico sa
INNER JOIN estudiantes e ON sa.estudiante_id = e.id
INNER JOIN usuarios u ON e.usuario_id = u.id
INNER JOIN cursos c ON sa.curso_id = c.id;

-- 8. Dashboard estudiante
SELECT 
    u.nombre + ' ' + u.apellido AS estudiante,
    COUNT(DISTINCT i.id) AS cursos_inscritos,
    COUNT(DISTINCT r.id) AS simulacros_realizados,
    AVG(r.puntaje) AS promedio_simulacros
FROM estudiantes e
INNER JOIN usuarios u ON e.usuario_id = u.id
LEFT JOIN inscripciones i ON e.id = i.estudiante_id
LEFT JOIN resultados r ON e.id = r.estudiante_id
GROUP BY u.nombre, u.apellido;

-- 9. Dashboard padre
SELECT 
    up.nombre + ' ' + up.apellido AS padre,
    ue.nombre + ' ' + ue.apellido AS estudiante,
    c.nombre AS curso,
    sa.avance_porcentaje,
    sa.asistencia_porcentaje,
    sa.recomendacion
FROM padres p
INNER JOIN usuarios up ON p.usuario_id = up.id
INNER JOIN estudiantes e ON p.estudiante_id = e.id
INNER JOIN usuarios ue ON e.usuario_id = ue.id
INNER JOIN seguimiento_academico sa ON e.id = sa.estudiante_id
INNER JOIN cursos c ON sa.curso_id = c.id;

-- 10. Promedio por curso
SELECT 
    c.nombre AS curso,
    AVG(r.puntaje) AS promedio_puntaje
FROM resultados r
INNER JOIN simulacros s ON r.simulacro_id = s.id
INNER JOIN cursos c ON s.curso_id = c.id
GROUP BY c.nombre;
GO