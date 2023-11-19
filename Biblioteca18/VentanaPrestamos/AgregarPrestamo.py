
from tkinter import ttk
from tkinter import *
from CRUD.administrarPrestamo import *
from Entidades.prestamo import Prestamo
from datetime import datetime
class AgregarPrestamo:
    def __init__(self, padron, datos=[]):
        self.window = Tk()
        self.window.title("Alta de Prestamos")
        self.padron = padron
        self.datos = datos

        frame1 = Frame(self.window)
        frame1.pack(pady=20, padx=10)
        frame2 = Frame(self.window)
        frame2.pack(pady=5, padx=5)

        self.dni = IntVar(self.window)
        self.codigo = IntVar(self.window)
        self.fechaPrestamo = StringVar(self.window)
        self.diasPactados = StringVar(self.window)
        self.fechaDevolucion = StringVar(self.window)

        Label(frame1, text="Dni del Socio:").grid(row=0, column=0)
        dni = Entry(frame1, textvariable=self.dni)
        dni.grid(row=0, column=1)
        Label(frame1, text="Codigo del libro:").grid(row=1, column=0)
        codigo = Entry(frame1, textvariable=self.codigo)
        codigo.grid(row=1, column=1) 
        Label(frame1, text="Fecha del Prestamo:").grid(row=2, column=0)
        fechaPrestamo = Entry(frame1, textvariable=self.fechaPrestamo)
        fechaPrestamo.grid(row=2, column=1)
        Label(frame1, text="Dias Pactados:").grid(row=3, column=0)
        diasPactados = Entry(frame1, textvariable=self.diasPactados)
        diasPactados.grid(row=3, column=1)

        if self.datos == []:
            Button(frame2, text="Agregar", command=self.agregar_Prestamo).pack(side="left", padx=10)
        else:
            dni.config(state='readonly')
            codigo.config(state='readonly')
            fechaPrestamo.config(state='readonly')
            diasPactados.config(state='readonly')
            Label(frame1, text="Fecha de Devolución:").grid(row=4, column=0)
            Entry(frame1, textvariable=self.fechaDevolucion).grid(row=4, column=1)

            for item in self.datos.selection():
                value = self.datos.item(item, 'values')
            self.dni.set(value[0])
            self.codigo.set(value[1])
            fecha = datetime.strptime(value[2], '%Y-%m-%d %H:%M:%S')
            self.fechaPrestamo.set(fecha.strftime('%d/%m/%Y'))
            self.diasPactados.set(value[3])
            fechaD = value[4] if value[4] == '' else datetime.strptime(value[4], '%Y-%m-%d %H:%M:%S')
            self.fechaDevolucion.set(fechaD if fechaD == '' else fechaD.strftime('%d/%m/%Y'))
            self.prestamo = Prestamo(self.fechaPrestamo.get(), self.padron.libros[int(self.codigo.get())], self.padron.socios[int(self.dni.get())], self.diasPactados.get(), None if self.fechaDevolucion.get() == '' else self.fechaDevolucion.get())

            Button(frame2, text="Editar", command=self.editar_Prestamo).pack(side="left", padx=10)
        
        Button(frame2, text="Cancelar", command=self.window.destroy).pack(side="right", padx=10)


    def mostrar(self):
        self.window.mainloop()

        # Función para agregar un Prestamo a la lista
    def agregar_Prestamo(self):
        dni = self.dni.get()
        codigo = self.codigo.get()
        fechaPrestamo = self.fechaPrestamo.get()
        diasPactados = self.diasPactados.get()
        # self.lista_Prestamos.insert("", "end", values=(dni, codigo, fechaPrestamo, diasPactados, fechaDevolucion))
        prestamo = Prestamo(fechaPrestamo, self.padron.libros[codigo], self.padron.socios[dni], diasPactados, None)
        try:
            cargar_prestamo(prestamo)
        except Exception as e:
            print(f"Error al agregar el prestamo: {e}")
        else:
            print("Prestamo cargado")
        
        self.dni.set("")
        self.codigo.set("")
        self.fechaPrestamo.set("")
        self.diasPactados.set("")


    # Función para editar un Prestamo seleccionado
    def editar_Prestamo(self):

        dni = self.dni.get()
        codigo = self.codigo.get()
        fecha_prestamo = self.fechaPrestamo.get()
        dias_pactados = self.diasPactados.get()
        fecha_devolucion = self.fechaDevolucion.get()
        nuevo = Prestamo(fecha_prestamo, self.padron.libros[codigo], self.padron.socios[dni], dias_pactados, fecha_devolucion)
        try:
            modificar_prestamo(self.prestamo, nuevo)
        except Exception as e:
            print(f"Error al modificar el prestamo: {e}")
        else:
            print("Prestamo modificado")
            
        # self.lista_Prestamos.insert("", "end", values=(dni, codigo, fechaPrestamo, diasPactados, fechaDevolucion))
        self.dni.set("")
        self.codigo.set("")
        self.fechaPrestamo.set("")
        self.diasPactados.set("")
        self.fechaDevolucion.set("")