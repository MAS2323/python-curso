# las expresiones regulares o reg son como minilenjuagues de programacion,
# dentro de otro lenguaje de programacion

# Las expresiones regulares, son una secuencia de caracteres que forman unpatros
# que sirven para realizar busquedas

# sirve para el procesamiento de texto

# -----------para trabajar con expresiones regulares tenemos que importar el modulo re----------

import re

cadena = 'Vamos a aprender expresiones regulares en Python. Python es un lenjuague de sintaxis sencilla'
# metodo seach()
# si lo que queremos buscar en la cadena no esta el programa nos devolvera un None
# print(re.search("aprender", cadena))
textoBuscar = 'aprender'
textoEncontrado = re.search(textoBuscar, cadena)
# el metodo start() lo que hace es devolvernos donde empieza una cadena
print(textoEncontrado.start())
# mientras que el metodo end nos da el numero donde finaliza el texto encontrado
print(textoEncontrado.end())
# el metod span() nos devuelve los dos valores, del star() y el end()
print(textoEncontrado.span())

textoBuscar2 = 'Python'

# el metodo findall nos devuelve todos las coincidencias del texto a buscar en la cadena
print(len(re.findall(textoBuscar2, cadena)))
