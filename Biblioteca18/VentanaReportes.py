
from tkinter import *
from tkinter import messagebox
class VentanaReportes:
    def __init__(self, padron):
        self.window = Tk()
        self.window.title("Reportes")
        self.padro = padron
        frame1 = Frame(self.window)
        frame1.pack(pady=20, padx=10)


        Label(frame1, text="Cantidad de libros en cada estado (tres totales)").grid(row=0, column=0)
        Button(frame1, text="Generar", command=self.reporte1).grid(row=0, column=1)
        Label(frame1, text="Sumatoria del precio de reposición de todos los libros extraviados").grid(row=1, column=0)
        Button(frame1, text="Generar", command=self.reporte2).grid(row=1, column=1)
        Label(frame1, text="Nombre de todos los solicitantes de un libro en particular identificado por su título").grid(row=2, column=0)
        Button(frame1, text="Generar", command=self.reporte3).grid(row=2, column=1)
        Label(frame1, text="Listado de préstamos de un socio identificado por su número de socio").grid(row=3, column=0)
        Button(frame1, text="Generar", command=self.reporte4).grid(row=3, column=1)
        Label(frame1, text="Listado de préstamos demorados").grid(row=4, column=0)
        Button(frame1, text="Generar", command=self.reporte5).grid(row=4, column=1)
        
        
    def reporte1(self):
        #messagebox.showinfo(title="Reporte", message=)
        pass
    def reporte2(self):
        #messagebox.showinfo(title="Reporte", message=)
        pass
    def reporte3(self):
        #messagebox.showinfo(title="Reporte", message=)
        pass
    def reporte4(self):
        #messagebox.showinfo(title="Reporte", message=)
        pass
    def reporte5(self):
        #messagebox.showinfo(title="Reporte", message=)
        pass
    
    def mostrar(self):
        self.window.mainloop()
        