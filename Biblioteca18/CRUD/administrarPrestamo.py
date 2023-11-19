from Entidades.prestamo import *
from db import *
from datetime import *
def cargar_prestamo(prestamo):
    db1 = DBConnection('biblioteca.db')
    cursor = db1.conn.cursor()
    datos = (f"{prestamo.fecha_prestamo.strftime('%d/%m/%Y')}", f"{prestamo.plazo}", f"{prestamo.socio.dni}", f"{prestamo.libro.codigo}")
    insert = "INSERT INTO prestamo (fechaPrestamo, diasPactados, socio_dni, libro_codigo) VALUES (?, ?, ?, ?)"
    cursor.execute(insert, datos)
    db1.conn.commit()
 
def eliminar_prestamo_db(prestamo):
    db1 = DBConnection('biblioteca.db')
    cursor = db1.conn.cursor()
    delete = f"DELETE FROM prestamo WHERE fechaPrestamo = {prestamo.fecha_prestamo.strftime('%d/%m/%Y')}"
    cursor.execute(delete)
    db1.conn.commit()
  

def modificar_prestamo(prestamo, nuevo):
    db1 = DBConnection('biblioteca.db')
    cursor = db1.conn.cursor()
    nueva_fecha_devolucion = nuevo.fecha_devolucion.strftime('%d/%m/%Y') if nuevo.fecha_devolucion else None
    datos = (
        prestamo.fecha_prestamo.strftime('%d/%m/%Y'),
        prestamo.plazo,
        prestamo.socio.dni,
        prestamo.libro.codigo,
        nueva_fecha_devolucion
    )
    update = """
        UPDATE prestamo
        SET fechaPrestamo = ?,
            diasPactados = ?,
            socio_dni = ?,
            libro_codigo = ?,
            fechaDevolucion = ?
        WHERE fechaPrestamo = ?
    """
    cursor.execute(update, datos + (prestamo.fecha_prestamo.strftime('%d/%m/%Y'),))
    db1.conn.commit()


def consultar_prestamo():
    db1 = DBConnection('biblioteca.db')
    cursor = db1.conn.cursor()
    cursor.execute("SELECT * FROM prestamo")
    result = cursor.fetchall()
    db1.conn.commit()
    return result
