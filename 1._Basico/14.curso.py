# Intruccion Continue, pass y else

# for letra in "python":

#     if letra == "h":
#         # Lo que hace continue es salatar la linea donde se definio la condicion
#         continue

#     print("Viendo la letra: " + letra)

nombre = "Pildoras Informaticas"

contador = 0
for i in nombre:
    contador += 1

print(len(nombre))

# La instruccion pass, lo que devuelve esta funcion es un null
# se usa sobre toda para especificar que algo se hara luego


class MiClase:
    pass


# instruccion else
email = input("Introduce tu email por favor: ")

for i in email:
    if i == "@":
        arroba = True
        break
# La instruccion else dentro de un bucle se va a ejecutar siempre y cuandoo el bucle este vacio
# Es decir cuando se haya terminado de recorer el bucle
else:

    arroba = False

print(arroba)
