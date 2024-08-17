# -*- coding: utf-8 -*-

# GUI with Tkinter and Python 2.7
from Tkinter import *

class Interfaz:
    def __init__(self, contenedor):
        # Crear widgets Label y Button
        self.e1 = Label(contenedor, text="Color", fg="black")
        self.e2 = Button(contenedor, text="Amarillo", fg="yellow", command=lambda: self.cambiar_color("yellow"))
        self.e3 = Button(contenedor, text="Azul", fg="blue", command=lambda: self.cambiar_color("blue"))
        self.e4 = Button(contenedor, text="Blanco", fg="white", command=lambda: self.cambiar_color("white"))

        # Organizar los widgets en una cuadrícula
        self.e1.grid(column=0, row=0, columnspan=3, sticky="we")
        self.e2.grid(column=0, row=1)
        self.e3.grid(column=1, row=1)
        self.e4.grid(column=2, row=1)

    # Función para cambiar el color del texto de la etiqueta
    def cambiar_color(self, color):
        self.e1.config(fg=color)

ventana = Tk()
mi_interfaz = Interfaz(ventana)
ventana.mainloop()

