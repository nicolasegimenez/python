#Graphical User Interface with python 2.7
from Tkinter import *
class Interfaz:
    def __init__(self, contenedor):
        self.textE3 = StringVar()
        self.e1 = Label(contenedor, text="Convertir celsius a farenheit", fg="black",)
        self.e2 = Label(contenedor, text="Celsius", fg="red" )
        self.e3 = Label(contenedor, text="farenheit", fg="blue")
        self.e4 = Button(contenedor, text="Convertir", fg="green", bg="orange", command=self.hacerConversion)
        self.e5 = Entry(contenedor, fg="white", bg="black")
        self.e6 = Label(contenedor, fg="purple", bg="red", textvariable=self.textE3)

        self.e1.grid(column=0, row=0, columnspan=2)
        self.e2.grid(column=0, row=1)
        self.e3.grid(column=0, row=2)
        self.e4.grid(column=0, row=3, columnspan=2)
        self.e5.grid(column=1, row=1)
        self.e6.grid(column=1, row=2)

    def hacerConversion(self):
        celsius = float(self.e5.get())
        farenheit = (celsius * 9/5) + 32
        self.textE3.set(farenheit)

ventana = Tk()
mi_interfaz = Interfaz(ventana)
ventana.mainloop()
