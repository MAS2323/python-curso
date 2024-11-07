# 1 importar el modulo io: usamos la funcion open para abrir archivos externos
from io import open

archivo_text = open("archivo.txt", "r+")
"""
read "r"
append "a"
weite "w"
lectura y escritura "r+"
"""

# Primera forma
# frase = "Estupendo dia para estudiar python \n Martes"
# archivo_text.write(frase)
# archivo_text.close()

# Segunda forma
# texto = archivo_text.read()
# archivo_text.close()
# print(texto)

# Tercera forma

# lines_texto = archivo_text.readline()
# archivo_text.close()
# print(lines_texto[0])

# Cuarta forma
# Agregar texto a un archivo existente
# archivo_text.write("\n siempre es una buena ocacion para estudiar Python")
# archivo_text.close()

# Quinta forma
# Lee todo lo que se encuentra dentro del archivo
# archivo_text.seek(11)
# print(archivo_text.read(11))
# print(archivo_text.read())
# archivo_text.seek(len(archivo_text.readline()))
# print(archivo_text.read())
# print(archivo_text.read())

# Modo de lectura y escritura r+
# archivo_text.write("Comienzo del texto")
# print(archivo_text.readlines())

lista_texto = archivo_text.readlines()
lista_texto[1] = " Esta linea ha sido incluida desde el exterior \n"

archivo_text.seek(0)

archivo_text.readlines(lista_texto)

archivo_text.close()
