# rangos dentro de las expresiones regulares:
# Los rangos nos permiten buscar elementos dentro de una lista que contengan:
# un rango de caracteres, numeros o que comiencen por un rango de caracteres o terminen por un rango de caracteres


import re

# lista_nombres = [

#     'Ana',
#     'Maria',
#     'Antonio',
#     'Pedro',
#     'Rosa',
#     'Manuel'
# ]

lista_pedidos = [
    'Ma.1',
    'sa1',
    'Ma2',
    'Ba1',
    'Ma3',
    'Va:1',
    'Va2',
    'Ma4',
    'Ma:A',
    'Ma5',
    'MaB',
    'MaC'
]

for elemento in lista_pedidos:
    # Establecemos el rango dentro de los corchetes
    # [o-t] = que nos devuelva todo lo que este en el rando de la o a la t
    # Ma[0-3A-B] en este caso nos mostrara los pedidos que esten en el rango de 0 a 3 junto los A a B
    # Ma[.:] en este caso mostraremos los pedidos o caracteres que contienen o un punto o dos puntos
    if re.findall('Ma[.:]', elemento):
        print(elemento)
