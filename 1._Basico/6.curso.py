# Los Diccionarios
# Son estructuras de datos que nos permiten almacenar datos de todo tipo, en el formato de clave: valor
# Sintaxis
miDiccionario = {
    "Alemania": "Berlin",
    "Francia": "Paris",
    "EQG": "Malabo",
    "Reino Unido": "Londres"
}
# Para acceder a los valores del diccionario tenemos que hacerlo con su clave o valor
# Asignar valores a un diccionario
miDiccionario['Italia'] = 'Lisboa'
print(miDiccionario)

miDiccionario['Italia'] = 'Roma'
print(miDiccionario)

# para eliminar un elemento del diccionario: usamos la funcion del
del miDiccionario['Reino Unido']
print(miDiccionario)

print("-------------------------------------Mezclas en diccionarios--------------------------------")
# Ya que un diccionario permite almacenar cualquier tipo de dato, podemos hacer una combinacion

miTupla = ('Reino Unido', 'Francia', 'Alemania')
miDiccionario2 = {
    miTupla[0]: 'Londres',
    miTupla[1]: 'Paris',
    miTupla[2]: 'Berlin'

}

print(miDiccionario2)

miDiccionario3 = {
    23: 'Jordan',
    "Nombre": 'Michael',
    "Equipo": "Chicago",
    "Anillos": {'Temporadas': [1991, 19992, 1996, 1998]}
}
print(miDiccionario3.keys())
print(miDiccionario3.values())
print(len(miDiccionario3))
print(miDiccionario3)
