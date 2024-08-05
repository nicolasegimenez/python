class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre= nombre
        print"se ha creado a", self.nombre, "de", self.edad

    def hablar (self, **palabras):
        for frase in palabras:
            print self.nombre, ': ', palabras[frase]

class Deportista(Persona):
    def __init__(self, edad, nombre, deporte):
        self.edad = edad
        self.nombre = nombre
        self.deporte = deporte
        print"se ha creado a", self.nombre, "de", self.edad

        print "Se ha creado a", self.nombre
    def practicarDeporte(self):
        print self.nombre, ':', "voy a practicar"


juan=Persona(18, "Juan")
juan.hablar(t1="hola estoy hablando",t2= "Este soy yo")

luis=Deportista(18,"Luis","natacion")
luis.hablar(t1="hola, estoy hablando", t2="Este soy yo")
luis.practicarDeporte()
print "Luis practica", luis.deporte