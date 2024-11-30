# Bucle for
# Existen bucles determinados e indeterminados o finitos e infinitos
# El Bucle for es determinado: sintaxis (for variable in elemento a recorer):
# cuerpo del bucle

# en nuestro ejemplo la i funciona como contador
# for i in [1, 2, 3, 4]:
#     print("Hola")
# for i in ['primavera', 'verano', 'otono', 'invierno']:
#     print(i)

contador = 0
miEmail = input("Introduce tu direccion de email: ")

for i in miEmail:

    # # El agumento end determina como queremos que se imprima nuestro bucle
    # print('hola', end="")

    # Se tiene que cumplir estas dos condiciones, al cumplirse las dos condiciones es cuando se sumara el contador
    if (i == '@' or i == "."):
        # si se cumple esta condicion el contador pasara a valer dos y el programa seguira
        contador = contador + 1
if contador == 2:
    print("Email es correcto")
else:
    print("El email es incorrecto")

# -----------------------------------------------------------------------------------------
# El range() es una funcion que crea un array que empieza desde el 0 has n

# la funcion rang(5) nos ceara un areglo de 0 hasta 5-1: en nuestro ejemplo n = 5
# la funcion range puede llegar a tener has tres parametos: range(n=inicio, x=final, z=variacion del inicio)
for i in range(5):
    print('Hola')
