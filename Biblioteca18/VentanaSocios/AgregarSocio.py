from tkinter import ttk
from tkinter import *
from Clase.socio import Socio
from Clase.administrarSocio import *
class AgregarSocio:
    def __init__(self, datos=[]):
        self.window = Tk()
        self.window.title("Alta de Socios")
        self.datos = datos
        frame1 = Frame(self.window)
        frame1.pack(pady=20, padx=10)
        frame2 = Frame(self.window)
        frame2.pack(pady=5, padx=5)

        self.dni = StringVar()
        self.nombre = StringVar()
        self.apellido = StringVar()

        Label(frame1, text="Dni:").grid(row=0, column=0)
        Entry(frame1, textvariable=self.dni).grid(row=0, column=1)
        Label(frame1, text="Nombre:").grid(row=1, column=0)
        Entry(frame1, textvariable=self.nombre).grid(row=1, column=1) 
        Label(frame1, text="Apellido:").grid(row=2, column=0)
        Entry(frame1, textvariable=self.apellido).grid(row=2, column=1)


        if self.datos == []:
            Button(frame2, text="Agregar", command=self.agregar_Socio).pack(side="left", padx=10)
        else:
            Button(frame2, text="Editar", command=self.editar_Socio).pack(side="left", padx=10)
        
        Button(frame2, text="Cancelar", command=self.window.destroy).pack(side="right", padx=10)


    def mostrar(self):
        self.window.mainloop()

        # Función para agregar un Socio a la lista
    def agregar_Socio(self):
        dni = self.dni.get()
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        socio = Socio(dni, nombre, apellido)
        try:
            cargar_socio(socio)
        except Exception as e:
            print(f"Error al agregar el socio: {e}")
        
        dni = self.dni.set("")
        nombre = self.nombre.set("")
        apellido = self.apellido.set("")


    # Función para editar un Socio seleccionado
    def editar_Socio(self):
        # selected_item = self.lista_Socios.selection()[0]
        dni = self.datos[0]
        nombre = self.datos[1]
        apellido = self.datos[2]
        socio = Socio(dni, nombre, apellido)
        
        # Para crear nuevo tendría que tomar los datos nuevos que se ingresan por teclado
        nuevo = Socio(dni, nombre, apellido)
        try:
            modificar_socio(socio, nuevo)
        except Exception as e:
            print(f"Error al modificar el socio: {e}")
        dni = self.dni.set("")
        nombre = self.nombre.set("")
        apellido = self.apellido.set("")
