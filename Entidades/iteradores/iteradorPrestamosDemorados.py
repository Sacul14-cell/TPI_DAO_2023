class iteradorPrestamosDemorados:
    def __int__(self, listaPrestamos:list):
        self.listaPrestamos = listaPrestamos

    def listaPrestamosDemorados(self):
        listaDemoras = []
        for prestamo in self.listaPrestamos:
            demora= prestamo.calcularDemora()
            if demora > 0:
                linea = "El libro " + str(prestamo.libro.get_titulo()) + "tiene una demora de " + str(demora) + "dias"
                listaDemoras.append(linea)
            return listaDemoras