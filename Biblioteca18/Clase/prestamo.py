from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, fecha_prestamo, libro, socio):
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = None
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

    def libroExtraviado(self):
        # Lógica para manejar un libro extraviado (puedes personalizar según tus necesidades)
        print("Libro extraviado. Se aplicarán las medidas correspondientes.")

    def calcularDemora(self):
        if self.fecha_devolucion:
            demora = (self.fecha_devolucion - self.fecha_prestamo).days
            return max(demora, 0)
        else:
            print("Error: El libro aún no ha sido devuelto.")
            return 0

def obtenerFechaActual():
    return datetime.now()