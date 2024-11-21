# dos funciones del modulo re
# Match y seach # estas expresiones son muy utilizada a la hora de buscar patros dentro de cadenas de texto

import re

cadena1 = 'Jara Onewe'
cadena2 = '42536796483'
nombre2 = 'a556739374'

# la funcion Match lo que hace es buscar si hay una coincidencia en un patron de busqueda al comienzo de una cadena de texto
# Para que la funcion match ingnore mayusculas y minusculas usamos una tercera expresion re.ING
# \d (d=digit o digito) lo que hace este patron en la funcion match es mirar si una cadena de texto empieza por un numero
if re.match("\d", cadena2):
    print('hemos encontrado el numero')

else:
    print('No lo hemos encontrado')
