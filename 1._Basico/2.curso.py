# Tipos, operadores y variables
# En python vamos a manejar tres tipos de datos: numericos, textos y booleanos

# Los operadores que podemos usar en python son los siguientes
# Aritmeticos, comparacion, logicos, asignacion y especiales

# Variable: es un espacio en la memoria del ordenador donde se almacena un valor, que podra cambiar durante
# la ejecucion del programa

# En python el tipo de variable no lo establece el contenedor si no el contenido

nombre = "Mas onewe"

a = 3
b = 6

print(nombre)

# En python todo es un objeto

x = type(a)
print(x)

mensaje = """
Esto es un mensaje 
con tres saltos de linea 
"""
print(mensaje)

# Operadores de comparacion: if, if else, elif

numero1 = 5
numero2 = 7

if numero1 > numero2:
    print("El numero uno es mayor")
else:
    print("El numero dos es mayor")
