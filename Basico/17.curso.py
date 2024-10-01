# Lanzamiento de excepciones
# Instruccion Raise

"""def evaluaEdad(edad):

    # Definiendo nuestra propia excepcion
    if edad < 0:
        raise ZeroDivisionError("No se permite edades negativas")
    if edad < 20:
        return "eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return "Cuidate"


print(evaluaEdad())
"""


from math import sqrt
import math


def raizCuadrad(num):

    if num < 0:
        raise ZeroDivisionError(
            "No se puede calcular raices de numeros negativos")
    else:

        return math.sqrt(num)


op = int(input("Introduzca un numero: "))

try:
    print(raizCuadrad(op))

except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("Programa terminado")
