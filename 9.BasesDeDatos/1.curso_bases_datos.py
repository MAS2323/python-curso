# Creacion de bases de datos
# conexion de bases de datos
# insercion de registros en bases de datos
# Python es capaz de gestionar los diferentes sistemas de gestores de datos

import sqlite3

# passos a seguir para crear la conexion y nuestra bases de datos

miConexion = sqlite3.connect("Primera Base")

# creando nuestra primera tabla: primero creamos el cursor o puntero
miCursor = miConexion.cursor()

# Creando nuestra primer tabla con la instruccion create

# miCursor.execute("create table PRODUCTOS (NOMBRE_ARTICULO VARCHAR (50), PRECIO INTEGER, SECCION VARCHAR(20))")

# Introducir datos en nuestra tabla: para hacerlo primero tenemos que comentar el codigo de creacion de una tabla

miCursor.execute("INSERT INTO PRODUCTOS VALUES('Balon', 234, 'Deporte')")
# para que se apliquen estos cambios en nuestra base de datos tenemos que usar la funcion commit en nuestra conexion

miConexion.commit()


# Despues de haber creado la base de datos utilizo el metodo close para cerrarlo
miConexion.close()
