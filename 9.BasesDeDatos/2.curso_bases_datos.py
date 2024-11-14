# Insercion de varios registros
# Recuperacion de varios registros
import sqlite3


# creacion de nuestra coneccion a la bases de datos con el metodo connect
miConexion = sqlite3.connect('Segunda DB')

# creacion de un cursor que nos permitira crear tablas
miCursor = miConexion.cursor()

# creando nuestra tabla de nombre productos con tres campos, nombre, precio y seccion
"""miCursor.execute(
    'create table productos (nombre_producto varchar(20), precio integer, seccion varchar(20))')"""

# insertar un producto a nuestra tabla

# miCursor.execute("insert into productos values('Balon', 23, 'Deporte')")

# Cuando vamos ha hacer un registro la forma mas comoda de trabajar es con tuplas,
# se podia haber hecho esto con tres las instrucciones sql insert into
"""variosProductos = [

    ("Camiseta", 10, "Deportes"),
    ("Jarron", 90, "Ceramica"),
    ("Camion", 20, "Jugueteria")
]
# Para introducir este registro multiple utilizamos la istruccion executemany
# Los interogantes hacen referencia a los campos que tiene nuestro registro
miCursor.executemany("INSERT INTO productos values(?,?,?)", variosProductos)"""

# Leer o acceder a los valores de nuestra bases de datos:
# lo hacemos con la instruccion select

miCursor.execute("select * from productos")
# usamos el metodo fetchall() para obtener una lista con todos los registros que nos
# devuelve la instruccion sql selct *
variosProductos = miCursor.fetchall()

for producto in variosProductos:

    print("Nombre articulo: ", producto[0], " seccion: ", producto[2])

miConexion.commit()

# finalizacion de nuestra conexion
miConexion.close()
