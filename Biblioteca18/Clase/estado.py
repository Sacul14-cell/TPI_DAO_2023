from abc import ABC, abstractmethod

class Estado(ABC):
    @abstractmethod
    def esExtraviado(self):
        pass

    @abstractmethod
    def esPrestado(self):
        pass

    @abstractmethod
    def esDisponible(self):
        pass

    @abstractmethod
    def getNombre(self):
        pass

    @abstractmethod
    def getDescripcion(self):
        pass
