from Biblioteca18.Clase.estado import Estado


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