# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class Transporte:
    __metaclass__ = ABCMeta

    def __init__(self, medio):
        self.medio = medio
        # Usar el atributo "medio" para definir cómo avanza

    @abstractmethod
    def avanzar(self):
        pass
    def giraIzquierda(self):
        print "Gira a la izquierda"

    def giraDerecha(self):
        print "Gira a la derecha"

    # De acuerdo al "medio", especificar qué hace para frenar
    @abstractmethod
    def detener(self):
        pass

class Tranvia(Transporte):
    def __init__(self, medio):
        super(Tranvia, self).__init__(medio)
        print "Se ha empezado a mover un tranvía que va por {}".format(medio)

    def avanzar(self):
        print "El tranvía que va por {} está avanzando".format(self.medio)

    def detener(self):
        print "El tranvía se detiene usando frenos eléctricos"

class Colectivo(Transporte):
    def __init__(self, medio):
        super(Colectivo, self).__init__(medio)
        print "Se ha empezado a mover un colectivo que va por {}".format(medio)

    def avanzar(self):
        print "El colectivo que va por {} está avanzando".format(self.medio)

    def detener(self):
        print "El colectivo se detiene usando frenos hidráulicos"

# Crear instancias y probar los métodos
tranvia = Tranvia("rieles")
tranvia.avanzar()
tranvia.giraIzquierda()
tranvia.detener()

colectivo = Colectivo("carretera")
colectivo.avanzar()
colectivo.giraDerecha()
colectivo.detener()
