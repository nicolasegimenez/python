# -*- coding: utf-8 -*-


import sqlite3

def consultas():
    # Conectar a la base de datos
    db2 = sqlite3.connect('musica.db')
    print("Estas en la funcion insertar")
    
    # Crear un cursor
    consulta = db2.cursor()
    
    # Ejecutar una consulta
    consulta.execute("SELECT * FROM music")
    
    # Obtener todas las filas de la consulta
    filas = consulta.fetchall()
    
    # Crear una lista para almacenar los resultados
    lista = []
    
    # Iterar sobre las filas y extraer la información
    for fila in filas:
        # Usar índices para acceder a las columnas
        s = {
            'cancion': fila[0],  # Cambia el índice según el orden de las columnas
            'artista': fila[1],  # Cambia el índice según el orden de las columnas
            'album': fila[2]     # Cambia el índice según el orden de las columnas
        }
        lista.append(s)
    
    # Cerrar el cursor y la conexión
    consulta.close()
    db2.close()
    
    return lista

# Llamar a la función
resultados = consultas()
print(resultados)
