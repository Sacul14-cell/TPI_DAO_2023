from Estados.estado import Estado


class Libro:
    def __init__(self, codigo, titulo, precio_reposicion, estado:Estado):
        self.codigo = codigo
        self.titulo = titulo
        self.precio_reposicion = precio_reposicion
        self.estado = estado

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_precio_reposicion(self):
        return self.precio_reposicion

    def set_precio_reposicion(self, precio_reposicion):
        self.precio_reposicion = precio_reposicion

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

    def __str__(self):
        return f"Libro [Codigo: {self.codigo}, Título: {self.titulo}]"
    
    def estaPrestado(self):
        return self.estado.esPrestado()

    def estaDisponible(self):
        return self.estado.esDisponible()

    def estaExtraviado(self):
        return self.estado.esExtraviado()