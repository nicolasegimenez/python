# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class FiguraRegular:
    __metaclass__ = ABCMeta

    def __init__(self, lado=3):
        self.lado = lado
        self._FiguraRegular__area = 0  # Atributo privado

    @abstractmethod
    def calcular_area(self):
        pass

    def verArea(self):
        return self._FiguraRegular__area

class Cuadrado(FiguraRegular):
    def __init__(self, lado):
        FiguraRegular.__init__(self, lado)

    def calcular_area(self):
        self._FiguraRegular__area = self.lado * self.lado  # Área de un cuadrado: lado^2

class TrianguloEquilatero(FiguraRegular):
    def __init__(self, lado):
        FiguraRegular.__init__(self, lado)

    def calcular_area(self):
        import math
        self._FiguraRegular__area = (math.sqrt(3) / 4) * (self.lado ** 2)  # Área de un triángulo equilátero

# Crear instancias y calcular el área
cuadrado = Cuadrado(5)
cuadrado.calcular_area()
print "El área del cuadrado es:", cuadrado.verArea()

triangulo = TrianguloEquilatero(4)
triangulo.calcular_area()
print "El área del triángulo equilátero es:", triangulo.verArea()

