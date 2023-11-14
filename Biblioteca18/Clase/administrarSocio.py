from socio import *
from db import *
import random
def cargar_socio(socio):
    db1 = DBConnection('biblioteca.db')
    cursor = db1.conn.cursor()
    datos = (f"{socio.dni}", f"{socio.nombre}", f"{socio.apellido}", f"{socio.fechaAlta}")
    insert = "INSERT INTO socio (dni, nombre, apellido, fechaHoraAlta) VALUES (?, ?, ?, ?)"
    cursor.execute(insert, datos)
    db1.conn.commit()
 
    
def eliminar_socio(socio):
    db1 = DBConnection('biblioteca.db')
    cursor = db1.conn.cursor()
    delete = f"DELETE FROM socio WHERE dni = {socio.dni}"
    cursor.execute(delete)
    db1.conn.commit()
  

def modificar_socio():
    pass


def consultar_socio():
    db1 = DBConnection('biblioteca.db')
    cursor = db1.conn.cursor()
    cursor.execute("SELECT * FROM socio")
    result = cursor.fetchall()
    db1.conn.commit()
    return result


"""for _ in range(50):
    nombres = [
    "Juan", "María", "José", "Ana", "Carlos", "Laura", "Luis", "Sofía", "Pablo", "Elena",
    "Pedro", "Carmen", "Fernando", "Isabel", "Miguel", "Lourdes", "Antonio", "Raquel", "Manuel", "Marta",
    "Ricardo", "Victoria", "Francisco", "Patricia", "Alejandro", "Beatriz", "Javier", "Eva", "Roberto", "Cristina",
    "David", "Natalia", "Jorge", "Andrea", "Adrián", "Rosa", "Alberto", "Nerea", "Gustavo", "Ivan",
    "Héctor", "Liliana", "Diego", "Verónica", "Emilio", "Cecilia", "Federico", "Alicia", "Oscar", "Luisa"
]
    apellidos = [
    "González", "Rodríguez", "Martínez", "Fernández", "López", "Pérez", "Gómez", "Sánchez", "Díaz", "Torres",
    "Ramírez", "Hernández", "Silva", "Jiménez", "Romero", "López", "Alvarez", "Giménez", "Vargas", "Castro",
    "Molina", "Paez", "Suárez", "Blanco", "Ferrer", "Rojas", "Navarro", "Morales", "Ríos", "Ortega",
    "Rivas", "Paredes", "Santos", "Cruz", "Mendoza", "Medina", "Fuentes", "Flores", "Campos", "Delgado", "Serrano",
    "Aguirre", "Peña", "Valenzuela", "Vega", "Cabrera", "Ponce", "Quintero", "Gallardo", "Montes", "Solís"
]
    dni = random.randint(10000001, 99999999)
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    socio = Socio(dni, nombre, apellido)
    cargar_socio(socio)"""
    
print(consultar_socio())