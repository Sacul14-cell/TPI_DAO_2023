from Entidades.socio import *
from db import *

def cargar_socio(socio):
    db1 = DBConnection('./TPI_DAO_2023/Biblioteca18/biblioteca.db')
    cursor = db1.conn.cursor()
    datos = (f"{socio.dni}", f"{socio.nombre}", f"{socio.apellido}", f"{socio.fechaAlta}")
    insert = "INSERT INTO socio (dni, nombre, apellido, fechaHoraAlta) VALUES (?, ?, ?, ?)"
    cursor.execute(insert, datos)
    db1.conn.commit()
 
    
def eliminar_socio_db(socio):
    db1 = DBConnection('./TPI_DAO_2023/Biblioteca18/biblioteca.db')
    cursor = db1.conn.cursor()
    delete = f"DELETE FROM socio WHERE dni = {socio.dni}"
    cursor.execute(delete)
    db1.conn.commit()
  

def modificar_socio(socio, nuevo):
    db1 = DBConnection('./TPI_DAO_2023/Biblioteca18/biblioteca.db')
    cursor = db1.conn.cursor()
    datos = (f"{nuevo.dni}", f"{nuevo.nombre}", f"{nuevo.apellido}")
    update = f"UPDATE socio SET dni = ?, nombre = ?, apellido = ? WHERE dni = {socio.dni}"
    cursor.execute(update, datos)
    db1.conn.commit()


def consultar_socio():
    db1 = DBConnection('./TPI_DAO_2023/Biblioteca18/biblioteca.db')
    cursor = db1.conn.cursor()
    cursor.execute("SELECT * FROM socio")
    result = cursor.fetchall()
    db1.conn.commit()
    return result
