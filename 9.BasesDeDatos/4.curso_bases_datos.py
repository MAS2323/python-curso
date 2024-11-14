# Clausula Unique
# Operaciones CRUD

import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

# Usamos la clusula unique para hacer que un parametro sea unico
"""miCursor.execute(
    '''create table productos (
    id integer primary key autoincrement,
    nombre_producto varchar(20) unique, 
    precio integer, 
    seccion varchar(20))
    ''')

productos = [
    ("Pelota", 20, "Deporte"),
    ("Pantalon", 15, "confeccion"),
    ("destornillador", 25, "ferreteria"),
    ("Jarron", 45, "cerramica"),
    ("Pantalones", 95, "confeccion")
]

miCursor.executemany("INSERT INTO productos values (NULL,?,?,?)", productos)"""

# miCursor.execute("UPDATE productos set precio= 35 where nombre_producto = 'pelota'")

# Nunca se debe olvidar la clausula whre en un delete
miCursor.execute("DELETE FROM productos WHERE id =5")


miConexion.commit()


miConexion.close()
