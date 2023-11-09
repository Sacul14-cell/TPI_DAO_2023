import tkinter as tk
from tkinter import ttk
from VentanaPrestamos.AgregarPrestamo import AgregarPrestamo
class ListadoPrestamos:

    def agregar_Prestamo(self):
        AgregarPrestamo().mostrar()
    def editar_Prestamo(self):
        AgregarPrestamo(self.lista_Prestamos).mostrar()
    # Función para eliminar un Prestamo seleccionado
    def eliminar_Prestamo(self):
        selected_item = self.lista_Prestamos.selection()[0]
        self.lista_Prestamos.delete(selected_item)

    # Función para cargar los datos de un Prestamo seleccionado en los campos de entrada
    def cargar_datos(self):
        selected_item = self.lista_Prestamos.selection()[0]
        Prestamo = self.lista_Prestamos.item(selected_item, "values")
        dni_socio = 323
        codigo_libro = 3252
        fecha_prestamo = "23/04/2023"
        dias_pactados = 1
        self.lista_Prestamos.insert("", "end", values=(dni_socio, codigo_libro, fecha_prestamo, dias_pactados))

    def __init__(self):
        # Crear la self.ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Prestamos")

        
        # Crear botones para CRUD
        agregar_button = tk.Button(self.ventana, text="Agregar", command=self.agregar_Prestamo)
        agregar_button.grid(row=3, column=0)
        editar_button = tk.Button(self.ventana, text="Editar", command=self.editar_Prestamo)
        editar_button.grid(row=3, column=1)
        eliminar_button = tk.Button(self.ventana, text="Eliminar", command=self.eliminar_Prestamo)
        eliminar_button.grid(row=3, column=2)

        # Crear lista de Prestamos
        self.lista_Prestamos = ttk.Treeview(self.ventana, columns=("Dni del socio", "Codigo del libro", "Fecha Prestamo", "Dias Pactados"), show="headings")
        self.lista_Prestamos.heading("#1", text="Dni del socio")
        self.lista_Prestamos.heading("#2", text="Codigo del libro")
        self.lista_Prestamos.heading("#3", text="Fecha Prestamo")
        self.lista_Prestamos.heading("#4", text="Dias Pactados")
        self.lista_Prestamos.grid(row=4, column=0, columnspan=3)

        dni_socio = 323
        codigo_libro = 3252
        fecha_prestamo = "23/04/2023"
        dias_pactados = 1
        self.lista_Prestamos.insert("", "end", values=(dni_socio, codigo_libro, fecha_prestamo, dias_pactados))

        # Configurar evento para cargar datos al hacer clic en un elemento de la lista
        self.lista_Prestamos.bind("<<TreeviewSelect>>", lambda event: self.cargar_datos())

    def mostrar(self):
        self.ventana.mainloop()
