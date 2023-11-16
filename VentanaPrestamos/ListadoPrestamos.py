import tkinter as tk
from tkinter import ttk
from VentanaPrestamos.AgregarPrestamo import AgregarPrestamo
from CRUD.administrarPrestamo import *

class ListadoPrestamos:

    def agregar_Prestamo(self):
        AgregarPrestamo(self.padron).mostrar()
    def editar_Prestamo(self):
        AgregarPrestamo(self.padron, self.lista_Prestamos).mostrar()
    # Función para eliminar un Prestamo seleccionado
    def eliminar_Prestamo(self):
        selected_item = self.lista_Prestamos.selection()
        for item in selected_item:
            value = self.lista_Prestamos.item(item, 'values')
        self.lista_Prestamos.delete(selected_item)
        dni = value[0]
        codigo = value[1]
        fecha_prestamo = value[2]
        dias_pactados = value[3]
        prestamo = Prestamo(fecha_prestamo, self.padron.libros[codigo], self.padron.socios[dni], dias_pactados)
        eliminar_prestamo_db(prestamo)

    def __init__(self, padron):
        # Crear la self.ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Prestamos")
        self.padron = padron
        
        # Crear botones para CRUD
        agregar_button = tk.Button(self.ventana, text="Agregar", command=self.agregar_Prestamo)
        agregar_button.grid(row=3, column=0)
        editar_button = tk.Button(self.ventana, text="Editar", command=self.editar_Prestamo)
        editar_button.grid(row=3, column=1)
        eliminar_button = tk.Button(self.ventana, text="Eliminar", command=self.eliminar_Prestamo)
        eliminar_button.grid(row=3, column=2)

        # Crear lista de Prestamos
        self.lista_Prestamos = ttk.Treeview(self.ventana, columns=("Dni del socio", "Codigo del libro", "Fecha Prestamo", "Dias Pactados", "Fecha de Devolución"), show="headings")
        self.lista_Prestamos.heading("#1", text="Dni del socio")
        self.lista_Prestamos.heading("#2", text="Codigo del libro")
        self.lista_Prestamos.heading("#3", text="Fecha Prestamo")
        self.lista_Prestamos.heading("#4", text="Dias Pactados")
        self.lista_Prestamos.heading("#5", text="Fecha de Devolución")
        self.lista_Prestamos.grid(row=4, column=0, columnspan=3)

        for prestamo in self.padron.prestamos:
            self.lista_Prestamos.insert("", "end", values=(prestamo.socio.dni, prestamo.libro.codigo, prestamo.fecha_prestamo, prestamo.plazo, '' if prestamo.fecha_devolucion is None else prestamo.fecha_devolucion))

        # Configurar evento para cargar datos al hacer clic en un elemento de la lista
        # self.lista_Prestamos.bind("<<TreeviewSelect>>", lambda event: self.cargar_datos())

    def mostrar(self):
        self.ventana.mainloop()