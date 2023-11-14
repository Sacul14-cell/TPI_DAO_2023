from Entidades.libro import Libro
from Entidades.socio import Socio
from Entidades.prestamo import Prestamo
from Estados.disponible import Disponible
from Estados.extraviado import Extraviado
from Estados.prestado import Prestado
from db import DBConnection
class Biblioteca:
    def __init__(self) -> None:
        # Colecciones
        estado = [Disponible, Prestado, Extraviado]
        self.libros = set()
        self.socios = set()
        self.prestamos = set()
        # Conexion a la base de datos
        self.db = DBConnection('biblioteca.db')

        # agregar Libros
        res = self.db.execute('SELECT * FROM libro')
        for i in res:
            lib = Libro(int(i[0]), i[1], float(i[2]), estado[int(i[3])-1]())
            self.agregarLibro(lib)
        # Agregar socios
        res = self.db.execute('SELECT * FROM socio')
        for i in res:
            s = Socio(int(i[0]), str(i[1]), str(i[2]))
            self.agregarSocio(s)
        # Agregar Prestamos
        res = self.db.execute('SELECT * FROM prestamo')
        for i in res:
            p = Prestamo(str(i[0]), int(i[1]), int(i[2]), int(i[3]))
            self.agregarPrestamo(p)

    
    def agregarLibro(self, libro):
        self.libros.add(libro)

    def agregarSocio(self, socio):
        self.socios.add(socio)
    
    def agregarPrestamo(self, prestamo):
        self.prestamos.add(prestamo)
    