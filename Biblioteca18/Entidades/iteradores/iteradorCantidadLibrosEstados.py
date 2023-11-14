class iteradorCantidadLibrosEstados:
    def __init__(self, listaLibros:list, dniSocio: int):
        self.listaLibros=listaLibros

    def contarLibros(self):
        contador=[0,0,0]
        for libro in self.listaLibros:
            if libro.estaDisponible():
                contador[0] += 1
            elif libro.estaPrestado():
                contador[1] += 1
            elif libro.estaExtraviado():
                contador[2] += 1
        return contador