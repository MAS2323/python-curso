# Los generadores
# Los generadores son estructuras que extraen valores de una funcion y se almacena en objetos iterables

# Sintaxis
# Los generadores son mas eficientes que las funciones
"""Def gerenarNumeros():
    yield numeros"""


def generarPares(limite):

    num = 1

    while num < limite:
        yield num*2
        num = num + 1


# Entre llamada y llamada el objeto generador entra en un estado de suspencion
devuelvePares = generarPares(10)

print(next(devuelvePares))

print("Aqui podria ir mas codigo....")

print(next(devuelvePares))

print("Aqui podria ir mas codigo....")

print(next(devuelvePares))


# La instruccion Yield from: esta instruccion simplifica el codigo de los generadores
# en el caso de utilizar bucles anidados: eje: un for deontro de otro for
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        # for subElementos in elemento:
        yield from elemento


ciudades_devueltas = devuelve_ciudades(
    "Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
