class IteradorPrestamosDemorados():
    def __init__(self, listaPrestamos):
        self.listaPrestamos = listaPrestamos

    def listaPrestamosDemorados(self):
        listaDemoras = []
        for prestamo in self.listaPrestamos:
            demora= prestamo.calcularDemora()
            if demora > 0:
                #linea = "El libro " + str(prestamo.libro.get_titulo()) + "tiene una demora de " + str(demora) + "dias"
                dato=[str(prestamo.libro.get_titulo()),str(demora)]
                listaDemoras.append(dato)
        return listaDemoras
