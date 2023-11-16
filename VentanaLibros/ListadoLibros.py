import tkinter as tk
from tkinter import ttk
from VentanaLibros.AgregarLibros import AgregarLibro
from Estados.prestado import Prestado
from Estados.disponible import Disponible
from Estados.extraviado import Extraviado
from Entidades.libro import Libro
from CRUD.administrarLibro import *
class ListadoLibros:

    def agregar_libro(self):
        AgregarLibro().mostrar()
    def editar_libro(self):
        AgregarLibro(self.lista_libros).mostrar()
    # Función para eliminar un libro seleccionado
    def eliminar_libro(self):
        selected_item = self.lista_libros.selection()
        for item in selected_item:
            value = self.lista_libros.item(item, 'values')
        self.lista_libros.delete(selected_item)
        codigo = value[0]
        titulo = value[1]
        precio = value[2]
        estado = value[3]
        print(estado)
        e = [Disponible, Prestado, Extraviado]
        estados = {"Disponible": 1, "Prestado": 2, "Extraviado": 3}
        libro = Libro(codigo, titulo, precio, e[estados[estado]-1]())
        eliminar_libro_db(libro)
    def __init__(self, padron):
        # Crear la self.ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Libros")
        self.padron = padron
        
        # Crear botones para CRUD
        agregar_button = tk.Button(self.ventana, text="Agregar", command=self.agregar_libro)
        agregar_button.grid(row=3, column=0)
        editar_button = tk.Button(self.ventana, text="Editar", command=self.editar_libro)
        editar_button.grid(row=3, column=1)
        eliminar_button = tk.Button(self.ventana, text="Eliminar", command=self.eliminar_libro)
        eliminar_button.grid(row=3, column=2)

        # Crear lista de libros
        self.lista_libros = ttk.Treeview(self.ventana, columns=("Codigo", "Titulo", "Precio", "Estado"), show="headings")
        self.lista_libros.heading("#1", text="Codigo")
        self.lista_libros.heading("#2", text="Titulo")
        self.lista_libros.heading("#3", text="Precio")
        self.lista_libros.heading("#4", text="Estado")
        self.lista_libros.grid(row=4, column=0, columnspan=3)

        for libro in self.padron.values():
            self.lista_libros.insert("", "end", values=(libro.codigo, libro.titulo, libro.precio_reposicion, libro.estado))
        # Configurar evento para cargar datos al hacer clic en un elemento de la lista
        # self.lista_libros.bind("<<TreeviewSelect>>", lambda event: self.cargar_datos())

    def mostrar(self):
        self.ventana.mainloop()
