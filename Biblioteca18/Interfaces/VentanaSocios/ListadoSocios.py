import tkinter as tk
from tkinter import ttk
from VentanaSocios.AgregarSocio import AgregarSocio
class ListadoSocios:

    def agregar_Socio(self):
        AgregarSocio().mostrar()
    def editar_Socio(self):
        AgregarSocio(self.lista_Socios).mostrar()
    # Función para eliminar un Socio seleccionado
    def eliminar_Socio(self):
        selected_item = self.lista_Socios.selection()[0]
        self.lista_Socios.delete(selected_item)

    # Función para cargar los datos de un Socio seleccionado en los campos de entrada
    def cargar_datos(self):
        selected_item = self.lista_Socios.selection()[0]
        socio = self.lista_Socios.item(selected_item, "values")
        dni = 323
        nombre = "sdhsdhs"
        apellido = "sfs"
        self.lista_Socios.insert("", "end", values=(dni, nombre, apellido))

    def __init__(self):
        # Crear la self.ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Socios")

        
        # Crear botones para CRUD
        agregar_button = tk.Button(self.ventana, text="Agregar", command=self.agregar_Socio)
        agregar_button.grid(row=3, column=0)
        editar_button = tk.Button(self.ventana, text="Editar", command=self.editar_Socio)
        editar_button.grid(row=3, column=1)
        eliminar_button = tk.Button(self.ventana, text="Eliminar", command=self.eliminar_Socio)
        eliminar_button.grid(row=3, column=2)

        # Crear lista de Socios
        self.lista_Socios = ttk.Treeview(self.ventana, columns=("Dni", "Nombre", "Apellido"), show="headings")
        self.lista_Socios.heading("#1", text="Dni")
        self.lista_Socios.heading("#2", text="Nombre")
        self.lista_Socios.heading("#3", text="Apellido")
        self.lista_Socios.grid(row=4, column=0, columnspan=3)

        dni = 323
        nombre = "sdhsdhs"
        apellido = "sfs"
        self.lista_Socios.insert("", "end", values=(dni, nombre, apellido))
        # Configurar evento para cargar datos al hacer clic en un elemento de la lista
        self.lista_Socios.bind("<<TreeviewSelect>>", lambda event: self.cargar_datos())

    def mostrar(self):
        self.ventana.mainloop()
