# Los generadores
# Los generadores son estructuras que extraen valores de una funcion y se almacena en objetos iterables
# Los Generadores:permiten extraer valores de una funcion y almacenarlo (de uno en uno) en objetos iterables
# sin la necesidad de almacenar todos a la vez en la memoria RAM

# Los generadores nos permiten obtener los valores uno a uno
# Sintaxis
# Los generadores son mas eficientes que las funciones
"""
    Sintaxis
Def gerenarNumeros():
    yield numeros"""


def generarPares(limite):

    num = 1

    while num < limite:
        yield num*2
        num = num + 1


# Entre llamada y llamada el objeto generador entra en un estado de suspencion
devuelvePares = generarPares(10)

# La funcion next nos retorna el siguiente elemento de un objeto iterable

print(next(devuelvePares))

print("Aqui podria ir mas codigo....")

print(next(devuelvePares))

print("Aqui podria ir mas codigo....")

print(next(devuelvePares))

# La instruccion Yield from: esta instruccion simplifica el codigo de los generadores
# en el caso de utilizar bucles anidados: ejemplo: un for dentro de otro for
# Muy utiles con listas de valores infinito.
# Entre llamada y llamada el objeto iterable entra en un estado de pausa que se conoce como estado de suspencion

# el asterisco quiere decir que se recibira una cantidad indeterminada de variables, elementos o parametros
# ademas estos parametros se recibiran en forma de tuplas


def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        # for subElementos in elemento:
        yield from elemento


ciudades_devueltas = devuelve_ciudades(
    "Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
