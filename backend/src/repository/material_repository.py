from src.schema.material import Material, MaterialActualizar
from src.database import get_connection


class MaterialRepository:

    async def mostrarMateriales(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id,
                   curso_id,
                   titulo,
                   descripcion,
                   tipo,
                   archivo_url,
                   fecha_subida
            FROM materiales
        """)

        materiales = []
        for row in cursor.fetchall():
            materiales.append({
                "id": row.id,
                "curso_id": row.curso_id,
                "titulo": row.titulo,
                "descripcion": row.descripcion,
                "tipo": row.tipo,
                "archivo_url": row.archivo_url,
                "fecha_subida": row.fecha_subida
            })

        conn.close()
        return materiales

    async def agregarMaterial(self, material: Material):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO materiales
            (curso_id, titulo, descripcion, tipo, archivo_url, fecha_subida)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            material.curso_id,
            material.titulo,
            material.descripcion,
            material.tipo,
            material.archivo_url,
            material.fecha_subida
        ))

        conn.commit()
        conn.close()

        return {"mensaje": "Material agregado correctamente"}

    async def actualizarMaterial(self, id: int, material: MaterialActualizar):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE materiales
            SET curso_id = ?,
                titulo = ?,
                descripcion = ?,
                tipo = ?,
                archivo_url = ?,
                fecha_subida = ?
            WHERE id = ?
        """, (
            material.curso_id,
            material.titulo,
            material.descripcion,
            material.tipo,
            material.archivo_url,
            material.fecha_subida,
            id
        ))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Material no encontrado"}

        return {"mensaje": "Material actualizado correctamente"}

    async def eliminarMaterial(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM materiales
            WHERE id = ?
        """, (id,))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        if filas == 0:
            return {"mensaje": "Material no encontrado"}

        return {"mensaje": "Material eliminado correctamente"}