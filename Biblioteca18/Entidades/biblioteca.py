from Entidades.libro import Libro
from Entidades.socio import Socio
from Entidades.prestamo import Prestamo
from Estados.disponible import Disponible
from Estados.extraviado import Extraviado
from Estados.prestado import Prestado
from CRUD.administrarSocio import *
from CRUD.administrarLibro import *
from CRUD.administrarPrestamo import *
from db import DBConnection
class Biblioteca:
    def __init__(self) -> None:
        # Colecciones
        estado = [Disponible, Prestado, Extraviado]
        self.libros = dict()
        self.socios = dict()
        self.prestamos = set()
        # Conexion a la base de datos
        # self.db = DBConnection('./TPI_DAO_2023/Biblioteca18/biblioteca.db')

        # agregar Libros
        res = consultar_libro()
        for i in res:
            lib = Libro(int(i[0]), i[1], float(i[2]), estado[int(i[3])-1]())
            self.agregarLibro(lib)
        # Agregar socios
        res = consultar_socio()
        for i in res:
            s = Socio(int(i[0]), str(i[1]), str(i[2]))
            self.agregarSocio(s)
        # Agregar Prestamos
        res = consultar_prestamo()
        for i in res:
            p = Prestamo(str(i[0]), self.libros[int(i[3])], self.socios[int(i[2])], str(i[1]))
            self.agregarPrestamo(p)

    
    def agregarLibro(self, libro):
        self.libros[libro.codigo] = libro

    def agregarSocio(self, socio):
        self.socios[socio.dni] = socio
    
    def agregarPrestamo(self, prestamo):
        self.prestamos.add(prestamo)

    def getLibros(self):
        return self.libros
    
    def getSocios(self):
        return self.socios
    
    def getPrestamos(self):
        return self.prestamos
    
