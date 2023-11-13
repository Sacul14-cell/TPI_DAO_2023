class iteradorSumatoriaLibrosExtraviados:
    def __init__(self, listaLibros:list):
        self.listaLibros=listaLibros

    def sumarReposiciónLibrosExtraviados(self):
        suma=0
        for libro in self.listaLibros:
            if libro.estaExtraviado():
                suma += float(libro.get_precio_reposicion())
        return suma
