# Bucle for
# Existen ducles determinados e indeterminados
# El Bucle for es determinado: sintaxis (for variable in elemento a recorer):
# cuerpo del bucle

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
        contador = contador + 1
if contador == 2:
    print("Email es correcto")
else:
    print("El email es incorrecto")

# -----------------------------------------------------------------------------------------
# El tipo range() es una funcion que crea un array que empieza desde el 0 has n

for i in range(5):
    print('Hola')
