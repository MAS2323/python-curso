# Serializacion: Consiste en guardar en un fichero externo un diccionario, una colleccion o un objeto
# Usamos la biblioteca Pickle para hacer la serializacion

import pickle

# Codigo para crear el fichero binario
"""lista_nombres = ['Pedro', 'Ana', 'Maria', 'Isabel']
fichero_binario = open('lista_nombres', 'wb')
wb = write binary (escritura en binario)

# el metodo dump se usa para crear el fichero binario 
pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del (fichero_binario)
"""

# Codigo para rescatar la informacion del fichero binario
# rb = read benary (lectura en binario)
fichero = open('lista_nombres', 'rb')

# El metodo load se utiliza para cargar la informacion en formato binario
lista = pickle.load(fichero)
print(lista)
