# Bucle for continuacion

# El primer numero hace referencia a donde empieza, el segundo donde termina y el terceto
# los intgervalos del cambio
# for i in range(5, 50, 3):
#     # Utilizamos la funcion de tipo f (format) para jugar con formatos de forma diferente
#     print(f"valor de la variable {i}")

# Si ponemos un valor en un if(valor) sin determinar nada mas el if asume que ese valor es True (Positivo)
valido = False

email = input("Introduce tu email: ")
for i in range(len(email)):

    if email[i] == '@':
        valido = True
if valido:  # si valido == True

    print("Email correcto")
else:
    print("Email incorrecto")
