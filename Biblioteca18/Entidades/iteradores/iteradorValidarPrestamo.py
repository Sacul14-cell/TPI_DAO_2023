from Estados.prestado import Prestado

class iteradorValidarPrestamo:
    def __init__(self, listaPrestamos: list, dniSocio: int, estadoPrestado: Prestado):
        self.prestamos=listaPrestamos
        self.dniSocio=dniSocio
        self.estado=estadoPrestado

    def validarEstadoSocio(self):
        contador=0
        for prestamo in self.prestamos:
            if prestamo.socio.dni == self.dniSocio:
                if prestamo.calcularDemora() > 0:
                    return False
                elif prestamo.libro.get_estado() is Prestado:
                    contador += 1
            if contador > 3:
                return False
            else:
                return True