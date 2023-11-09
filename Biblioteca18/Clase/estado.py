from abc import ABC, abstractmethod

class Estado(ABC):
    @abstractmethod
    def es_extraviado(self):
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
