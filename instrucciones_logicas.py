try:
    libros = int(input("Cuantos libros lees anualmente? "))
    if libros >= 15:
        print('eres buen lector')
    else:
        print('necesitas leer mas')

except ValueError:
    print("Por favor, introduce un numero valido")