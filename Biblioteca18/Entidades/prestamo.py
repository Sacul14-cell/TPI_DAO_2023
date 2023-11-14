from datetime import datetime, timedelta
from Estados.estado import Estado

class Prestamo:
    def __init__(self, fecha_prestamo, libro, socio, fechaDevEstipulada):
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = None
        self.plazo=fechaDevEstipulada
        self.libro = libro
        self.socio = socio

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
            return max(demora, 0)
        else:
            demora = (self.plazo - self.fecha_prestamo).days
            return max(demora, 0)

def obtenerFechaActual():
    return datetime.now()