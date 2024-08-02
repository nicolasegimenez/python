class Persona:
    def __init__(self):
        self.edad = 18
        self.nombre= "Juan"
        print "se ha creado a", self.nombre, "de", self.edad

    def hablar (self, palabras="No se que decir"):
        print self.nombre, ': ', palabras


juan=Persona()
juan.hablar()
juan.hablar("hola estoy hablando")