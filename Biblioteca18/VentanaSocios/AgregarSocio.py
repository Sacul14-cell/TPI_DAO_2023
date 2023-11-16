from tkinter import *
from Entidades.socio import Socio
from CRUD.administrarSocio import *
class AgregarSocio:
    def __init__(self, datos=[]):
        self.window = Tk()
        self.window.title("Alta de Socios")
        self.datos = datos
        frame1 = Frame(self.window)
        frame1.pack(pady=20, padx=10)
        frame2 = Frame(self.window)
        frame2.pack(pady=5, padx=5)

        self.dni = IntVar(self.window)
        self.nombre = StringVar(self.window)
        self.apellido = StringVar(self.window)

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
        print("Datos: ",dni, nombre, apellido)
        socio = Socio(dni, nombre, apellido)
        try:
            cargar_socio(socio)
        except Exception as e:
            print(f"Error al agregar el socio: {e}")
        else:
            print("Socio cargado")
        
        self.dni.set(0)
        self.nombre.set("")
        self.apellido.set("")


    # Función para editar un Socio seleccionado
    def editar_Socio(self):
        for item in self.datos.selection():
            value = self.datos.item(item, 'values')
        dni = value[0]
        nombre = value[1]
        apellido = value[2]
        socio = Socio(dni, nombre, apellido)
        
        
        
        
        dni = self.dni.get()
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        nuevo = Socio(dni, nombre, apellido)
        try:
            modificar_socio(socio, nuevo)
        except Exception as e:
            print(f"Error al modificar el socio: {e}")
        self.dni.set(0)
        self.nombre.set("")
        self.apellido.set("")