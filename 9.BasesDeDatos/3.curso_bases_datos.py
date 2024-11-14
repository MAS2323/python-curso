# claves principales en bases de datos

import sqlite3

# En una base relacional los registros que se introducen en ella
# deben estar identificados de forma unica

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

# Tenemos que agregar la palabra clave primary key a la variable que queremos que sea clave
# vamos ha acer que el codigo_arcticulo (ID) se autoincremente solo
miCursor.execute(
    '''create table productos (
    id integer primary key autoincrement,
    nombre_producto varchar(20), 
    precio integer, 
    seccion varchar(20))
    ''')

# Creamos una lista para introducir los productos en nuestra tabla
productos = [
    ("Pelota", 20, "Deporte"),
    ("Pantalon", 15, "confeccion"),
    ("destornillador", 25, "ferreteria"),
    ("Jarron", 45, "cerramica")
]

miCursor.executemany("INSERT INTO productos values (NULL,?,?,?)", productos)

miConexion.commit()

miConexion.close()
