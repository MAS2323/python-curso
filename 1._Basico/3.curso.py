# Funciones en python
# Una funcion es un bloque de codigo que realiza una tarea determinada
# A las funciones en python tambien se les denomina metodos cuando se encuentran dentro de una clase

# Sintaxis

"""
def nombre_funcion():
    instruccion de la funcion
    return(opcional)

def nombre_funcion(parametros):
    instruccion de la funcion
    return(opcional)
"""


def mensaje():  # Declaracion de la funion
    # Cuerpo de la funcion
    print("Estamos aprendiendo pyhton")
    print("Estamos aprendiendo instruciones basicas")
    print("Poco apoco iremos avanzando")


mensaje()  # llamada de la funion

print("----------------------------------------------------------------------------------------------")

# La principal utilidad de una funcion es su reutilizacion


def suma(num1, num2):  # Paso por paramatros
    print(num1 + num2)


# Declaracion o llamada de la funcion y paso de parametros a la misma
suma(3, 7)
suma(67, 8)
suma(35, 9)

print("----------------------------------------------------------------------------------------------")

# Para python todo es referencia, todos los valores se pasan por referencia


def suma2(num1, num2):
    resultado = num1 + num2
    return resultado


almacena_resultado = suma2(4, 5)

print(almacena_resultado)
