import tkinter as tk
from tkinter import ttk
from VentanaLibros.AgregarLibros import AgregarLibro
class ListadoLibros:

    def agregar_libro(self):
        AgregarLibro().mostrar()
    def editar_libro(self):
        AgregarLibro(self.lista_libros).mostrar()
    # Función para eliminar un libro seleccionado
    def eliminar_libro(self):
        selected_item = self.lista_libros.selection()[0]
        self.lista_libros.delete(selected_item)

    # Función para cargar los datos de un libro seleccionado en los campos de entrada
    def cargar_datos(self):
        selected_item = self.lista_libros.selection()[0]
        libro = self.lista_libros.item(selected_item, "values")
        codigo = 323
        titulo = "sdhsdhs"
        precio = 435
        estado = "1"
        self.lista_libros.insert("", "end", values=(codigo, titulo, precio, estado))

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

        for libro in self.padron:
            self.lista_libros.insert("", "end", values=(libro.codigo, libro.titulo, libro.precio_reposicion, libro.estado))
        # Configurar evento para cargar datos al hacer clic en un elemento de la lista
        self.lista_libros.bind("<<TreeviewSelect>>", lambda event: self.cargar_datos())

    def mostrar(self):
        self.ventana.mainloop()
