# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class Animal:
    __metaclass__ = ABCMeta
    def __init__(self):
        print "Ha nacido un animal"

    @abstractmethod
    def rugir(self):
        pass

class Perro(Animal):
    def __init__(self, nombre,raza):
        Animal.__init__(self)
        self.nombre = nombre
        self.raza=raza
        print "ha nacido un perro llamado {} de raza {}".format(nombre, raza)

    def rugir(self):
        print "ladrar"

class Gato (Animal):
    def __init__(self, nombre, raza):
        Animal.__init__(self)
        self.nombre = nombre
        self.raza = raza
        print "ha nacido un gato llamado {} de raza {}".format(nombre, raza)
    
    def rugir(self):
        print "maullar"

mi_perro = Perro("Firulais", "Labrador")
mi_perro.rugir()  # Esto llamara rugir implementado como ladrar

mi_gato = Gato("Miau", "Siamés")
print mi_gato.nombre  # Accede al atributo nombre de la instancia
print mi_gato.raza    # Accede al atributo raza de la instancia
mi_gato.rugir()       # Llama al método rugir implementado como maullar
