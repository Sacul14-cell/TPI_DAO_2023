from datetime import *
class Socio():
    def __init__(self, dni:int, nombre:str, apellido:str):
        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido
        self._fechaHoraAlta = f'{datetime.today().strftime("%Y-%m-%d %H:%M:%S")}'
    @property
    def dni(self):
        return self._dni
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def set_dni(self, dni):
        self._dni = dni

    @property
    def fechaAlta(self):
        return self._fechaHoraAlta
    
    @property
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def set_apellido(self, apellido):
        self._apellido = apellido
    
    
    def __str__(self):
        return f"{self.dni} {self.nombre} {self.apellido} {self.fechaAlta}"