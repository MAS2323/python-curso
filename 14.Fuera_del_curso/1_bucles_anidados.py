# Los bucles anidados son bucles dentro de otros bucles
# No importa el bucle que sea, for o while: el bucle interno finalizara todas sus
# iteraciones antes que termine una iteracion del bucle externo

# Solicitudes

filas = int(input('Cuantas filas quieres? '))
columnas = int(input('Cuantas columnas quieres? '))
simbolo = input('Introduce el simbolo que quieres ')

# -----------Bucles anidados---------for------------------
# el bucle externo sera responsable de las filas
# el bucle externo sera responsable de las columnas

for i in range(filas):  # este bucle recore el rango de las filas
    for j in range(columnas):  # este bucle recore el rango de las columnas
        print(simbolo, end="")
    # una ves terminado de recorer el for interno haremos un print de un salto de linea
    print("")

# nuestro bucle funciona de la siguiente forma
'''
i = 5
j = 6

en la primera iteracion i = j = 1 se imprimira el valor del simbolo 
pero como j = 6 y esta dentro del bucle for i = 5 

el segundo blocle finalisara cuando j = 6 

en la segunda iteracion i = 2 ahora estariamos en la segunda fila
j =1,2,3,4,5,6

en la tercera iteracion i = 3 ahora estariamos en la tercera fila 
j =1,2,3,4,5,6

en la cuarta iteracion i = 4 ahora estariamos en la cuarta fila 
j = 1,2,3,4,5,6

en la quinta iteracion i = 5 ahora estariamos en la quinta fila 
j = 1,2,3,4,5,6

por ultimo en la sexta iteracion i = 6 estariamos en la sexta fina 
j=1,2,3,4,5,6
y asi finalizara nuestro bucle anidado 

En resumen lo que hicimos es:
usar un bucle for para las filas 
y otro bucle for para las columnas 

'''
