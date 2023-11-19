from Estados.estado import Estado


class Prestado(Estado):
    def esExtraviado(self):
        return False

    def esPrestado(self):
        return True

    def esDisponible(self):
        return False

    def getNombre(self):
        return "Prestado"

    def getDescripcion(self):
        return "El libro está prestado a un usuario."
    def __str__(self):
        return self.getNombre()
    def getCodigo(self):
        return 2