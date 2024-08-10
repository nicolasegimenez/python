
# -*- coding: utf-8 -*-

def escritura (*datos):
    with open('./datos.txt','w') as prueba:
        for dato in datos:
            prueba.write(dato)
    print("Escritura")
    prueba.close()
escritura('hola', 'mundo', 'Bonita', "nico", "cristo")

def lectura():
    prueba=open('./datos.txt', 'r')
    print(prueba.read())
    prueba.close()
lectura()

Cadena='Es mas facil romper un atomo que un prejuicio'
print(Cadena.count('a'))

cadena_upper=Cadena.upper()
print(cadena_upper)
    
cadena_split= cadena_upper.split("O", cadena_upper.count('O'))
print(cadena_split)

print(Cadena.rfind('p'))

Lista=[100, 25,65, [54,25, [96, 21,47]] ,52]
print(Lista)
print(Lista[3][2][2])
Lista.append(90)
Lista[3][2].insert(1, 65)
print(Lista)
Lista.reverse()
print(Lista)