from datetime import datetime, timedelta
from Estados.estado import Estado

class Prestamo:
    def __init__(self, fecha_prestamo, libro, socio, fechaDevEstipulada, fecha_devolucion):
        self.fecha_prestamo = datetime.strptime(fecha_prestamo, '%d/%m/%Y')
        self.plazo=fechaDevEstipulada
        self.libro = libro
        self.socio = socio
        self.fecha_devolucion = None if fecha_devolucion is None else datetime.strptime(fecha_devolucion, '%d/%m/%Y')

    def devolverLibro(self):
        self.fecha_devolucion = obtenerFechaActual()
        if self.fecha_devolucion > self.fecha_prestamo:
            demora = self.calcular_demora()
            if demora > 0:
                print(f"Libro devuelto con demora de {demora} días.")
            else:
                print("Libro devuelto a tiempo.")
        else:
            print("Error: La fecha de devolución debe ser posterior a la fecha de préstamo.")

    def libroExtraviado(self, estadoExtraviado: Estado):
        self.libro.set_estado(estadoExtraviado)
        print("Libro extraviado. Se aplicarán las medidas correspondientes.")
        print(self.libro)

    def calcularDemora(self):
        if self.fecha_devolucion:
            demora = (self.fecha_devolucion - self.fecha_prestamo).days
            return int(demora)
        else:
            ahora = obtenerFechaActual()
            demora = (ahora - self.fecha_prestamo).days
            return int(demora)
    def __str__(self):
        return f"Fecha Prestamo: {self.fecha_prestamo}, Fecha Devolucion: {self.fecha_devolucion}, Libro: {self.libro}, Plazo: {self.plazo}"
def obtenerFechaActual():
        return datetime.now()

