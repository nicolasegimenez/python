#Calculo de areas

F=3.141516

def acuadrado():
    lado = input("cual es el valor del lado?")
    x=lado**2
    print "\n El area del cuadrado es ", x, "unidades cuadradas"

def atriangulo():
    base=input("cual es el valor de la base?")
    altura= input("cual es el valor de la altura?")
    y= base*altura/2
    print"\n el area deeltriangulo es ", y, "unidades cuadradas"

def acirculo():
    radio = input("Cual es el valor del radio?")
    z= (F*radio) ** 2
    print"\n El area del circulo es",z, "unidades cuadradas"
i=True
while i == True:
    area= input("\nElije la figura geometrica \n Cuadrado=1 \n Triangulo=2 \n circulo=3 \n")
    if area == 1:
        acuadrado()
    elif area ==2:
        atriangulo()
    elif area==3:
        acirculo()
    else:
        print"Ingresa una opcion valida"
    i= input("\nQuieres \n Si=True \n No=False\n")