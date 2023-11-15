class IteradorPrestamosDemorados:
    def __int__(self, listaPrestamos:list):
        self.listaPrestamos = listaPrestamos

    def listaPrestamosDemorados(self):
        for prestamo in self.listaPrestamos:
            demora= prestamo.calcularDemora()
            if demora > 0:
                #linea = "El libro " + str(prestamo.libro.get_titulo()) + "tiene una demora de " + str(demora) + "dias"
                dato=[str(prestamo.libro.get_titulo()),str(demora)]
                listaDemoras.append(dato)
            return listaDemoras
