class Automovil:
    
    def __init__(self, color, modelo, vel_max):
        self.color = color
        self.modelo = modelo
        self.vel_max= vel_max
        print "Se ha creado un auto", modelo, "color", color, "y su velocidad maxima alcanza los:", vel_max
    
    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        print "El color del automovil ahora es: ", self.color
    
    def mostrar_info(self, vel_actual):
        print "Modelo:", self.modelo
        print "Color:", self.color
        print "Velocidad máxima:", self.vel_max
        print "Velocidad actual:", self.vel_actual
 
    def propietario(self, **compradores)
     for nombre, fecha in compradores.items():
            print "Propietario:", nombre, "Fecha de compra:", fecha

# Crear un automóvil
auto = Automovil('rojo', 'Toyota', 180)

# Cambiar el color del automóvil
auto.cambiar_color('azul')

# Mostrar información del automóvil
auto.mostrar_info(60)

# Añadir propietarios
auto.propietario(Juan='2024-01-01', Maria='2025-05-12')