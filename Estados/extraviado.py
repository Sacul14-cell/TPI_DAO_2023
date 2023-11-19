from Estados.estado import Estado


class Extraviado(Estado):
    def esExtraviado(self):
        return True

    def esPrestado(self):
        return False

    def esDisponible(self):
        return False

    def getNombre(self):
        return "Extraviado"

    def getDescripcion(self):
        return "El libro está extraviado."
    def __str__(self):
        return self.getNombre()
    def getCodigo(self):
        return 3