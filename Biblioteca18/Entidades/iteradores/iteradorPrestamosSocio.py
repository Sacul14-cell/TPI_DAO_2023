class iteradorPrestamosSocio:
    def __init__(self, listaPrestamos: list):
        self.listaPrestamos=listaPrestamos

    def listaPrestamosSocio(self, dniSocio: int):
        libros=[]
        for prestamo in self.listaPrestamos:
            if prestamo.socio.dni == dniSocio:
                libros.append(prestamo.__str__())
        return libros