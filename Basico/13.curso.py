import math
# Bucle while: bucle indeterminado
# i = 1

# while i <= 10:
#     print("Ejecucion " + str(i))
#     i = i + 1


# print("Termino la ejecucion")

# Programa para introducir la edad y ver si es verdadera

# edad = int(input("Introduce tu edad por favor: "))

# while edad < 0 or edad > 100:
#     print("Has introduciod una edad incorrecta. Vuelva a intentarlo")
#     edad = int(input("Introduce tu edad por favor: "))

# print("Gracias por colaborar puedes pasar")
# print("Edad del aspirante " + str(edad))


print("Programa de calculo de la raiz cuadrada")
numero = int(input("Introduce un numero por favor: "))

intentos = 0  # contador

while numero < 0:
    print("No se puede hallar la raiz cuadrad de un numero negativo")

    if intentos == 2:
        print("Has consumido demasiados intentos. El programa ha finalizado")
        break

    numero = int(input("Introduce un numero por favor: "))
    if numero < 0:
        intentos = intentos + 1
if intentos < 2:
    solucion = math.sqrt(numero)
    print("La raiz cuadrad de " + str(numero) + " es " + str(solucion))
