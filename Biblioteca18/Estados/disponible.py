from Estados.estado import Estado


class Disponible(Estado):
    def esExtraviado(self):
        return False

    def esPrestado(self):
        return False

    def esDisponible(self):
        return True

    def getNombre(self):
        return "Disponible"

    def getDescripcion(self):
        return "El libro está disponible para ser prestado."
    def __str__(self):
        return self.getNombre()