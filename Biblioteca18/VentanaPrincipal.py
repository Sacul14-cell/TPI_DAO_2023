from tkinter import *
from VentanaLibros.ListadoLibros import ListadoLibros
from VentanaPrestamos.ListadoPrestamos import ListadoPrestamos
from VentanaSocios.ListadoSocios import ListadoSocios
from VentanaReportes import VentanaReportes
class VentanaPrincipal:
    def __init__(self, padron):
        self.window = Tk()
        self.window.title("TPI-DAO")
        self.padron = padron
        frame1 = Frame()
        frame1.pack(pady=20, padx=20)
        frame2 = Frame()
        frame2.pack(pady=10, padx=10)
        

        Button(frame1, text="Administrar Libros", command=self.ListarLibros).pack(padx=10, pady=10)
        Button(frame1, text="Administrar Socios", command=self.ListarSocios).pack(padx=10, pady=10)
        Button(frame1, text="Administrar Prestamos/Devoluciones", command=self.ListarPrestamos).pack(padx=10, pady=10)

        
        Button(frame2, text="Generar Reportes", command=self.reportes).pack(padx=10)
        
        
    def mostrar(self):
        self.window.mainloop()
    
    def reportes(self):
        VentanaReportes(self.padron).mostrar()
    def ListarLibros(self):
        ListadoLibros(self.padron.libros).mostrar()
    def ListarSocios(self):
        ListadoSocios(self.padron.socios).mostrar()
    def ListarPrestamos(self):
        ListadoPrestamos(self.padron).mostrar()