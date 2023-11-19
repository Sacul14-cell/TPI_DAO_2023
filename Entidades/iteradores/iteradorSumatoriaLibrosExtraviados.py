class IteradorSumatoriaLibrosExtraviados:
    def __init__(self, listaLibros:list):
        self.listaLibros=listaLibros

    def sumarReposiciónLibrosExtraviados(self):
        suma=0
        contador=0
        for libro in self.listaLibros.values():
            if libro.estaExtraviado():
                suma += float(libro.get_precio_reposicion())
                contador +=1
        datos=[contador,suma]
        return datos
