# Las listas en python
# Las listas son estructuras de datos que nos permiten almacenar gran cantidad de valores de cualquier tipo
# sintaxis nombreLista = [elem1, elem2, elem3...]

miLista = ['Maria', 66, True, 'Pepe', 'Antonio', 'Carmelo', 78.88]

print(miLista[:])  # Imprimir toda la lista
print(miLista[3])  # Imprimer el tercer elemento de mi lista
# acceder a una porcion de mi lista del primer(o) al segundo elemento(2)
# Cuando usamos esta sintaxis solo se coge del primero al ultimo menos uno ej print(miLista(x, n))= x,...,n-1
print(miLista[0:3])

# Agregar elementos a la ultima posicion de mi lista usamos la funcion append
miLista.append('Sandra')
print(miLista)
# Usamos insert(n1,n2) para determinar donde ira el elemento que agregaremos en nuestra lista n1 = posicion, n2 = elemento a agragar

miLista.insert(2, "Manuel")
print(miLista[:])

# Para agregar varios elementos a una lista utilizamos la funcion extend
miLista.extend(['Ferando', 'Abilio', 'Saturnino'])
print(miLista[:])

# Con la funcion index podemos ver que indice tiene un elemto en una lista
indice = print(miLista.index('Manuel'))
print(indice)

# Funcion para comprobar si un elemto se encuentra en una lista usamos la funcion "in"

valor = "Manuel" in miLista
print(valor)
 
# Para eliminar un elemento de una lista utilizamos la funcion remove

miLista.remove('Manuel')
print(miLista[:])

# Para eliminar el ultimo elemento de nuestra lista utilizamos la funcion pop
miLista.pop()
print(miLista[:])

print("-----------------------------suma de listas---------------------------")
# Operador multiplicacion *, funciona como repetidor
# Operador suma + sirve para concatenar

milista2 = ['Jesus', 'Motu', 'Ela']
miLista3 = miLista + milista2
miLista3*4
print(miLista3[:])
