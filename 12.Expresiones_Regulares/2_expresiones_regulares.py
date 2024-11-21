# Meta caracteres
# #Anclas y clases de caracteres

import re

# listNombres = [
#     'Vicencio Mas',
#     'Consuelo Samiel',
#     'Hermelinda Mas',
#     'Brayan Samiel',
#     'Vicencio Mba'
# ]

# Los metacaracteres tienen su potencial a la hora de trabajar con dominios

# listaDominios = [
#     'http://pildorasinformaticasespaña.es',
#     'ftp://pildorasinformaticas.es',
#     'http://pildorasinformaticas.com',
#     'ftp://pildorasinformaticas.com'
# ]

listaPalabras = [
    'hombre',
    'mujeres',
    'niños',
    'niñas'
]

# el ^ lo que hara es mirar en toda la lista que nombre coincide con Vicencio
# de esta forma nos devolvera el nombre completo
# mientras que el metacaracter $ lo que hace es devolvernos los nombres que
# finalicen con el nombre o caracter Samiel
for elemento in listaPalabras:
    # if re.findall('^Vicencio', elemento):
    # if re.findall('es$', elemento):
    # [oa] es un patros de busqueda para que nos encuentre los niños y niñas
    if re.findall('niñ[oa]s', elemento):
        print(elemento)


# clases de caracteres: son los que se utilizan dentro de un corchete
# en estos corchetes especificaremos patrones de busqueda dentro de un texto
# En este ejemplo lo usaremos para saber si en nuestro dominios existe el caracter ñ
