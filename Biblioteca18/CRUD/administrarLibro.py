from Entidades.libro import *
from db import *

def cargar_libro(libro):
    db1 = DBConnection('./TPI_DAO_2023/Biblioteca18/biblioteca.db')
    cursor = db1.conn.cursor()
    datos = (f"{libro.codigo}", f"{libro.titulo}", f"{libro.precio_reposicion}", f"{libro.estado.getCodigo()}")
    insert = "INSERT INTO libro (codigo, titulo, precio, estado_idestado) VALUES (?, ?, ?, ?)"
    cursor.execute(insert, datos)
    db1.conn.commit()
 
def eliminar_libro_db(libro):
    db1 = DBConnection('./TPI_DAO_2023/Biblioteca18/biblioteca.db')
    cursor = db1.conn.cursor()
    delete = f"DELETE FROM libro WHERE codigo = {libro.codigo}"
    cursor.execute(delete)
    db1.conn.commit()
  

def modificar_libro(libro, nuevo):
    db1 = DBConnection('./TPI_DAO_2023/Biblioteca18/biblioteca.db')
    cursor = db1.conn.cursor()
    datos = (f"{nuevo.codigo}", f"{nuevo.titulo}", f"{nuevo.precio_reposicion}", f"{nuevo.estado.getCodigo()}")
    update = f"UPDATE libro SET codigo = ?, titulo = ?, precio = ?, estado_idestado = ? WHERE codigo = {libro.codigo}"
    cursor.execute(update, datos)
    db1.conn.commit()


def consultar_libro():
    db1 = DBConnection('./TPI_DAO_2023/Biblioteca18/biblioteca.db')
    cursor = db1.conn.cursor()
    cursor.execute("SELECT * FROM libro")
    result = cursor.fetchall()
    db1.conn.commit()
    return result
