# -*- coding: utf-8 -*-

import sqlite3

def crear_tabla():
    conexion = sqlite3.connect('musica.db')
    consulta = conexion.cursor()

    # Crear tabla solo si no existe
    tabla = """CREATE TABLE IF NOT EXISTS music(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cancion TEXT NOT NULL,
        artista TEXT NOT NULL,
        album TEXT NOT NULL
    )"""
    
    try:
        consulta.execute(tabla)
        print("Tabla creada con éxito o ya existe.")
    except sqlite3.Error as e:
        print("Error al crear la tabla: {}".format(e))
    finally:
        conexion.commit()
        conexion.close()

def insertar():
    db1 = sqlite3.connect('musica.db')
    print("Estás en la función insertar")
    
    cancion1 = raw_input("Ingrese el nombre de la canción: ")
    artista1 = raw_input("Ingrese el nombre del artista: ")
    album1 = raw_input("Ingrese el nombre del álbum: ")

    consulta = db1.cursor()

    # Utilizar parámetros en lugar de concatenar strings para evitar inyecciones SQL
    strConsulta = "INSERT INTO music (cancion, artista, album) VALUES (?, ?, ?)"
    
    try:
        consulta.execute(strConsulta, (cancion1, artista1, album1))
        print("Canción insertada con éxito.")
    except sqlite3.Error as e:
        print("Error al insertar los datos: {}".format(e))
    finally:
        db1.commit()
        consulta.close()
        db1.close()

if __name__ == "__main__":
    crear_tabla()
    insertar()
