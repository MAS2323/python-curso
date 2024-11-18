# La funcion filter forma parte de las funcion llamadas funciones superior
# La funcion filter sirve para comprobar que los elementos de una secuencia por ejemplo una lista cumple
# una condicion, devolviendo un iterador con los elementos que cumplen dicha condicion

'''def numeroPar(num):

    if num % 2 == 0:

        return True

'''
numeros = [17, 24, 39, 8, 51, 92]

# La funcion filter recibe dos argumentos, por un lado la funcion que queremos llamar
# y que comprueba que numeros son pares y por otro lado la lista de numeros
print(list(filter(lambda numero_par: numero_par % 2 == 0, numeros)))

# Siempre vamos a usar la funcion filter para filtrar objetos
