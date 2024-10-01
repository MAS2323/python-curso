# Uso de Metodos de cadenas
"""nombreUsuario = input("Itroduce tu nombre de usuario: ")
# La funcion capitalize() lo que hace es poner la primera letra en mayuscula
print("El nombre es ", nombreUsuario.capitalize())

"""
edad = input("Introduce la edad: ")

while (edad.isdigit() == False):
    print("Por favor, introduce un valor numerico")
    edad = input("Introduce un valor numerico: ")

if (int(edad) < 18):

    print("No puede pasar")
else:
    print("Puedes pasar")

# Ejercicio 1:
# • Crea un programa que pida introducir una dirección de email por teclado. El programa
# debe imprimir en consola si la dirección de email es correcta o no en función de si esta
# tiene el símbolo ‘@’. Si tiene una ‘@’ la dirección será correcta. Si tiene más de una o
# ninguna ‘@’ la dirección será errónea. Si la ‘@’ está al comienzo de la dirección de email
# o al final, la dirección también será errónea,

email = input("Introduce tu direccion de email: ")
