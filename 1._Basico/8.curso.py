# Condicionales
print("Verificacion de acceso")

edad_usuario = int(input("Introduce tu edad por favor: "))

if edad_usuario < 18:
    print("No puedes pasar")
if edad_usuario > 100:
    print("Edad incorrecta")
else:
    print("Puedes pasar")
print("El programa a finalizado")

# Tambien tenemos la opcion de elif cuando tenemos varias condiciones

nota_alumno = int(input("Introduzca tu nota por favor: "))

if nota_alumno < 5:
    print("Insuficiente")

elif nota_alumno > 6:
    print("Suficiente")

elif nota_alumno > 7:

    print("Bien")

elif nota_alumno > 9:

    print("Aprobado")
else:

    print("Sobresaliente")
