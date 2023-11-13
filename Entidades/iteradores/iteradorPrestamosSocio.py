class iteradorPrestamosSocio:
    def __int__(self, listaPrestamos: list):
        self.listaPrestamos=listaPrestamos

    def listaPrestamosSocio(self, dniSocio: int):
        libros=[]
        for prestamo in self.listaPrestamos:
            if prestamo.socio.dni == dniSocio:
                libros.append(prestamo.libro.get_titulo())
        return libros