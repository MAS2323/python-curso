# Que son las funciones lambda y cual es su utilidad
# una funcion lambda es una funcion anonima y se utilizan en python para abreviar
# todo lo que se pueda hacer con una expresion lambda se puede hacer con una funcion normal pero no alreves


# Si a lo largo de nuestro programa utilizaremos esta funcion varias veces viene muy bien usar una funcion lambda
# Siempre se usa una funcion lambda cuando la funcion en cuestion es sencilla

"""def areaTriangulo(base, altura):
    return (base * altura)/2

tringulo1 = areaTriangulo(5,7)

print(areaTriangulo(5, 7))
"""


def area_triangulo(base, altura): return (base*altura)/2


print(area_triangulo(9, 6))
