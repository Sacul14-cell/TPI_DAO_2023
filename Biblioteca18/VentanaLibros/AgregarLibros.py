
from tkinter import ttk
from tkinter import *
from Entidades.libro import Libro
from Estados.disponible import Disponible
from Estados.extraviado import Extraviado
from Estados.prestado import Prestado
from CRUD.administrarLibro import *
from db import DBConnection
class AgregarLibro:
    def __init__(self, datos=[]):
        self.window = Tk()
        self.window.title("Alta de libros")
        self.datos = datos
        self.db = DBConnection("biblioteca.db")
        frame1 = Frame(self.window)
        frame1.pack(pady=20, padx=10)
        frame2 = Frame(self.window)
        frame2.pack(pady=5, padx=5)

        self.codigo = IntVar(self.window)
        self.titulo = StringVar(self.window)
        self.precio = DoubleVar(self.window)

        Label(frame1, text="Codigo:").grid(row=0, column=0)
        Entry(frame1, textvariable=self.codigo).grid(row=0, column=1)
        Label(frame1, text="Titulo:").grid(row=1, column=0)
        Entry(frame1, textvariable=self.titulo).grid(row=1, column=1) 
        Label(frame1, text="Precio:").grid(row=2, column=0)
        Entry(frame1, textvariable=self.precio).grid(row=2, column=1)
        Label(frame1, text="Estado:").grid(row=3, column=0)
        # Entry(frame1, textvariable=self.estado).grid(row=3, column=1)
        estado_options = ["Disponible", "Prestado", "Extraviado"]
        self.estado = ttk.Combobox(frame1, width=17, height=5, state="readonly", values=estado_options)
        self.estado.grid(row=3, column=1)
        if self.datos == []:
            Button(frame2, text="Agregar", command=self.agregar_libro).pack(side="left", padx=10)
        else:
            Button(frame2, text="Editar", command=self.editar_libro).pack(side="left", padx=10)
        
        Button(frame2, text="Cancelar", command=self.window.destroy).pack(side="right", padx=10)


    def mostrar(self):
        self.window.mainloop()

        # Función para agregar un libro a la lista
    def agregar_libro(self):
        codigo = self.codigo.get()
        titulo = self.titulo.get()
        precio = self.precio.get()
        estado = self.estado.get()
        e = [Disponible, Prestado, Extraviado]
        estados = {"Disponible": 1, "Prestado": 2, "Extraviado": 3}
        libro = Libro(codigo, titulo, precio, e[estados[estado]-1]())
        try:
            cargar_libro(libro)
        except Exception as e:
            print(f"Error al agregar el libro: {e}")
        else:
            print("Libro agregado correctamente.")
        #l = Libro(int(codigo), titulo, float(precio), e[estados[estado]-1]())
        # self.lista_libros.insert("", "end", values=(codigo, titulo, precio, estado))
        # self.codigo.set(0)
        # self.titulo.set("")
        # self.precio.set(0)


    # Función para editar un libro seleccionado
    def editar_libro(self):
        selected_item = self.datos.selection()
        for item in selected_item:
            value = self.datos.item(item, 'values')
        codigo = value[0]
        titulo = value[1]
        precio = value[2]
        estado = value[3]
        e = [Disponible, Prestado, Extraviado]
        estados = {"Disponible": 1, "Prestado": 2, "Extraviado": 3}
        libro = Libro(codigo, titulo, precio, e[estados[estado]-1]())
        
        codigo = self.codigo.get()
        titulo = self.titulo.get()
        precio = self.precio.get()
        estado = self.estado.get()
        nuevo = Libro(codigo, titulo, precio, e[estados[estado]-1]())
        
        try:
            modificar_libro(libro, nuevo)
        except Exception as e:
            print(f"Error al editar el libro: {e}")
        # self.lista_libros.item(selected_item, values=(codigo, titulo, precio, estado))
        codigo = self.codigo.set("")
        titulo = self.titulo.set("")
        precio = self.precio.set("")
        estado = self.estado.set("")