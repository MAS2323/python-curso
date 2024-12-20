# Las tuplas
# Las tuplas son listas inmutables, es decir no se pueden modificar despues de su creacion
# Sintaxis nombreTupla =(elem1, elem2, elem3 .....)

miTupla = ("Juan", 23, 3, 1998)
miLista = ["Juan", 23, 3, 1998]
print(miTupla[0])

# Metodos aplicables a las tuplas
# Convertir de lista a tupla y viceversa

miLista = list(miTupla)  # De tupla a lista # metodo list()
print(miLista[:])

miTupla = tuple(miLista)  # DE lista a tupla # metodo tuple
print(miTupla)

# Una tupla tambien permite el metodo in para comprobar si hay un elemto en la tupla

print('Juan' in miTupla)

# El metodo count nos permite averiguar que elemteos se encuentran en una tupla o lista de forma repetida
# El argumento que le pasamos es el elemento que deseamos buscar, es decir elemento que deseamos ver si se repite
# en la lista o tupla: lo que retorna es el numero de veces que se encuentyra ese elento en nuestra tupla o lista
print(miTupla.count(23))

# El metodo len nos permite conocer la longitud de la tupla
print(len(miTupla))

# Tuplas unitarias: son tuplas con un unico elemento
miTuplaUnitaria = ('Antonio')
print(len(miTuplaUnitaria))

# A la hora de crear una tupla los parentecis son opcionales
# Cuando escribimos una tupla sin parentecis lo conocemos como empaquetado de una tupla
miTupla2 = 'Manolo', 13, 1, 1994
print(miTupla2)
nombre, dia, mes, agno = miTupla2  # Empaquetado
print(nombre)
print(dia)
print(mes)
print(agno)
