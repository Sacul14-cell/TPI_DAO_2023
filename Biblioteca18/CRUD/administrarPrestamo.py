from Entidades.prestamo import *
from db import *

def cargar_prestamo(prestamo):
    db1 = DBConnection('./TPI_DAO_2023/Biblioteca18/biblioteca.db')
    cursor = db1.conn.cursor()
    datos = (f"{prestamo.fecha_prestamo}", f"{prestamo.plazo}", f"{prestamo.socio.dni}", f"{prestamo.libro.codigo}")
    insert = "INSERT INTO prestamo (fechaPrestamo, diasPactados, socio_dni, libro_codigo) VALUES (?, ?, ?, ?)"
    cursor.execute(insert, datos)
    db1.conn.commit()
 
def eliminar_prestamo_db(prestamo):
    db1 = DBConnection('./TPI_DAO_2023/Biblioteca18/biblioteca.db')
    cursor = db1.conn.cursor()
    delete = f"DELETE FROM prestamo WHERE fechaPrestamo = {prestamo.fecha_prestamo}"
    cursor.execute(delete)
    db1.conn.commit()
  

def modificar_prestamo(prestamo, nuevo):
    db1 = DBConnection('./TPI_DAO_2023/Biblioteca18/biblioteca.db')
    cursor = db1.conn.cursor()
    datos = (f"{nuevo.fecha_prestamo}", f"{nuevo.plazo}", f"{nuevo.socio.dni}", f"{nuevo.libro.codigo}")
    update = f"UPDATE prestamo SET fechaPrestamo = ?, diasPactados = ?, socio_dni = ?, libro_codigo = ? WHERE fechaPrestamo = {prestamo.fecha_prestamo}"
    cursor.execute(update, datos)
    db1.conn.commit()


def consultar_prestamo():
    db1 = DBConnection('./TPI_DAO_2023/Biblioteca18/biblioteca.db')
    cursor = db1.conn.cursor()
    cursor.execute("SELECT * FROM prestamo")
    result = cursor.fetchall()
    db1.conn.commit()
    return result
